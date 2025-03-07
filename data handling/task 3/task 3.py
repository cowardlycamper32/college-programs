import chardet
import pandas as pd
from nlib.novasroutines import logInit as logInit, writeLog as writeLog, closelog as closeLog
log = logInit("data handling 3/task 3.py")
with open("spotify-2023.csv", "rb") as f:
    result = chardet.detect(f.read())
    writeLog(log, result)
#Subtasks
#1
df = pd.read_csv("./spotify-2023.csv")

print(df.head(10))
writeLog(log, "\n" + df.head(10).to_string())

#2
print(df.info())
writeLog(log, df.info())
print(df.shape)
writeLog(log, df.shape)

#3
df = df.rename(columns = {"artist(s)_name" : "artist_names"})
writeLog(log, df.head(10))
#4
print(df.duplicated().sum())
writeLog(log, df.duplicated().sum())

#5
print(df.isnull().sum())
writeLog(log, df.isnull().sum())
#6
unique_artist_names = df["artist_names"].nunique()
print(unique_artist_names)
writeLog(log, unique_artist_names)

#7
