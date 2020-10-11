#!/bin/bash

task=$(pwd)/PreProcess.py

for i in */*/*.xml ; do
  "$task" $i ${i%.xml}.txt
done
