#!/bin/bash
awk '/Aron/{first_name=$2;last_name=$3;print first_name,last_name;}' names.txt
