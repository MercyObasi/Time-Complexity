"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
nums = set()
for i in calls:                                                # O(n)
        if i[0][0]== "1" and i[0][1] == "4":
            k = i[0]
            nums.add(k)
        
answer = sorted(nums)                                         # O(nlogn)
print("These numbers could be telemarketers")
for u in answer:                                              # O(n)
    print(u)                                                  # O(n) + O(nlogn) + O(n) = O(nlogn) 
                                                    