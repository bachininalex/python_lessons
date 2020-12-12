#Calculation area of rectangle
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

