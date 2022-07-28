"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import code
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def find_Bangalore_nums(list):
  recipient = set()
  for i in calls:
    if i[0][1] == "0" and i[0][2] == "8" and i[0][3] == "0":
      called_nums  = i[1]
      recipient.add(called_nums)

  return recipient

recipient_numbers = (find_Bangalore_nums(calls))

def codes_Bangalore_nums(list):
  codes = set()

  for j in list:
    if j[0] == "(" and j[4] == ")":
      cod = ""
      z = 1
      while z <= 3:
        cod += j[z]
        z +=1
      codes.add(cod)
  
    elif j[0] == "(" and j[6] == ")":
      code = ""
      z = 1
      while z <= 5:
        code += j[z]
        z += 1
      codes.add(code)
  
    elif j[0] == "7" or j[0] == "8" or j[0] == "9":
      codz = ""
      z = 0
      while z <= 5:
        codz += j[z]
        z += 1
      codes.add(codz)

  return codes

ans = codes_Bangalore_nums(recipient_numbers)
print("The numbers called by people Bangalore have codes")
for k in sorted(ans):
  print(k)


# percent_Bangalore_nums
 
  count_caller = 0
for i in calls:
  if i[0][1] == "0" and i[0][2] == "8" and i[0][3] == "0":
    if i[1][1] == "0" and i[1][2] == "8" and i[1][3] == "0":
      count_caller += 1

#percentage
callers = float (count_caller / 100)


print("%.2F" %callers,"percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
