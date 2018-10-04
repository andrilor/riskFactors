import csv
import string
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
def punctuation_test(value):
    punct = list(string.punctuation)
    placeholder = ""
    if value[-1] == punct:
        placeholder = str(value[:-1])
        placeholder = float(placeholder[:-1])
    else:
        placeholder = value
    print(placeholder)
    print(value[:-1])
    return placeholder
def find_min(file_name, num):
    min_num = 99999999
    min_num_state = ""
    for i in file_name[2:]:
        placeholder1 = i[num]
        placeholder = punctuation_test(placeholder1)
        int1 = float(placeholder)
        str2 = i[0]
        if int1 < min_num:
            min_num = int1
            min_num_state = str2
    return min_num, min_num_state
def find_Max(file_name, num):
    max_num = 0
    max_num_state = ""
    for i in file_name[2:]:
        placeholder1 = i[num]
        int1 = float(placeholder1)
        str2 = i[0]
        if int1 > max_num:
            max_num = int1
            max_num_state = str2
    return max_num, max_num_state
filename = input("Enter filename containing csv data: ")
Name = openfile(filename)

num, state = find_min(Name, 11)
print(one)
print(two)
#one, two = find_Max(Name, 11)
#print(one)
#print(two)
#print(Name[0])
#print(Name[1][1])
#print(Name[1][5])
#print(Name[1][7])
#print(Name[1][11][:-1])
#print(Name[1][13][:-1])

#str1 = ''.join(str(i) for i in mylist)
#int1 = float(str1)

