'''
5 (Financial application: calculate tips) Write a program that reads the subtotal and
the gratuity rate and computes the gratuity and total. For example, if the user
enters 10 for the subtotal and 15% for the gratuity rate, the program displays 1.5
as the gratuity and 11.5 as the total. Here is a sample run:

Enter the subtotal and a gratuity rate:
The gratuity is 2.35 and the total is 18.04
15.69, 15
'''

Subtotal, Gratuity = eval(input("Enter the subtotal and a gratuity rate:"))
EstimatedGratuity = (int((Gratuity / 100)*Subtotal * 100)) / 100
EstimatedTotal = (int(((Gratuity / 100)*Subtotal + Subtotal)*100))/100
print("The gratuity is",EstimatedGratuity,"and the total is",EstimatedTotal )