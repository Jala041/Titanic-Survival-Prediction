import pandas as pd

df = pd.read_csv("data\raw\train.csv")

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

df = df.drop(columns=["Cabin"])

df = df.drop_duplicates()

df.to_csv("data/processed/titanic_cleaned.csv", index=False)

print("Data preprocessing completed successfully.")