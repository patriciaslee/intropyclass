money = {'quarter':0,'dime':0,'nickel':0,'penny':0}

amount = input("Enter amount of bill (2 decimal digits only--e.g. 1.00 for $1, 0.25 for 25 cents, etc.): ")

dollar,cent = amount.split('.')
dollar = int(dollar)
cent = int(cent)

money['quarter'] = dollar * 4

while cent != 0:
	if cent >= 25:
		money['quarter'] += 1
		cent = cent - 25
		continue
	if cent >= 10:
		money['dime'] += 1
		cent = cent - 10
		continue
	if cent >= 5:
		money['nickel'] += 1
		cent = cent - 5
		continue
	if cent >= 1:
		money['penny'] += 1
		cent = cent - 1
		continue
print ('For the bill amount of $',amount,' you will need:')
print (money['quarter'],'quarter(s), ',money['dime'],'dime(s), ',money['nickel'],'nickel(s), and ',money['penny'],' penny/pennies.')
