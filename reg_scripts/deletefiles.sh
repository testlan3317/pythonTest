#!/bin/bash

dbfile=$(find ./ -name "aptserver_sys*")
dbfiles=( $dbfile )
#echo ${#dbfiles[@]}
echo ${dbfiles[*]}
for (( i=0;i<${#dbfiles[@]};i++ ))
do
  cdate=$(echo ${dbfiles[$i]}|awk -F "_sys" '{print $2}'|sed 's/\.sql//g')
  #echo $cdate
  now_date=$(date +%Y%m%d)
  file_date=$(date +%s -d $cdate)
  cur_date=$(date +%s -d $now_date)
  #echo $file_date
  #echo `expr $(expr $cur_date - $file_date ) / 86400` 
  if [ `expr $(expr $cur_date - $file_date ) / 86400` -gt 28 ]
  then
    echo "greater than 28, delete ${dbfiles[$i]}"
    rm ${dbfiles[$i]}
  fi

done
