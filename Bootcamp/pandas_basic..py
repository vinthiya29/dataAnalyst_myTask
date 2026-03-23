import pandas as pd

df = pd.read_csv("Sample - Superstore.csv")
print("Dataset Loaded")

print(df.head(5))


print("Missing Values\n", df.isnull().sum())
print(df[df['Sales']>1000])
# print(df.groupby('Category')['Sales'].sum())

# df['Cost'] = df['Sales'] - df['Profit']
# df['New_Profit'] = df['Sales'] - df['Cost']
# print("New_Profit:\n", df[['Sales', 'Cost', 'Profit']].head())

#
# df_sorted = df.sort_values(by='Sales', ascending=False)
# print("Sorted Values\n", df_sorted.head())





# # Save file
df.to_csv("cleaned_data.csv", index=False)
print("File saved")