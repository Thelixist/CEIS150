# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 22:57:11 2021

@author: D99003734
"""
from datetime import datetime
from stock_class import Stock, DailyData
from account_class import  Traditional, Robo
import matplotlib.pyplot as plt
import csv


def add_stock(stock_list):
    option = ""
    while option != "0":
        print("Add a stock to the list")
        symbol = input("Symbol: ").upper()
        name = input("Stock name: ")
        shares = float(input("How many shares: "))
        new_stock = Stock(symbol, name, shares)
        stock_list.append(new_stock)
        option = input("Would you like to add another stock? or press 0 to stop: ")
	


# Remove stock and all daily data
def delete_stock(stock_list):
    found = False
    i = 0
    print("This method is under construction")
    print("What stock would you like to remove?: ")
    print("Stock List: [", end = ' ')
    for stock in stock_list:
        print(stock.symbol, end='')
        
    print(" ]", end='')
    userSymbol = input("Type the symbol of the stock to remove. : ").upper()
        
    for stock in stock_list:
        if stock.symbol == userSymbol:
            found = True
            stock_list.pop(i)
        i += 1
            
    if found == True:
        print("Deleted")
    else:
        print("Error, message for symbol not found")
        _ = input("Press Enter to Continue ***")
    
    
# List stocks being tracked
def list_stocks(stock_list):
    option = ""
    while option != "0":
        symbolLabel = "SYMBOL"
        nameLabel = "NAME"
        sharesLabel = "SHARES"
        print("Stock List ----")
        print(symbolLabel," " * (14-len(symbolLabel)),nameLabel," " * (14-len(nameLabel)),sharesLabel)
        print("======================================")
    #output column headings (include a border below the headings)
    
        for stock in stock_list:
            print(stock.symbol," " * (14-len(stock.symbol)),stock.name," " * (14-len(stock.name)),stock.shares)
        option = input("Would you like to continue? Enter 0 for no: ")
        
	#output stock.symbol, stock.name, stock.shares (format into columns aligned with headings)
#pause and prompt the user to press Enter to continue

    
    # Add Daily Stock Data
def add_stock_data(stock_list):
    symbolLabel = "SYMBOL"
    nameLabel = "NAME"
    sharesLabel = "SHARES"
    print("Stock List ----")
    print(symbolLabel," " * (14-len(symbolLabel)),nameLabel," " * (14-len(nameLabel)),sharesLabel)
    print("======================================")
    
    for stock in stock_list:
        print(stock.symbol," " * (14-len(stock.symbol)),stock.name," " * (14-len(stock.name)),stock.shares)

    choice = input("Which stock by symbol would you like to add?: ").upper()
    found = False
    current_stock = ''
    for stock in stock_list:
        if choice == stock.symbol:
            found = True
            current_stock = stock
        if found == True:
            data = input("Enter Date,Price,Volume: ")
            while data != "":
                date, price, volume = data.split(",")
                daily_data = DailyData(datetime.strptime(date,"%m/%d/%y"),float(price),float(volume))
                current_stock.add_data(daily_data)
                data = input("Enter Date,Price,Volume: ")
                print("Entry Complete")
            else:
                
                _=input("Press enter to continue.")
        else:
            print("Symbol not found!")
                
    
def investment_type(stock_list):
    print("Investment Account ---")
    balance = float(input("What is your initial balance: "))
    number = input("What is your account number: ")
    acct= input("Do you want a Traditional (t) or Robo (r) account: ")
    if acct.lower() == "r":
        years = float(input("How many years until retirement: "))
        robo_acct = Robo(balance, number, years)
        print("Your investment return is ",robo_acct.investment_return())
        print("\n\n")
    elif acct.lower() == "t":
        trad_acct = Traditional(balance, number)
        temp_list=[]
        print("Choose stocks from the list below: ")
        while True:
            print("Stock List: [",end="")
            for stock in stock_list:
                print(stock.symbol," ",end="")
            print("]")
            symbol = input("Which stock do you want to purchase, 0 to quit: ").upper()
            if symbol =="0":
                break
            shares = float(input("How many shares do you want to buy?: "))
            found = False
            for stock in stock_list:
              if stock.symbol == symbol:
                  found = True
                  current_stock = stock
            if found == True:
                current_stock.shares += shares 
                temp_list.append(current_stock)
                print("Bought ",shares,"of",symbol)
            else:
                print("Symbol Not Found ***")
        trad_acct.add_stock(temp_list)


# Function to create stock chart
def display_stock_chart(stock_list,symbol):
    print("This method is under construction")

# Display Chart
def display_chart(stock_list):
    print("This method is under construction")
  


                
 # Get price and volume history from Yahoo! Finance using CSV import.
def import_stock_csv(stock_list):
    print("This method is under construction")
    
   # Display Report 
def display_report(stock_list):
    print("This method is under construction")
    
def main_menu(stock_list):
    option = ""
    while True:
        print("Stock Analyzer ---")
        print("1 - Add Stock")
        print("2 - Delete Stock")
        print("3 - List stocks")
        print("4 - Add Daily Stock Data (Date, Price, Volume)")
        print("5 - Show Chart")
        print("6 - Investor Type")
        print("7 - Load Data")
        print("0 - Exit Program")
        option = input("Enter Menu Option: ")
        if option =="0":
            print("Goodbye")
            break
        
        if option == "1":
            add_stock(stock_list)
        elif option == "2":
            delete_stock(stock_list)
        elif option == "3":
            list_stocks(stock_list)
        elif option == "4":
           add_stock_data(stock_list) 
        elif option == "5":
            display_chart(stock_list)
        elif option == "6":
            investment_type(stock_list)
        elif option == "7":
            import_stock_csv(stock_list)
        else:
            
            print("Goodbye")

# Begin program
def main():
    stock_list = []
    main_menu(stock_list)

# Program Starts Here
if __name__ == "__main__":
    # execute only if run as a stand-alone script
    main()