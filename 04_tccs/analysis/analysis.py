import morar
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from sklearn.decomposition import PCA
import numpy as np

plt.style.use(["seaborn-ticks", "seaborn-muted", "seaborn-paper"])

data = pd.read_csv("../data/df_cell_subclass.csv")

data.Metadata_concentration = data.Metadata_concentration / 1e9

# change baraserib and ZM447439 MoA to Aurora B inhibitors
data.loc[data.Metadata_compound == "barasertib", "Metadata_compoundClass"] = "Aurora B inhibitor"
data.loc[data.Metadata_compound == "ZM447439", "Metadata_compoundClass"] = "Aurora B inhibitor"

def metacols(dataframe):
    return [i for i in dataframe.columns if i.startswith("Metadata_")]

def datacols(dataframe):
    return [i for i in dataframe.columns if not i.startswith("Metadata_")]

pca_out = PCA(n_components=2).fit_transform(data[datacols(data)],
                                            data["Metadata_compoundClass"])


metadata = data[metacols(data)]

pca_df = pd.DataFrame(pca_out, columns=["PC1", "PC2"])
pca_df = pd.concat([pca_df, metadata], axis=1)

pca_df = pca_df.query("Metadata_CellLine == 'MDA231'")

colours = "#E41A1C #999999 #4DAF4A #984EA3 #FF7F00 #e8e800 #A65628 #F781BF #000000 #377EB8"
colours = colours.split()[::-1]

pca_agg = morar.aggregate(pca_df, on=["Metadata_unique_plate", "Metadata_Well"],
                          method="median")


plt.figure(figsize=[8, 10])
plt.subplot(211)
plt.title("PCA of compounds response, averaged per image", loc="left", fontweight="bold")
plt.grid(linestyle=":")
for i, (name, group) in enumerate(pca_df.groupby("Metadata_compoundClass", sort=True)):
    zorder = 100 if name == "DMSO" else 1
    plt.plot(group.PC1, group.PC2, "o", label=name, alpha=0.4, c=colours[i], zorder=zorder)
leg = plt.legend()
for lh in leg.legendHandles:
    lh._legmarker.set_alpha(1)
plt.ylim([-20, 35])
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.subplot(212)
plt.title("PCA of compounds response, averaged per well", loc="left", fontweight="bold")
plt.grid(linestyle=":")
for i, (name, group) in enumerate(pca_agg.groupby("Metadata_compoundClass", sort=True)):
    zorder = 100 if name == "DMSO" else 1
    plt.plot(group.PC1, group.PC2, "o", label=name, alpha=0.4, c=colours[i], zorder=zorder)
leg = plt.legend()
for lh in leg.legendHandles:
    lh._legmarker.set_alpha(1)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()
plt.savefig("../../figs/ch3pcaClustering.pdf")

bara = pca_agg.query("Metadata_compound == 'barasertib'")
bara = bara.sort_values("Metadata_concentration")

cyclo = pca_agg.query("Metadata_compound == 'cycloheximide'")
cyclo = cyclo.sort_values("Metadata_concentration")

plt.figure(figsize=[11, 6])
plt.grid(linestyle=":")
plt.plot(pca_agg.PC1, pca_agg.PC2, "o", label=name, alpha=0.7, c="gray")
plt.plot(bara.PC1, bara.PC2, linewidth=2, c="black", alpha=0.5)
plt.scatter(bara.PC1, bara.PC2, s=50, c=bara.Metadata_concentration,
            norm=colors.LogNorm(), cmap=plt.cm.viridis, zorder=100)
plt.colorbar()
plt.plot(cyclo.PC1, cyclo.PC2, linewidth=2, c="black", alpha=0.5)
plt.scatter(cyclo.PC1, cyclo.PC2, s=50, c=cyclo.Metadata_concentration,
            norm=colors.LogNorm(), cmap=plt.cm.plasma, zorder=100)
plt.colorbar()
for lh in leg.legendHandles:
    lh._legmarker.set_alpha(1)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.tight_layout()
plt.show()

