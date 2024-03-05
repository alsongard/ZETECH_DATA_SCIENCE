import pandas as pd
df = pd.DataFrame(
    {
        "A": [10, 20, 30],
        "B": [30, 40, 50],
        "C" : [50, 60, 70]
    }
)
print(df)

df["row_average"] = df.loc[:, ["B","C"]].mean(axis=1)

print(df)




