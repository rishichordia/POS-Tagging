#!/bin/bash
#Usage: ./do 

py="python3"

for i in Train-corpus/*/*.xml ; do
	src="$i"
	target="${src%.xml}.pre.txt"
	[[  -f "$target" ]] || "$py" PreProcess.py "$src" "$target" || echo "$src --> $target error" 

	src="$target"
	target="${target%.pre.txt}.dict.pkl"
	[[  -f "$target" ]] || "$py" Dict.py "$src" "$target" || echo "$src --> $target error" 
done
