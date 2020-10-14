#!/bin/bash
#Usage: ./do 

py="python3"

for i in */*/*.xml ; do
	src="$i"
	target="${src%.xml}.pre.txt"
	[[  -f "$target" ]] || "$py" PreProcess.py "$src" "$target" || echo "PreProcess: $src --> $target error" 

	src="$target"
	target="${target%.pre.txt}.dict.pkl"
	[[  -f "$target" ]] || "$py" Dict.py "$src" "$target" || echo "Dict: $src --> $target error" 

done

unset target

if [[ !	-f res/stats.pkl ]] ; then
	for i in Train-corpus/*/*.dict.pkl ; do
		src="$i"
		"$py" Stat.py "$src" || echo "Stat: $src error"
		done
fi
