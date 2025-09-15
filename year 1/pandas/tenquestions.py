import pandas as pd
from numpy.ma.extras import column_stack


def questionone():
    df = pd.read_csv("car_crashes.csv")
    return df

def questiontwo(df):
    return df.info()

def questionthree(df):
    return df.info()

def questionfour(df):
    df.rename(columns={'abbrev': 'state'}, inplace=True)
    return df

def questionfive(df):
    return df["speeding"].sum()

def questionsix(df):
    return df[["alcohol", "state"]].groupby("state")


def main():
    df = questionone()
    print(questiontwo(df))
    print("\n\n\n------\n\n\n")
    print(questionthree(df))
    print("\n\n\n------\n\n\n")
    print(questionfour(df))
    print("\n\n\n------\n\n\n")
    print(questionfive(df))
    print("\n\n\n------\n\n\n")
    print(questionsix(df))

main()