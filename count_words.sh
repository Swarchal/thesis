#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
MASTER_DOC=/home/scott/Dropbox/thesis/sw_thesis.tex

DATE=`date '+%Y-%m-%d'`
WORDCOUNT=$(/usr/bin/texcount $MASTER_DOC -inc -total | grep "Words in text" | cut -d ' ' -f 4)
echo -e "$DATE""\t""$WORDCOUNT" >> /home/scott/Dropbox/thesis/word_count.tsv

exit 0
