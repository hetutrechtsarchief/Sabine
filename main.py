#!/usr/bin/env python3

import csv,re,sys,datetime
from collections import defaultdict
from tqdm import tqdm
from rapidfuzz import process, fuzz
from xlsxwriter.workbook import Workbook

def getFuzzyMatch(input_str, compare_strs): #, compare_lowered_option_strs=None):
	(most_likely_option, match_percentage, idx) = process.extractOne(input_str, compare_strs, scorer=fuzz.ratio)
	return match_percentage, most_likely_option

# deze nieuwe aanpak maakt gebruik van een tip van Ivar waarbij ik in Google Sheets 4 velden aan elkaar plak en gekke tekens strip.
# =TRIM(REGEXREPLACE(REGEXREPLACE(JOIN(" ",B2,C2,D2,E2),"[^a-zA-Z0-9\-]"," "),"\s+"," "))
# in de Sabine sheet wordt ook een extra formule gebruikt om voor- en achternaam van auteur om te draaien voor een exactere match:
# =IFERROR(REGEXEXTRACT(C2,".*,\s(.*)") & " " & REGEXEXTRACT(C2,"(.*),"),C2)

input_sabine_filename = "data/sabine-tbl01.csv"
input_hua_filename = "data/hua-artikelen.csv"
output_filename = "data/result.xlsx"
logfile = open("data/logfile.tsv","w")

workbook = Workbook(output_filename)
workbook.set_size(2500,1500)
worksheet = workbook.add_worksheet()
wrap = workbook.add_format()
wrap.set_text_wrap()

worksheet.freeze_panes(1, 0)  # Freeze the first row.
worksheet.set_column(0, 0, 10) # Status
worksheet.set_column(1, 1, 10) # Score
worksheet.set_column(2, 2, 130, wrap) # HUA title
worksheet.set_column(3, 3, 130, wrap) # Sabine title

row_nr = 1

#################################
sabine_artikelen = []
for row in csv.DictReader(open(input_sabine_filename), delimiter=","):
	if row["dat14"]: # only items with link
		sabine_artikelen.append(row)

##################################
hua_artikelen = [ row for row in csv.DictReader(open(input_hua_filename), delimiter=",") ]
by_concat = defaultdict(list)
by_guid = {}
for artikel in hua_artikelen:
	concat = artikel["CONCAT"].strip()  # concat is een combi van "titel, auteur, pagina, jaar" stripping everything but alpha,digits,dashes separated by spaces
	GUID = artikel["GUID"]
	by_guid[GUID] = concat
	by_concat[concat].append(GUID)

##################################
for sabine_index, sabine_row in enumerate(tqdm(sabine_artikelen)):
	sab_concat = sabine_row["CONCAT"]

	highestScore = 0
	best_match_hua = None
	best_match_sabine_index = None

	score, best_match_hua = getFuzzyMatch(sab_concat, by_concat.keys())

	guid = by_concat[best_match_hua][0]
	sab_link = sabine_row["dat14"]

	if score>=50:
		worksheet.write(row_nr, 1, round(score))
		worksheet.write(row_nr, 2, f'=hyperlink("https://hetutrechtsarchief.nl/collectie/{guid}","{best_match_hua}")')
		worksheet.write(row_nr, 3, f'=hyperlink("{sab_link}","{sab_concat}")')
		row_nr += 1

###################################
worksheet.add_table(0,0,row_nr-1,3,{'columns': [{'header': 'Status'},{'header': 'Score'},{'header': 'HUA'},{'header': 'Sabine'}]})
workbook.close()

