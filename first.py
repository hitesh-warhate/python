# Write a program that takes principal, rate, and time from the user and calculates simple interest.

principal = float(input("EEnter the principal: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))

simple_interest = (principal * rate * time) / 100
print(f"The simple interest is: {simple_interest}")