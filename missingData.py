import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['figure.figsize'] = (10,10)
pd.options.mode.chained_assignment = None

df = pd.read_csv('wfpvam_foodprices.csv')
cols = df.columns 
colours = ['#000099', '#ffff00'] # yellow = missing data.
sns.heatmap(df[cols].isnull(), cmap=sns.color_palette(colours))
#plt.savefig("Graphs/missing_data.png")
plt.show()


