###############################################################################
# DONE: 1. (3 pts)
#
#   Write a function called color_picker() that prints out a message to a user.
#
#   This function should do the following:
#     1. Prompt the user to enter the name of a color.
#     2. Using case statements, if it matches the color that they picked, it should print out a success message like so:
#           "Success! You picked red."
#        Do NOT use f-strings here. Just use regular strings and use the case statement to pick which string to print.
#     3. You should have a case for at least 5 colors of your choosing.
#     3. If the user picks a color that you do not have a case for, it should print:
#           "Unknown Color!"
#
#   Make sure you call your function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def color_picker():
    color_chosen = input("Type the color of your lightsaber: ")
    match color_chosen:
        case "red":
            print("The dark side is strong with one who chooses the " + color_chosen + " saber")
        case "blue":
            print("One is strong with the light if you selected the " + color_chosen + " saber")
        case "green":
            print("Wise you are in the ways of the good if you select the " + color_chosen + " saber")
        case "black":
            print("I guess you are a mandolorian if you want a " + color_chosen + " saber")
        case "orange":
            print("You are both strong and wise in the light, and are willing to protect it since you chosed the " + color_chosen + " saber")
        case _:
            print("Unknown Color")
color_picker()



###############################################################################
# DONE: 2. (3 pts)
#
#   Write a function called grade() that tells a student what letter grade they
#   got on an assignment based on the percentage they indicate.
#
#   This function should do the following:
#     1. Prompt the user to enter a percentage. They should enter the
#        percentage as a decimal (so an 85% should be entered as 0.85)
#     2. Using case statements, check which range the percentage is in and print a statement telling the user what grade they got on the assignment. It should look something like:
#           "You received a(n) A."
#     3. Your ranges should match a standard grading scale where greater than or equal to 90% is an A, etc.
#     4. If the user enters an invalid percentage, the function should print:
#           "Invalid Score!"
#
#   Make sure you call your function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def grade():
    grade_recived = float(input("Enter a percentage as a decimal: "))
    match grade_recived:
        case _ if 0.9 <= grade_recived < 1:
            print("You recieved an A")
        case _ if 0.8 <= grade_recived < 0.89:
            print("You received an B")
        case _ if 0.7 <= grade_recived < 0.79:
            print("You recieved an C")
        case _ if 0.6 <= grade_recived < 0.69:
            print("You received an D")
        case _ if 0 <= grade_recived < 0.59:
            print("You received an F")
        case _:
            print("Invalid Score!")
grade()