#!/bin/bash
#Usage: ./do 

py="python3"

mkdir -p res

echo "Preprocessing... "
for i in */*/*.xml ; do
	src="$i"
	target="${src%.xml}.pre.txt"
	[[  -f "$target" ]] || "$py" PreProcess.py "$src" "$target" || echo "PreProcess: $src --> $target error" &
done
wait

echo  "Generating dictionaries... "
for i in */*/*.pre.txt ; do
	src="$i"
	target="${src%.pre.txt}.dict.pkl"
	[[  -f "$target" ]] || "$py" Dict.py "$src" "$target" || echo "Dict: $src --> $target error" &
done
wait

unset target
unset src

echo  "Generating statistics..."
[[ -f res/stats.pkl ]] || "$py" Stat.py || echo "Stat: error"
#[[ -f res/stats.pkl ]] && "$py" PrintFreq.py > res/top10.txt 
[[ -f res/pair.pkl ]] || "$py" Pair.py || echo "Pair: error"
[[ -f res/triple.pkl ]] || "$py" Triple.py || echo "Triple: error"

#echo 'Run `python Confusion.py naive` for naive confusion matrix. Run `python Confusion.py hmm` for hmm confusion matrix'

echo "Predicting test tags..."
for i in Test-corpus/*/*.pre.txt ; do
	src="$i"
	target1="${src%.pre.txt}.naive.tags"
	target2="${src%.pre.txt}.hmm.tags"
	echo -ne "Current file: ${src}\r"
	[[  -f "$target1" ]] || "$py" Predict.py "$src" "$target1" "naive" || echo "Predict: $src --> $target error"
	[[  -f "$target2" ]] || "$py" Predict.py "$src" "$target2" "hmm" || echo "Predict: $src --> $target error"
done

echo "Generating confusion matrices and evaluating performance..."
target1="res/hmm.conf.pkl"
target1="res/naive.conf.pkl"
[[  -f "$target1" ]] || "$py" Confusion_Matrix.py  "naive" || echo "Confusion_Matrix: $src --> $target error"
[[  -f "$target2" ]] || "$py" Confusion_Matrix.py  "hmm" || echo "Confusion_Matrix: $src --> $target error"
"$py" Performance.py
