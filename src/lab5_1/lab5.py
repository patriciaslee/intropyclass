#===================================================================================#
#
# lab5.py
#
#===================================================================================#

import sys      # access to variables used or maintained by the interpreter
import datetime # date
import time     # time

# Input the bill as a float/integer and ask again if an error
while True:
    try:
        billFloat = float(input('\nEnter amount of bill (2 decimal digits only--\
e.g. 1.00 for $1, 0.25 for 25 cents, etc.):  $ '))
        break
    except ValueError:
        print('Try again!',sys.exc_info()[0],' Please enter a digit from 1-10, not as \
the word that represents that number.')
    except:
        print('Unknown Error: ',sys.exc_info()[0])
        raise

# Define currency with 2 decimal places 
currency = round(billFloat,2)

# coinTypes in a Tuple (immutable) (Quarter, Dime, Nickel, Penny)
coinTypes = (0.25,0.10,0.05,0.01)
# coinList collects number of each coin in a List(mutable)
coinList = []

# Loop until number of coins are determined, starting from the largest ($0.25) to
# the smallest ($0.01) denomination
for coin in coinTypes:
    coinNumber = round(int(currency/coin),2)    # Quotient of currency and coin
    currency = round(currency%coin,2)           # Remainder of currency/coins
    coinList.append(str(coinNumber))            # Append coin numbers to the coin list

# Output strings
string1 = 'For the bill amount of $' + str(round(billFloat,2)) + ', you will need:'
string2 = "%s quarter(s), %s dime(s), %s nickel(s), %s penny/pennies" % tuple(coinList)

date_time = datetime.datetime.now()

# Print output strings to monitor
print('\n' + str(date_time))
print(string1)
print(string2)


# Write the output strings to file 'statement.txt'.  Append all results.
while True:
    try:
        f = open('statement.txt', 'a')
        break
    except IOError:
        print('Cannot open statement.txt')
    except:
        print('Unknown Error: ', sys.exc_info()[0])

f.write('\n' + str(date_time) + '\n')
f.write(string1 + '\n')
f.write(string2 + '\n')

f.close()
