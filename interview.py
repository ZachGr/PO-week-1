def interview(questions, time):
    length = len(questions)
    i = 0
    result = "Qualify"
    notresult = ""
    req = [5,5,10,10,15,15,20,20]
    ranks = ["Very Easy","Very Easy","Easy","Easy", "Medium", "Medium", "Hard", "Hard"]

    if time > 120:
        notresult = "Disqualified: Exceeded the total time limit of the interview."
    elif length < 8:
        notresult = "Disqualified: Did not answer all questions"


    while i < length:
        if questions[i] > req[i]:
            notresult = "Disqualified: Exceeded the time limit for a "+ranks[i]+" question"
        i+=1
        
    if notresult == "":
        print(result)
    else:
        print(notresult)


interview([5, 5, 10, 10, 15, 15, 20, 20], 120)# ➞ "qualified"

interview([2, 3, 8, 6, 5, 12, 10, 18], 64)# ➞  "qualified"

interview([5, 5, 10, 10, 25, 15, 20, 20], 120)# ➞ "disqualified"

interview([5, 5, 10, 10, 15, 15, 20], 120)# ➞ "disqualified"

interview([5, 5, 10, 10, 15, 15, 20, 20], 130)# ➞ "disqualified"