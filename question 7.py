'''
7 (Find the number of years and days) Write a program that prompts the user to
enter the minutes (e.g., 1 billion), and displays the number of years and days for
the minutes. For simplicity, assume a year has 365 days. Here is a sample run:
Enter the number of minutes:
1000000000 minutes is approximately 1902 years and 214 days
'''

Minutes = eval(input("Enter the number of minutes:"))
hours = Minutes / (60)
Tdays = hours / 24
Years = int(Tdays / 365)
Days = int(Tdays % 365)
print(Minutes," minutes is approximately ",Years,"years and ",Days,"days")

