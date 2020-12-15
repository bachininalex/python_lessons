#Simple code that Determine a person age

print("Please enter prefer age of person(between 0.1 and 120 years): ")
age = int(input())
print("You enter:", age)
if age < 1:
	print("Baby")
elif age > 1 and age < 13:
	print ("Child")
elif age > 13 and age < 20:
	print("Junior")
elif age > 20 and age < 120:
	print("Adult")
elif age < 0.09 or age > 121:
    print("You entered incorrect!")
