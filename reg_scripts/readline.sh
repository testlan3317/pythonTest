#!/bin/bash
File=$1
NO_line=$2
count=0
while read line;do
  count=$(( $count+1 ))
  if [ $count -eq $NO_line ]
  then
    #echo $count $line
    echo $line
  fi
done <$File
