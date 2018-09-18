# Month: june
# Day: 17
# National holiday

# January 1 => New year's day
# June 17 => National holiday
# December 25 => Christmas day
 
# Write a program that prompts for the name of a month and a day number. You can assume that the month name is entered using lowercase letters. Using this input, you need to construct a string which contains the name of the month,
# with the first letter as uppercase, followed by the day number, with one space in between.
 
# If the resulting string is a holiday then the program prints the associated name according to the table above.
# If the resulting string is not a holiday then the program prints "Not a holiday".
# The input/output of the program should be exactly the same as shown in the example below.
# Hint: Use the capitalize() function.


month = input("Month: ")
day = input("Day: ")

new_year = "New year's day"
national = "National holiday"
christmas = "Christmas day"

if month == "january" and day == "1":
    print("{}{} {} => {}".format(month[0].upper(),month[1:], day, new_year))
elif month == "june" and day == "17":
    print("{}{} {} => {}".format(month[0].upper(),month[1:], day, national))
elif month == "december" and day == "25":
    print("{}{} {} => {}".format(month[0].upper(),month[1:], day, christmas))
else:
    print("Not a holiday")



    

#  = input("Input a grade: ")) # Do not change this line

# if grade < 0 or grade > 10:
#     print("Invalid grade!") # Do not change this line
# elif grade >= 5 or grade == 10:
#     print("Passing grade!") # Do not change this line
# else:
#     print("Failing grade!") # Do not change this line