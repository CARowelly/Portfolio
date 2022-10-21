# PythonCode.py
# 7 - 1 Project 3: Corner Grocer App
# SNHU CS - 210
# 2022/04/15
# Craig Rowell

import re
import string
import os.path 
from os import path


# call this function by passing into CallProcedure
# ex. callProcedure("CountAllItems") which returns a list of each type of item and prints all items

def CountAllItems():
        # opens input file in read mode
        text = open("CS210_Project_Three_Input_File.txt", "r")

        # an empty dictionary to store item names
        dictionary = dict()

        # input formatting
        for line in text:
            # removes spaces and newlines
            line = line.strip()

            # set all characters to lowercase
            item = line.lower()

            # checks for multiples of same word
            if item in dictionary:
                # increment number of duplicate items
                dictionary[item] = dictionary[item] + 1
            else:
                # add item to dictionary with a value of 1
                dictionary[item] = 1

        # print all items in dictionary
        for key in list (dictionary.keys()):
            print(key.capitalize(), ":", dictionary[key])
        
        # close input file
        text.close()


# Call this function by passing it into CallIntFunc along with user input
# callIntFunc("CountInstances", userInput); returns the number of instances of the user input
# returns int wordCount

def CountInstances(userInput):

    # converts userInput to lower case
    userInput = userInput.lower()

    # opens input file in read mode
    text = open("CS210_Project_Three_Input_File.txt", "r")

    # var to track number of matches
    matches= 0

    # input formatting
    for line in text:
        # removes spaces and newlines
        line = line.strip()

        # set all characters to lowercase
        item = line.lower()

        # checks if item is equatable to userInput
        if item == userInput:
            # increment number of matches
            matches += 1
    
    # returns number of matches
    return matches
    # close input file
    text.close()


# count the number of each type of item, then write to frequency.dat
# call this function by passing it into the CallProcedure
# returns the document frequency.dat with each individual item and the number of times that item occurs

def RecordData():
    # opens the input file in read mode
    text = open("CS210_Project_Three_Input_File.txt", "r")

    # creates and writes frequency.dat
    frequency = open("frequency.dat", "w")

    # creates an empty dictionary to store items
    dictionary = dict()

    # input formatting
    for line in text:
        # removes spaces and newlines
        line = line.strip()

        # set all characters to lowercase
        item = line.lower()

        # checks if item is already in dictionary
        if item in dictionary:
            # increments the number of like items
            dictionary[item] = dictionary[item] + 1
        else:
            # adds new item to dictionary with a value of 1
            dictionary[item] = 1

    # writes each key and value pair to frequency.dat
    for key in list (dictionary.keys()):
        # formats key and value pairs as strings ending on a new line
        frequency.write(str(key.capitalize()) + " " + str(dictionary[key]) + "\n")

    # closes the opened files
    text.close()
    frequency.close()
        