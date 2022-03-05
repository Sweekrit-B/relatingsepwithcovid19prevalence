import numpy as np
import pandas as pd
from scipy import stats
from scipy import optimize
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

#California Vaccination Relations
data_list = []
data = pd.read_excel("1_vaccinationratiodata_CA.xlsx")
x1 = list(data['population_to_GDP'])
data_list.append(x1)
x2 = list(data['population_to_ntav'])
data_list.append(x2)
x3 = list(data['population_to_propertytax'])
data_list.append(x3)
x4 = list(data['population_to_rfs'])
data_list.append(x4)
x5 = list(data['population_to_wages'])
data_list.append(x5)
y = list(data['population_to_doses'])

print("California Correlation Values (high GDP representation, rank 1)")
for element in data_list:
    r, p = 0, 0
    r, p = stats.pearsonr(element, y)
    print("Column " + str(data_list.index(element)) + " to dose correlation: " + str(round(r, 10)) + ". " + "Column " + str(data_list.index(element)) + " to dose p-value: " + str(round(p, 20)))
    plt.scatter(element, y, s=100, edgecolors="black")
    plt.title("Column " + str(data_list.index(element)) + " ratio vs. population-dose ratio (California)")
    plt.show()

#Oregon Vaccination Relations
print()
print("Oregon Correlation Values (mid GDP representation, rank 25)")

data1 = pd.read_excel("1_vaccinationratiodata_OR.xlsx")
a = list(data1['population_to_GDP'])
b = list(data1['population_to_doses'])
r1, p1 = 0, 0
r1, p1 = stats.pearsonr(a, b)
print("population-GDP ratio to population-dose ratio correlation: " + str(round(r1, 10)) + ". GDP to dose p-value: " + str(round(p1, 20)))
plt.scatter(a, b, s=100, edgecolors="black")
plt.title("population-GDP ratio vs. population-dose ratio (Oregon)")
plt.show

#Vermont Vaccination Relations
print()
print("Vermont Correlation Values (low GDP representation, rank 51)")

data2 = pd.read_excel("1_vaccinationratiodata_VT.xlsx")
m = list(data2['population_to_GDP'])
n = list(data2['population_to_doses'])
r2, p2 = 0, 0
r2, p2 = stats.pearsonr(m, n)
print("population-GDP ratio to population-dose ratio correlation: " + str(round(r2, 10)) + ". GDP to dose p-value: " + str(round(p2, 20)))
plt.scatter(m, n, s=100, edgecolors="black")
plt.title("population-GDP ratio vs. population-dose ratio (Vermont)")
plt.show

'''r, p = stats.pearsonr(x, y)
print(round(r, 4))
print(round(p, 7))'''

'''def linear(x, a, b):
    return a*x**2 + b*x

constants = curve_fit(linear, x, y)
a_fit = constants[0][0]
b_fit = constants[0][1]

fit = []
for i in x:
    fit.append(linear(i, a_fit, b_fit))

print(a_fit, b_fit)'''
'''
plt.figure(figsize=(10, 10))
plt.scatter(x, y, s=100, edgecolors="black")
#plt.scatter(x, fit)
plt.title("Population-GDP ratio vs. Population-dose ratio")
plt.show()
'''