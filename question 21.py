'''21 (Financial application: compound value) Suppose you save $100 each month into
a savings account with an annual interest rate of 5%. Therefore, the monthly interest
rate is 0.05/12 = 0.00417 After the first month, the value in the account
becomes
100 * (1 + 0.00417) = 100.417
After the second month, the value in the account becomes
(100 + 100.417) * (1 + 0.00417) = 201.252
After the third month, the value in the account becomes
(100 + 201.252) * (1 + 0.00417) = 302.507
and so on.
Write a program that prompts the user to enter a monthly saving amount and
displays the account value after the sixth month. Here is a sample run of the
program:

Enter the monthly saving amount:
After the sixth month, the account value is 608.81
'''

MonthlySavingAmt = eval(input("Enter the monthly saving amount:"))
AIR = 5
MIR = (AIR / 100) / 12
FM = 100 * (1 + MIR)
SM = (100 + FM) * (1 + MIR)
TM = (100 + SM) * (1 + MIR)
FOM = (100 + TM) * (1 + MIR)
FIM = (100 + FOM) * (1 + MIR)
SIM = (100 + FIM) * (1 + MIR)
SIM = int(SIM * 100) / 100
print("After the sixth month, the account value is ",SIM)
