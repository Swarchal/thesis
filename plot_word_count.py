#!/usr/bin/env python

import datetime
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.style.use("seaborn-ticks")

default_blue = "#1f77b4"

data = pd.read_table("word_count.tsv")
data.date = pd.to_datetime(data.date)

# replace zero values with NaN
data.word_count.replace(0, np.nan, inplace=True)
# fill missing values with previous
data.word_count.ffill(inplace=True)

plt.step(data.date, data.word_count)
plt.grid(linestyle=":")
plt.xlim([datetime.date(2018, 5, 1),
          datetime.date(2018, 9, 5)])

#plt.hlines(y=20000,
#           xmin=datetime.date(2018, 5, 8),
#           xmax=datetime.date(2018, 8, 31),
#           linestyle=":")
plt.vlines(ymin=0, ymax=20000,
           x=datetime.date(2018, 8, 1),
           linestyle=":")

plt.vlines(ymin=0, ymax=20000,
           x=datetime.date(2018, 8, 31),
           linestyle=":")

x = [datetime.date(2018, 6, 16), datetime.date(2018, 7, 1)]
plt.axvspan(*x, alpha=0.1, color="darkorange")
plt.annotate("job interviews\n& conference",
             (datetime.date(2018, 6, 17), 7000),
             fontsize=6, color="darkorange", fontweight="bold")

plt.annotate("self-imposed deadline",
             (datetime.date(2018, 8, 2), 15000),
             fontsize=8, color=default_blue,
             fontweight="bold", rotation=90)

plt.annotate("submission deadline",
             (datetime.date(2018, 9, 1), 15000),
             fontsize=8, color=default_blue,
             fontweight="bold", rotation=90)

plt.ylim([0, 25000])
plt.xticks(rotation=90)
plt.ylabel("word count")
plt.title("Thesis word count over time", fontweight="bold")
plt.tight_layout()
plt.savefig("word_count.pdf")
