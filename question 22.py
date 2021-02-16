
'''
22 (Population projection) Rewrite Exercise 1.11 to prompt the user to enter the
number of years and displays the population after that many years. Here is a
sample run of the program:
Enter the number of years:
The population in 5 years is 325932970
'''

birth =7
death = 13
NI = 45
CP = 312032486
YIS = 365 * 24 * 60 * 60
print(YIS)
BirthInOneYear = round(YIS/birth) #YIS // birth
DeathInOneYear = round(YIS/ death) #YIS // death
NIInOneYear = round(YIS /NI ) #YIS // NI
print(BirthInOneYear)
print(DeathInOneYear)
print(NIInOneYear)
print((BirthInOneYear - DeathInOneYear + NIInOneYear))

NoOfYears = eval(input("Enter the number of years:"))
for i in range(NoOfYears):
    CP = CP + (BirthInOneYear - DeathInOneYear + NIInOneYear)

print("THe population in ",NoOfYears, "years is ", CP )

