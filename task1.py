
import pandas as pd

df = pd.read_csv('sales_data.csv')

df['customer_name'] = df['customer_name'].str.strip().str.title()

df['age'] = df['age'].where(
    (df['age'] >= 0) & (df['age'] <= 100)
)
df['email'] = df['email'].fillna("unknown")



df['amount'] = df['amount'].replace(r'[\$,]', '', regex=True).astype(float)

df['city'] = df['city'].str.title()



df['purchase_date'] = pd.to_datetime(
    df['purchase_date'], dayfirst=True, format='mixed'
).dt.strftime('%Y-%m-%d')

df = df.drop_duplicates() 
print(df)
df.to_csv(r'D:\project_data\final_sales_clean.csv', index=False, encoding='utf-8-sig')