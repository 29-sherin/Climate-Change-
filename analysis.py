import pandas as pd
from pandas_datareader import wb
import matplotlib.pyplot as plt
import numpy as np

ind1='EN.ATM.CO2E.PC' # metric tons of CO2 per capita
ind2='EG.USE.PCAP.KG.OE' # Energy use (kg of oil equivalent) per capita

def get_df(file):
    """Enter a csv file or a csv file path containing countries as the headings line"""
    mn=pd.read_csv(file)
    mn_l=list(mn)
    df1=wb.download(indicator=ind1,country=mn_l,start=2010,end=2014)
    df2=wb.download(indicator=ind2,country=mn_l,start=2010,end=2014)
    df=pd.merge(df1,df2,how='inner',left_index=True,right_index=True)
    df.columns=['metric tons of CO2 per capita','Energy use (kg of oil equivalent) per capita']
    df.reset_index(0,inplace=True)
    df.reset_index(0,inplace=True)
    yr_cols=df.pivot_table(index='country',columns='year',values='metric tons of CO2 per capita')
    yr_cols.reset_index(0,inplace=True)
    cntry_cols=df.pivot_table(index='year',columns='country',values='Energy use (kg of oil equivalent) per capita')
    cntry_cols.reset_index(0,inplace=True)
    return yr_cols,cntry_cols

filename="countries.csv"

# yr_df is the CO2 produced in metric tons per capita in a year
# cntry_df is the energy used per capita in in each country
yr_df,cntry_df=get_df(filename)

#getting the dataframes information
yr_df.describe()
cntry_df.describe()

#plotting bar plots for both dataframes

yr_df.plot(kind='bar',x='country');
cntry_df.plot(kind='bar',x="year");

#plotting line graphs
yr_df.plot(kind='line',x='country');
cntry_df.plot(kind='line',x='year');

#building up for correlation

mn_l=["USA","DEU","CHN","CAN","BRA"]

df1=wb.download(indicator=ind1,country=mn_l,start=2010,end=2014)
df2=wb.download(indicator=ind2,country=mn_l,start=2010,end=2014)
df=pd.merge(df1,df2,how='inner',left_index=True,right_index=True)
df.columns=['metric tons of CO2 per capita','Energy use (kg of oil equivalent) per capita']

df.reset_index(0,inplace=True)
df.reset_index(0,inplace=True)
# generating a correlation table
df_v=df[["metric tons of CO2 per capita","Energy use (kg of oil equivalent) per capita"]].corr()

# plotting the correlation map
plt.imshow(df_v, cmap='hot', interpolation='nearest')











