# Program that show in rela time whith the year is a magic
print('Please enter date, mounth and year in dable format below')
day = int(input('You day:'))
mounth = int(input('You mounth:'))
	
if day >= 1 or day <= 31:
	if mounth >= 1 or mounth <= 12:
		year = int(input('Enter your year in double format(e. g. 70(means 1970):')
	else:
		print('Enter correct year(in double format(e. g. 80))')


else:
	print('Entered day or mounth are incorrect!')









