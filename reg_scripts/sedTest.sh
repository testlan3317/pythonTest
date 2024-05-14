#!/bin/bash

sed 's/unix/linux/' geekfile.txt

# here "s" specifies the substitution operation
# "/" are delimiters.
# "unix" is the search pattern
# "linux" is the replacement
#
# by default, the sed command replaces the first occurance of the pattern only
#
# using nth to replace the specific occurance
# sed 's/<pattern>/<replacment>/nth' filename 
# sed 's/unix/linux/2' geekfile.txt
#
# replacing all with g: means global
# sed 's/unix/linux/g' geekfile.txt
#
# replacing from nth to the rest in a line 
#
# sed 's/unix/linux/3g' geekfile.txt
#
# replacing string on a specific line number
#
# sed '3 s/unix/linux/' geekfile.txt
#
# replacing string on a range of lines
# sed '1,3 s/unix/linux/' geekfile.txt
#
# replacing 2 to $(the last line of the file)
# sed '2,$ s/unix/linux/' geekfile.txt
