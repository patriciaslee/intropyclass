while (1==1):
    try:
        in_txt = input('Enter amount of bill (2 decimal digits only--e.g. 1.00 for $1, 0.25 for 25 cents, etc.):')
        value=[]
        value=in_txt.split('.')
        print (len(value))
        A=int(value[0])
        B=int(value[1])
        if len(value[1]) == 2:
            count = {}
            count['quarter'] = int(value[0])*4 + int(value[1])//25
            value[1] = int(value[1])%25
            count['dime'] = value[1]//10
            value[1] = value[1]%10
            count['nickel'] = value[1]//5
            count['cent'] = value[1]%5
            break
    except ValueError:
        print('Try again! Value error. Please enter a digit from 1-10, not as the word that represents that number.')
    except IOError:
        print('Try again! I/O error.')
    except:
        print('Try again! Other error.')
print('For the bill amount of $',in_txt,', you will need:')
print(count['quarter'],'quarter(s), ',count['dime'],'dime(s), ',count['nickel'],'nickel(s), and ',count['cent'],'penny/pennies.')
