# %%
# Loading the necessary libraries both data frame and plot libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Reading the data into a dataframe
vg_data=pd.read_csv('../Data/vgsales.csv')

# vg_data.describe()
#vg_data.value_counts(ascending=False)
# 1. Video Games Sales per Year
# **Important Note**: We group sales by the year of release. Not by the real sale date as we dont have much historical data.
# Total Sales
gd_sales= vg_data.groupby(['Year']).sum()
gd_sales.reset_index(inplace=True)
top_games=50
vg_data.head(10)


# Grouped Data
vg=vg_data.groupby(['Platform','Publisher']).agg({"Global_Sales":sum}, ascending=True)
vg.reset_index (inplace=True)

fig=px.treemap(vg, path=['Platform', 'Publisher'], values='Global_Sales')
fig.show()

fig.write_html("treemapHelper.html")