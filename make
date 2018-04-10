#!/bin/bash

trap "exit" INT
#set -e

echo "compiling main document"
xelatex sw_thesis.tex
bibtex sw_thesis
xelatex sw_thesis.tex
xelatex sw_thesis.tex


#echo "compiling individual chapters"
#while read chapter; do
#    short_name=$(echo "$chapter" | cut -d "_" -f2)
#    chapter_path="$chapter"/"$short_name"
#    xelatex "$chapter_path"
#    bibtex "$chapter_path"
#    bibtex "$chapter_path"
#    xelatex "$chapter_path"
#done < chapter_list.txt

echo "clearing out rubbish..."

exts=(.latexmk .aux .bcf .bbl .blg .lof .lot .log .run.xml .out .toc .log blx.bib)

for ext in ${exts[@]}; do
    if [ -f *"$ext" ]; then
        rm *"$ext"
    fi
done

for ext in ${exts[@]}; do
    filepath="*/*$ext"
    if [ -f "$filepath" ]; then
        rm -rf "$filepath"
    fi
done

if [ -f missfont.log ]; then
    rm missfont.log
fi

exit 0
