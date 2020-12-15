# Program that displayes reflect to correspondes of Arabic numerals to Roman

print("Pease enter Arabic numeral the range of 1 and 10: ")
arabic_numerals = int(input())

roman = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']

if (arabic_numerals >= 1 and arabic_numerals <= 10):
	print("You entered", arabic_numerals, "Arabic numeral to Roman:", roman[arabic_numerals])

else:
	print("Please enter correct numeral")

