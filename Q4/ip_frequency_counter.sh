#!/bin/bash

filename=$1

if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit
fi

cat $1| grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}"| sort -h |uniq -c


