import csv

def openfile(file_name):
    try:
        ls = []
        with open(file_name, newline="", encoding='utf-8') as dataFile:
            readCSV = csv.reader(dataFile)
            for row in readCSV:
                ls.append(row)
        return ls
    except FileNotFoundError:
        print("Cannot find file " + file_name)

filename = input("Enter filename containing csv data: ")
Name = openfile(filename)
print(Name[0][0])