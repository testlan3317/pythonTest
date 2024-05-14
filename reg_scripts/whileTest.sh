#!/bin/bash

i=0

while [[ $i -lt 5 ]]
do
  ((i++))
  if [[ $i -eq 2 ]]; then
      continue
  fi
  echo "number: $i"
done

echo "All Done!"
