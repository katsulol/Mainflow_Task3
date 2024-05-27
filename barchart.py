import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("householdtask3.csv")

def space():
    for i in range(20):
        print("\n")

def rep():
    a = input("Repeat??...(Y/N)")
    if a == "Y" or a == "y":
        space()
        num()
    elif a == "N" or a == "n":
        print("cya")
    else:
        space()
        print("Enter a valid response")
        num()

def num():
    a = int(input("Enter the number: "))

    if a == 1:
        categories = np.array(df["year"])
        values = np.array(df["income"])
        plt.bar(categories, values, color='lightgreen')
        plt.title('Income by Year')
        plt.xlabel('Year')
        plt.ylabel('Income')
        plt.xticks(rotation=45)
        plt.show()
        space()
        rep()

    elif a == 2:
        categories = np.array(df["year"])
        values = np.array(df["expenditure"])
        plt.bar(categories, values, color='lightblue')
        plt.title('Expenditure by Year')
        plt.xlabel('Year')
        plt.ylabel('Expenditure ($)')
        plt.xticks(rotation=45)
        plt.show()
        space()
        rep()

    elif a == 3:
        categories = np.array(df["year"])
        values = np.array(df["eqv_income"])
        plt.bar(categories, values, color='lightcoral')
        plt.title('Equivalized Income by Year')
        plt.xlabel('Year')
        plt.ylabel('Equivalized Income')
        plt.xticks(rotation=45)
        plt.show()
        space()
        rep()

    else:
        space()
        print("Enter a valid number")
        num()

def start2():
    print("The Bar charts available are: ")
    print("Enter the respective number to display the graph: ")
    print("Graphs available are: \nIncome by Year (1)\nExpenditure by Year (2)\nEquivalized Income by Year (3)")
    num()


start2()
