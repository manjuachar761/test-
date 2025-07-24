import pandas as pd
import matplotlib.pyplot as plt
import seaborn as s

df = pd.read_csv('Iris.csv')

#boxplot
s.boxplot(df['SepalLengthCm'],color='red')
plt.title("Boxplot of spies")
plt.xlabel(" Sepallength in cm")
plt.legend()
plt.show()

#scatter
species=df['species'].unique()
for sp in species:
    subset = df[df['species']==sp]
    plt.scatter(subset['PetalLengthCm'],subset['PetalWidthCm'],label=sp)
plt.title('petal length vs petal width')
plt.xlabel('petal length')
plt.ylabel('petal length')
plt.legend()
plt.show()

#bargraph
species_counts= df['species'].value_counts()
plt.bar(species_counts.index,species_counts.values,color='red')
plt.title('species vs count')
plt.xlabel('species')
plt.ylabel('count')
plt.show()

#piechart
species_counts=df['species'].value_counts()
plt.pie(species_counts.values, labels=species_counts.index)
plt.title("piechart for species_count")
plt.legend()
plt.show()