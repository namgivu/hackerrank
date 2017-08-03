#!/usr/bin/env bash

#get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
s=${BASH_SOURCE} ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; SCRIPT_HOME=$s

#python path
h="$SCRIPT_HOME/.." ; h=$(cd "$h" && pwd) ; HACKERRANK_HOME=$h
export PYTHONPATH="$HACKERRANK_HOME:$PYTHONPATH"

#do run
python application.py < input.txt > output.txt
