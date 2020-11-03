#!/bin/bash
#Usage: ./do 

py="python3"

mkdir -p res

for i in */*/*.xml ; do
	src="$i"
	target="${src%.xml}.pre.txt"
	[[  -f "$target" ]] || "$py" PreProcess.py "$src" "$target" || echo "PreProcess: $src --> $target error" 

	src="$target"
	target="${target%.pre.txt}.dict.pkl"
	[[  -f "$target" ]] || "$py" Dict.py "$src" "$target" || echo "Dict: $src --> $target error" 

done

unset target
unset src

[[ -f res/stats.pkl ]] || "$py" Stat.py || echo "Stat: error"
[[ -f res/stats.pkl ]] && "$py" PrintFreq.py > res/top10.txt 
[[ -f res/pair.pkl ]] || "$py" Pair.py || echo "Pair: error"
