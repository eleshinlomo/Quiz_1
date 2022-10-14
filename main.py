score = 0

question_1 = input("Which continent does Nigeria belong to? ")
if question_1 == "Africa":
    score += 10
    print("Bravo! You scored " + str(score) + " Keep pushing. You smart!")
else:
    print("Wrong Answer! We know you are smart, just a lil hangover from last night")
question_2 = input("What is the Firstname of the last president of America? ")
if question_2 == "Trump":
    score += 10
    print("Bravo! You scored " + str(score) + " Keep pushing. You smart!")
else:
    print("How could you have missed the first name of last US President?")
    print( "Your total score is " + str(score) + ".")
if score >= 20:
        print("Bravo! You are one of the smartest folks on earth.")
else:
    print("Ooops! You need need to put up some work buddy!")

print("*** QUIZ HAS ENDED. YOUR TOTAL SCORE IS {}. THANK YOU FOR YOUR TIME!".format(score))

