print("X---- WELCOME TO QUIZ ----X")
print("QUIZ RULES:-")
print("1. Every Question is compulsory, you don't have choice!\n 2. For each right answer you will rewarded with 10 points!\n 3. For each wrong answer you will be deducted by 5 points!\n 4. There will be 5 questions in the QUIZ")

print("Let's Start the Quiz....")
print("Give Answers in the form of a,b,c,d")

questions = [
    {
        "Question" : "Which country has the highest life expectancy?",
        "Options" : {"a":"India","b":"Hong Kong","c":"Italy","d":"USA"},
        "Answer" : "b"
    },

    {
        "Question" : "How many minutes are in a full week?",
        "Options" : {"a":10080,"b":11000,"c":9800,"d":8000},
        "Answer" : "a"
    },

    {
        "Question" : "What phone company produced the 3310?",
        "Options" : {"a":"Apple","b":"Samsung","c":"Nokia","d":"Realme"},
        "Answer" : "c"
    },

    {
        "Question" : "How many dots appear on a pair of dice?",
        "Options" : {"a":45,"b":46,"c":41,"d":42},
        "Answer" : "d"
    },
    
    {
        "Question" : "What is the 4th letter of the Greek alphabet?",
        "Options" : {"a":"Alpha","b":"Delta","c":"Gamma","d":"Epsilon"},
        "Answer" : "b"
    },

  


]
def run_quiz(questions):
    score = 0

    for i,k in enumerate(questions):
        print("\nQuestion",i+1,":",k['Question'])
        for option,text in k['Options'].items():
            print(option,":",text)

        while True:
            answer = input("Enter your answer(a/b/c/d): ")
            if answer in ['a','b','c','d']:
                break
            else:
                print("INVALID\n[Give Answer in a/b/c/d]")
            

        if answer == k['Answer']:
            print("Correct!\n+10")
            score = score+10
        else:
            print("Wrong!\n-5")
            score = score-5
    return score    

        
finalscore = run_quiz(questions)
print("Your final score is", finalscore,"/",len(questions)*10)