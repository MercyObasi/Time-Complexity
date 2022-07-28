"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from subprocess import call
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def count_phone_num(texts, calls):
    counter = 0
    count = 0
    count1 = 0
    for i in texts:
        for j in i[:2]:
            count +=1

    for h in calls:
        for k in h[:2]:
            count1 +=1        

    counter = count + count1
    return counter

print("There are",count_phone_num(texts,calls),"different telephone numbers in the records.")
