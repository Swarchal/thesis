#!/bin/bash

trap "exit" INT
#set -e

MASTER_DOC=sw_thesis.tex

echo "compiling main document"
xelatex -shell-escape "$MASTER_DOC"
bibtex sw_thesis
xelatex -shell-escape "$MASTER_DOC"
xelatex -shell-escape "$MASTER_DOC"

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

echo "================================================================================"
echo "                                word count                                      "
echo "================================================================================"
texcount "$MASTER_DOC" -inc -total

exit 0
