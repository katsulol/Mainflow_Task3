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
        x = np.array(df["income"])
        y = np.array(df["expenditure"])
        plt.scatter(x,y)
        plt.title('Income vs Expenditure')
        plt.xlabel('Income')
        plt.ylabel('Expenditure')
        plt.grid(True)
        plt.show()
        space()
        rep()

    elif a == 2:
        x = np.array(df["age"])
        y = np.array(df["income"])
        plt.scatter(x,y)
        plt.title('Age vs Income')
        plt.xlabel('Age')
        plt.ylabel('Income')
        plt.grid(True)
        plt.show()
        space()
        rep()

    elif a == 3:
        x = np.array(df["age"])
        y = np.array(df["expenditure"])
        plt.scatter(x,y)
        plt.title('Age vs Expenditure')
        plt.xlabel('Age')
        plt.ylabel('Expenditure')
        plt.grid(True)
        plt.show()
        space()
        rep()

    else:
        space()
        print("Enter a valid number")
        num()

def start():
    print("The Scatter plots availale are: ")
    print("Enter the respective number to display the graph: ")
    print("Graphs available are: \nIncome Expenditure Graph(1)\nAge Income Graph(2)\nAge Expenditure Graph(3)")
    num()

start()
