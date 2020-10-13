#!/bin/bash

py="python3"
py_task="PreProcess.py"

for i in */*/*.xml ; do
  "$py" "$py_task" $i ${i%.xml}.pre.txt
done
