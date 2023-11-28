import pandas

file = "california_housing_train.csv"

df = pandas.read_csv(file)

# Показать median_house_value где median_income < 2
# print(df.loc[df.median_income < 2, ['median_income', 'median_house_value']])
# # 3. Показать данные в первых 2 столбцах
# print(df.iloc[:, 0:2])


# Выбрать данные где housing_median_age < 20 и
# median_house_value > 70000

#            условия                       выводимые столбцы
# print(df.loc[(df.housing_median_age < 20) & (df.median_house_value > 70000), ['housing_median_age', 'median_house_value']])

# Задача №61. Решение в группах
# 1. Определить какое максимальное и минимальное значение median_house_value

# print(df.median_house_value.max())
# print(df.median_house_value.min())
# print(df.median_house_value.mean()) # среднее
# print(df.median_house_value.median()) # медианное

# 2. Показать максимальное median_house_value, где median_income = 3.1250

# print(df.loc[df.median_income == 3.1250, ['median_house_value']].max())

# 3. Узнать какая максимальная population в зоне минимального значения median_house_value

min = df.median_house_value.min()

df2 = df.loc[df.median_house_value == min, ['median_house_value', 'population']]

print(df2.population.max())