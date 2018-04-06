#!/bin/sh

trap "exit" INT
#set -e

xelatex sw_thesis.tex
bibtex sw_thesis
xelatex sw_thesis.tex
xelatex sw_thesis.tex

echo "clearing out rubbish..."

rm *.aux *.log *.out *.bcf *.bbl *.blg *.lof *.lot *.run.xml *.toc

if [ -f missfont.log ]; then
    rm missfont.log
fi

exit 0
