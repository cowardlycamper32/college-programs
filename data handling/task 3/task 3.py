import pandas as pd
from nlib.novasroutines import logInit as logInit, writeLog as writeLog, closelog as closeLog
log = logInit("data handling 3/task 3.py")

#Subtasks
#1
df = pd.read_csv("./spotify-2023.csv")

print(df.head(10))
writeLog(log, "\n" + df.head(10).to_string())

#2
print(df.info())
print(df.shape)

#3
df = df.rename(columns = {"artist(s)_name" : "artist_names"})
#4
print(df.duplicated().sum())

#5
print(df.isnull().sum())

#6
unique_artist_names = df["artist_names"].nunique()
print(unique_artist_names)

#7
