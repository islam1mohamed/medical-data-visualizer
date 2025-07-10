import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

BMI = df['weight'] / ((df['height'] / 100) ** 2)

# 2
df['overweight'] = (BMI > 25).astype(int)

# 3
df['cholesterol'] = (df['cholesterol']>1).astype(int)
df['gluc'] = (df['gluc']>1).astype(int)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df,  id_vars=["cardio"],value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size()


    # 7
    # Rename 'size' column to 'total'
    df_cat.rename(columns={'size': 'total'}, inplace=True)

    # 8
    fig = sns.catplot(
        # figsize=(10, 6),
        data=df_cat,
        x="variable",
        hue="value",
        col="cardio",
        kind="bar",
        y="total",   
        height=6,
        aspect=1.5
    )
    fig.set_axis_labels("variable", "total")
    fig.set_titles("{col_name} Cardio")
    fig.set_xticklabels(['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # plt.show()   

    # 9
    fig.savefig('catplot.png')
    return fig.fig

# 10
def draw_heat_map():
    # 11
    df_heat= df[(df['ap_lo'] <= df['ap_hi'])& (df['height'] >= df['height'].quantile(0.025))& (df['height'] <= df['height'].quantile(0.975))& (df['weight'] >= df['weight'].quantile(0.025))& (df['weight'] <= df['weight'].quantile(0.975))]
    
    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu ( np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(12, 10))

    # 15
    sns.heatmap(corr ,mask= mask, cmap= 'coolwarm', annot=True, fmt='.1f', linewidths=0.5, cbar_kws={"shrink": .8})

    # 16
    fig.savefig('heatmap.png')
    return fig
