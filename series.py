import pandas as pd

a = pd.Series([10, 20, 30, 40, 50])
b = pd.Series([40, 50, 60, 70, 80])

#Not common in both
not_common = list(set(a) ^ set(b))
print("Not common in both:", not_common)

#Smallest and largest in series A
small=(a.min())
large=(a.max())
print("Smallest number in series A:",small)
print("largest number in series A:",large)

#Sum of series B
print(" Sum of series B:", b.sum())

#Average of series A
print(" Average of series A:", a.mean())

#Median of series B
print("Median of series B:", b.median())