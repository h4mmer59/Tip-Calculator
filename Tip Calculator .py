# This is a simple program to calculate the tip of your meal
print "Welcome to Tip Calculator"
print "It's here that you'll be able to calculate the cost of your tip with only a couple of clicks"
cost_of_meal = input("Put the cost of your meal here!")
		
# I am still correcting on how to display the numbers in an orderly fashion that makes it good
tax_of_meal = input("Awesome! Now enter the tax!")
		
total_meal_cost_without_tip = cost_of_meal + tax_of_meal 
print "Your total meal cost (without tax) is:"
print total_meal_cost_without_tip
tip_percentage = input("Now put the percentage that you want to leave for a tip (Make sure to add a decimal before the number)")
tip = total_meal_cost_without_tip * tip_percentage
total_meal_cost = total_meal_cost_without_tip + tip
print "Your tip amount is:"
print tip
print "Your total meal cost is:"
print total_meal_cost