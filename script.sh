rm data/result.xlsx

killall -9 "Microsoft Excel"

./main.py

open data/result.xlsx