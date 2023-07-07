# A program to calculate scores into Alphabet grades

scre = input("Please enter score:")
score = float(scre)
if score>0:
    #print ("you have entered a positive score", score)
    if score<1:
        print ("You have entered a valid score", score, "equivalent to:")
        if score >= 0.9:
            print ("A")

        elif score >= 0.8:
            print ("B")
        elif score >= 0.7:
            print ("C")
        elif score >= 0.6:
            print ("D")
        elif score < 0.6:
            print ("F")
    else:
        print ("you have entered an invalid score of", score)
        quit()    

else:    
    print ("you have entered an invalid score of", score)
    quit()