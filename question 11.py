'''
*1.11 (Population projection) The US Census Bureau projects population based on the
following assumptions:
One birth every 7 seconds
One death every 13 seconds
One new immigrant every 45 seconds
Write a program to display the population for each of the next five years. Assume the
current population is 312032486 and one year has 365 days. Hint: in Python, you
can use integer division operator // to perform division. The result is an integer. For
example, 5 // 4 is 1 (not 1.25) and 10 // 4 is 2 (not 2.5)
'''

birth =7
death = 13
NI = 45
CP = 312032486
YIS = 365 * 24 * 60 * 60
BirthInOneYear = YIS // birth
DeathInOneYear = YIS // death
NIInOneYear = YIS // NI
print("The number of births in one year:", BirthInOneYear)
print("The number of deaths in one year:", DeathInOneYear)
print("The number of New Immigrant in one year:", NIInOneYear)
print("The population estimate for the next 5 years are as follows")
Year1 = CP + BirthInOneYear - DeathInOneYear + NIInOneYear
Year2 = CP + Year1 + (BirthInOneYear - DeathInOneYear + NIInOneYear)
Year3 = CP + Year2 + (BirthInOneYear - DeathInOneYear + NIInOneYear)
Year4 = CP + Year3 + (BirthInOneYear - DeathInOneYear + NIInOneYear)
Year5 = CP + Year4 + (BirthInOneYear - DeathInOneYear + NIInOneYear)

print("Year 1:", Year1)
print("Year 2:", Year2)
print("Year 3:", Year3)
print("Year 4:", Year4)
print("Year 5:", Year5)