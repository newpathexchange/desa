#!/bin/bash

file=$1
thresh=$2

# Default file
if [ -z "$file" ]; then
  file=/tmp/alive.txt
fi

# Default threshold 20 seconds
if [ -z "$thresh" ]; then
  thresh=20
fi

if [ -f "$file" ]; then
  file_age=$(($(date +%s) - $(date +%s -r "$file")))
  [ $file_age -lt $thresh ]
else
  exit 1
fi

