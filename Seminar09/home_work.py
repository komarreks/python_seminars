import pandas

file = "california_housing_train.csv"

df = pandas.read_csv(file)

df_min_population = df.population.min()

max_households_in_min_population = df.loc[df.population == df_min_population].households.max()

print(max_households_in_min_population)