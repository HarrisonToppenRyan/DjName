# Author :  Harrison Toppen-Ryan
# Description :  DJ name, HW5, CSCI 141
# Date :  November 21st, 2020

#generate name function for inputing names and making it into a list
def generateDJNames():
    name = input("What is your first and last name? ")
    #creatiing a list from first and last name 
    nameList = name.split()
    #calling the isInputValid function 
    isInputValid(name, nameList)
#taking in the name and namelist info 
def isInputValid(name, nameList):
    #if there us a space in the name 
    if ' ' in name:
        #if the name is too short 
        if len(nameList[0]) < 5:
            print("Name is not long enough.")
        #if the first name contains an odd number of characters 
        elif len(nameList[0]) % 2 != 0:
            print("Your DJ name is: ", nameList[0][0:len(nameList[0])//2], nameList[1][len(nameList[0])//2:],"Sizzle", sep="")
        else:
            print("Your DJ name is: ", nameList[0][0:len(nameList[0])//2], nameList[1][len(nameList[0])//2:],"Sizzle", sep="")
    else:
        #if there not a space in the name 
        while ' ' not in name:
            print("Incorrect input. A single space is required")
            print("please try again")
            #calling the generate names function 
            generateDJNames()

def main():
    generateDJNames()
    
main()


