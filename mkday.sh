#!/usr/bin/env bash
DAY=$1

if [ -z $DAY ]
then 
    echo "Bad day"
    exit 1
fi


DAY_DIR=day$(printf "%02d" $DAY)

if [ -d $DAY_DIR ]
then
    echo "Bad day"
    exit 1
fi

mkdir -p $DAY_DIR
cp template.py $DAY_DIR/p1.py
touch $DAY_DIR/input.txt
