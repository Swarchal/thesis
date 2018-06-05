import datetime
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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

plt.hlines(y=20000,
           xmin=datetime.date(2018, 5, 8),
           xmax=datetime.date(2018, 8, 31),
           linestyle=":")
plt.vlines(ymin=0, ymax=20000,
           x=datetime.date(2018, 8, 1),
           linestyle=":")

plt.vlines(ymin=0, ymax=20000,
           x=datetime.date(2018, 8, 31),
           linestyle=":")

plt.ylim([0, 30000])
plt.xticks(rotation=90)
plt.ylabel("word count")
plt.title("thesis word count")
plt.tight_layout()
plt.savefig("word_count.pdf")
