# -*- coding: utf-8 -*-
#Main menu
chapter = 0

#Constants for amount of cookies
COOKIES_RECIPE = 48.0
SUGAR_RECIPE = 1.5
BUTTER_RECIPE = 1.0
FLOUR_RECIPE = 2.75


def main():
	print('Hello, please select prefer block to execute')
	print('A list of all chapter see below:\n')
	print('1. Car distance')
	print('2. Make a cookies')
	print('3. Show age of people')
	print('4. Amount to personal acoount')
	print('5. Conver Arab to Roman')
	print('6. Calculation area of rectangle')
	print('7. Convert Celsius to Fahrenheit')
	print('8. Displays day of the week that correspond entered number ')
	print('9. Calculate sum of some items')
	print('10. Show in real time whith the date is a magic \n')


	print('If you wand drawing turtle, please enter "turtle"\n')


	chapter = int(input('Enter number of chapter:'))

	if chapter == 1:
		show_x()
	elif chapter == 2:
		car_distance()
	elif chapter == 3:
		cookies()


def show_x():
	print(' go            go');
	print('  go         go'  );
	print('   go       go'  );
	print('    go    go'  );
	print('      gogo'  );
	print('     go   go          ');
	print('    go     go'  );
	print('   go       go'  );
	print('  go         go'  );
	print('      '             );

def car_distance():
	speed_car = 70
	time = 40
	distance = 100
	time=int(input("Enter time for traveling: \n"))
	speed=int(input("Enter speed for traveling: \n"))
	distance = speed * time
	print("For ",time, "time, car will travel distance:", distance)

def cookies():
	#Part of program from answers to homework
	cookies = 0.0
	sugar = 0.0
	butter = 0.0
	flour = 0.0
	#Get amount of cookies
	cookies = float(input("Введите количество булочек: "))

	#Calculate how to need glases of sugar to make cookies
	sugar = (cookies * SUGAR_RECIPE) / COOKIES_RECIPE

	#Calculate how to need glases of butter to make cookies
	butter = (cookies * BUTTER_RECIPE) / COOKIES_RECIPE

	# Calculate how to need flour to make cookies
	flour = (cookies * FLOUR_RECIPE) / COOKIES_RECIPE


	print ("Чтобы изготовить", cookies, "булочек, вам понадобятся:")
	print (format(sugar, '.2f'), "стаканов сахара")
	print (format(butter, '.2f'), "стаканов масла")
	print (format(flour, '.2f'), "стаканов муки")

#Simple function code that Determine a person age.
def age_of_people():
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

#Function that execute calculate Amount for account
def amountofaccount():
	print("Enter principal amount on accont:")
	principal = float(input())

	print("Enter annual interest rate")
	rate = float(input())
	InterestRate = rate / 100


	print("Enter frequency of accrual of interest income per year:")
	frequency = float(input())

	print("Number of year: ")
	NumberOfYear = float(input())
	degree = frequency * NumberOfYear

	principalAmount = principal * (1 + InterestRate / frequency)**degree

	print("Final amount on account")
	print(format(principalAmount, '.2f'))

# Function that displayes reflect to correspondes of Arabic numerals to Roman
def arab_to_roman():
	print("Pease enter Arabic numeral the range of 1 and 10: ")
	arabic_numerals = int(input())

	roman = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']

	if (arabic_numerals >= 1 and arabic_numerals <= 10):
		print("You entered", arabic_numerals, "Arabic numeral to Roman:", roman[arabic_numerals])

	else:
		print("Please enter correct numeral")

#Calculation area of rectangle
def area_of_rectangle():
	print("Please enter lenght and width of first rectangle: ")
	lenght1 = float(input("lenght:"))
	width1 = float(input("width:"))
	area_first = lenght1 * width1

	print("Please enter lenght and width of second rectangle: ")

	lenght2 = float(input("lenght:"))
	width2 = float(input("width:"))

	area_second = lenght2 * width2

	if area_first > area_second :
		print("Area of first rectangle is bigger:", area_first)
	elif area_first == area_second:
		print("Area of both rectangle is equal")
	else:
		print("Area of second rectangle is bigger" , area_second)


#Conver celsium to farengate:
def c_to_f():
	Celsium = float(input("Enter temperature in Censium: \n"))
	result = (Celsium * 9 / 5) + 32
	print("Converted temperature to Farengate equal is :", result)

#Displays day of the week that correspond entered number.
def day_of_week():
	day = int(input("Enter number between 1 to 7 \n"))

	my_list = [" ","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]


	if (day >= 1 and day <=7):
		print("You enter correct number", "Correspond day is: ", my_list[day])
	 
	else:
		print("Please enter number between 1 and 7")

#Sum all items, tases and how to pay.
def items():
	item1 = int(input("Enter sum of 1st item  \n"))
	item2 = int(input('Enter sum of 2st item \n'))
	item3 = int(input('Enter sum of 3st item \n'))
	item4 = int(input('Enter sum of 4st item \n'))
	item5 = int(input('Enter sum of 5st item \n'))


	all_item = item1 + item2 + item3 + item4 + item5

	result = all_item

	tax = result * 0.07

	sumtopay = result + tax

	print('Sum all items equal:', result)
	print('Sum tax for all items :', tax)
	print('You finish sum is:', sumtopay)

#Function that show in rela time whith the year is a magic
def magic_date():
	print('Please enter date, mounth and year in dable format below')
	day = int(input('You day:'))
	mounth = int(input('You mounth:'))
		#if day >= 1 or day <= 31:
			#elif mounth >= 1:
				#year = int(input('Enter your year in double format(e. g. 70(means 1970):')
			#elif mounth <= 12:
				#ear = int(input('Enter your year in double format(e. g. 70(means 1970):')
			#else:
				#print('Enter correct year(in double format(e. g. 80))')
		#else:
			#print('Entered day or mounth are incorrect!')

#Draving turtle
def draving_turtle():
	import turtle

	turtle.speed(7)
	turtle.setup(640, 480)
	turtle.penup()
	turtle.goto(0, -50)
	turtle.pendown()

	print('It is draving the cube in circle')

	turtle.pencolor('blue')
	turtle.bgcolor('yellow')

	turtle.pensize(5)
	turtle.circle(120)

	turtle.penup()
	turtle.goto(0, -15)
	turtle.pendown()

	turtle.forward(50)
	turtle.left(45)
	turtle.forward(25)

	turtle.penup()
	turtle.forward(25)
	turtle.pendown()

	turtle.left(45)
	turtle.forward(50)

	turtle.forward(50)
	turtle.left(45)
	turtle.forward(50)
	turtle.left(45)
	turtle.forward(50)

	turtle.forward(50)
	turtle.left(45)
	turtle.forward(50)
	turtle.left(45)
	turtle.forward(50)

	turtle.forward(50)
	turtle.left(45)
	turtle.forward(50)
	turtle.left(45)
	turtle.forward(50)

	turtle.pos()

	turtle.hideturtle()

	turtle.done()  		


main()



