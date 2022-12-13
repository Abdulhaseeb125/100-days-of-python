# this is a Tim_Urban age calculator that tells you
# how may days,weeks and months your have lived and you have left if your lived for 90 years
total_years = 90
days_in_a_year = 365
weeks_in_a_year = 52
months_in_a_year = 12
days_in_90_years = days_in_a_year * total_years
weeks_in_90_years = weeks_in_a_year * total_years
months_in_90_year = months_in_a_year * total_years
your_age = int(input("Enter your age:"))
days_left = days_in_90_years - your_age * days_in_a_year
months_left = months_in_90_year - your_age * months_in_a_year
weeks_left = weeks_in_90_years - your_age * weeks_in_a_year
print(f"According to Tim_Urban.You have {days_left} days , {weeks_left} weeks and {months_left} months remaining")
print(f"And your have lived for {your_age * days_in_a_year} days ,"
      f"{your_age * weeks_in_a_year} weeks and {your_age * months_in_a_year} months")

#.................The End..................
