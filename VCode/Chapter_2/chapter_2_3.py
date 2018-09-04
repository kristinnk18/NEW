# Take the number of points one team is ahead
# Subtract three
# Add ½ point if team that is ahead has the ball, subtract ½ point otherwise
# Square the result
# If the result is greater than the number of seconds left, the lead is safe

# Take the number og points one team is ahead.

points_str = input ("Enter the lead in points: ")
Points_remaining_int = int(points_str)

#Subtract three.

lead_calculation_float = float(Points_remaining_int - 3)

# Add ½ point if team that is ahead has the ball, subtract ½ point otherwise

has_ball_str = input ("Does the lead team have the ball (Yes or No): ")

has_ball_str = "Yes"

if has_ball_str == "Yes":
    lead_calculation_float = lead_calculation_float + 0.5
else:
    lead_calculation_float = lead_calculation_float - 0.5

# Numbers less than zero become zero

if lead_calculation_float < 0:
    lead_calculation_float = 0

# Square that

lead_calculation_float = lead_calculation_float**2

# If the resault is greate than the number og seconds left in game, the lead is safe.

seconds_reamainin_int = int(input("enter the number of seconds rmaining: "))


if lead_calculation_float > seconds_reamainin_int:
    print("lead is safe")

else:
    print("lead is not safe")

    