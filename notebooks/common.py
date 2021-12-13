import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def vis_correlation_matrix(corr: np.ndarray, figsize=(15, 14)):


    mask = np.triu(np.ones_like(corr, dtype=bool))
    _ = plt.figure(figsize=figsize)
    cmap = sns.diverging_palette(230, 20, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(
        corr,
        mask=mask,
        cmap=cmap,
        vmin=-1,
        vmax=1,
        center=0,
        annot=True,
        fmt=".2f",
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5},
    )
    plt.show()