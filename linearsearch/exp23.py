import pandas as pd
df=pd.read_excel("C:\Users\Student\Documents\\Exp23.xlsx")
print("standard deviation is =     ",df.loss.std())
print("mean is =  ",df.loss.mean())
print("variance is =  ",df.loss.var())
