#!/bin/bash
function usage() {
    echo "+++++++++++ Manual Start +++++++++++++++++++++++++++"
    echo "usage: "
    echo "./reg_scripts switch_number"
    echo "+++++++++++ Manual End   +++++++++++++++++++++++++++"
}

[ $# -lt 1 ]&&usage&&exit -1

#if [ ${#1} -lt 16 ];then echo "invalid"&&exit -1;fi
#if [ -d /etc/elasticsearch ]
#then
#  echo "it's a directory"
#fi

# when run the directory check, it'll need absolute path

for files in $(ls /etc/$1);do  
  if [ -d /etc/$1/$files ]; then
      #echo $files is a directory
      echo "-----ignore the folders-----"
  else
      #echo $files is a file
      echo $files
  fi
  
done;
echo ${#1}

if [ $2==NULL ]; then echo "null";fi
