Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def percentages():
	males = float(input("Enter number of males:"))
	females = float(input("Enter number females:"))
	total = males + females
	male_decimal = males/total
	male_percent = male_decimal*100
	female_decimal = females/total
	female_percent = female_decimal*100
	print("Percent of males: "+str(int(male_percent))+"%")
	print("Percent of females: "+str(int(female_percent))+"%")

	
>>> percentages()
Enter number of males:75
Enter number females:25
Percent of males: 75%
Percent of females: 25%
>>> 