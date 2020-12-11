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
print(format(principalAmount, .2f))

