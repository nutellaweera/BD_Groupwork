import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('wfpvam_foodprices.csv')
df = df.drop(columns=['country id', 'locality id', 'market id', 'commodity purchase id', 'currency id', 'market type id', 'measurement id', 'mp_commoditysource', 'locality name'])




