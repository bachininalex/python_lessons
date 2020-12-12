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
