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
    a = int(input("Enter the graph number: "))

    if a == 1:
        plt.figure(figsize=(10, 6))
        plt.plot(df['year'], df['own_prop'], marker='o', linestyle='-')
        plt.title('Homeownership Rate Over Time')
        plt.xlabel('Year')
        plt.ylabel('Homeownership Rate (%)')
        plt.grid(True)
        plt.show()
        space()
        rep()

    elif a == 2:
        plt.figure(figsize=(10, 6))
        plt.plot(df['year'], df['income'], marker='o', linestyle='-')
        plt.title('Average Income Over Time')
        plt.xlabel('Year')
        plt.ylabel('Average Income')
        plt.grid(True)
        plt.show()
        space()
        rep()

    elif a == 3:
        plt.figure(figsize=(10, 6))
        plt.plot(df['year'], df['expenditure'], marker='o', linestyle='-')
        plt.title('Average Expenditure Over Time')
        plt.xlabel('Year')
        plt.ylabel('Average Expenditure')
        plt.grid(True)
        plt.show()
        space()
        rep()

    else:
        space()
        print("Enter a valid number")
        num()

def start3():
    print("The LineCharts available are: ")
    print("Enter the respective number to display the graph: ")
    print("Graphs available are: \nHomeownership Rates over time(1)\nAvg Income Over Time(2)\nAvg Expenditure Over Time(3)")
    num()

start3()