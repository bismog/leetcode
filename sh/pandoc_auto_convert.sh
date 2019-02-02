#!/usr/bin/env bash

## This script is for automatically converting markdown to html via pandoc

markdown_list=$(find ./ -name "*.md" -o -name "*.markdown" | xargs)
for md in $markdown_list;do
    html_file=${md%.*}.html
    pandoc -s --toc --toc-depth=5 --number-sections -o $html_file $md
done
