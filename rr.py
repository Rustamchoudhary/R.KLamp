import pandas as pd

#Reading data frame csv fille
df = pd.read_csv ('company_sales_data.csv')

print(df.duplicated())
#df_duplicates = df.drop_duplictes()
