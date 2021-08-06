import pandas as pd

# Create Dataframe using CSV file
df = pd.read_csv("Weather_CSV_File_1.csv")

#Create Dataframe using excel file
df1 = pd.read_excel("Weather_Excel_File_1.xlsx","Sheet1")

#Create using Dictionary
weather_data = {
    'day' : ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature' : [32,35,28],
    'windspeed' : [6,7,2],
    'event' : ['Rain','Sunny','Snow']
}
df2 = pd.DataFrame(weather_data)

#Create using Tupple
weather_datas = [
    ('1/1/2017',32,6,'Rain'),
    ('1/2/2017',35,7,'Sunny'),
    ('1/3/2017',28,2,'Snow')
]

df3 = pd.DataFrame(weather_datas, columns=['day','temperature','windspeed','event'])

print(df)

print(df1)

print(df2)

print(df3)
