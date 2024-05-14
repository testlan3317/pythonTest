#!/bin/bash

awk '{ print "Record: ", NR, "has",NF,"fields"; }' ./names.txt
