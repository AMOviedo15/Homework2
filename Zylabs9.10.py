#Aaron Oviedo #1990958

import csv

userfile = input()

wordNum = {}

with open(userfile, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        for word in row:
            if word not in wordNum.keys():
                wordNum[word] = 1
            else:
                wordNum[word] += 1

    for key in wordNum.keys():
        print(key + " " + str(wordNum[key]))