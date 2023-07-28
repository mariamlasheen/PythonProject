import pandas as pd 
import csv

#Loading the csv file
path='C:\\Users\\Mariam\\Employees.csv'
df=pd.read_csv(path)




#remove duplicated
df.drop_duplicates(inplace=True)


#remove deciamal age
df['Age']=df['Age'].astype(int)



#convert usd to egp currency

def converting_usd_to_egp(usd):
    usd_currency=30.90
    return round(usd * usd_currency)


df['Salary(EGP)']=df['Salary(USD)'].apply(converting_usd_to_egp)
df=df.drop(columns=['Salary(USD)'])






#print stats
gender_counts = df['Gender'].value_counts()
male_to_female_ratio = gender_counts['M'] / gender_counts['F']

print(round(df['Age'].mean()))
print(df['Salary(EGP)'].median())
print(male_to_female_ratio)



#writhe the new csv file
df.to_csv('C:\\Users\\Mariam\\vs_New_Employees.csv', index=False)
