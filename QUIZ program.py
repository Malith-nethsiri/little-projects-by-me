# QUIZ

questions = ["1. What is the capital of Japan?","2. Which gas do plants absorb from the atmosphere?","3. who wrote the play *Romeo and Juliet*?" ]
guess_answers = [["A. Seoul", "B. Beijing" ,"C. Tokyo" ,"D. Shanghai"],
                 ["A. Oxygen", "B. Nitrogen","C. Hydrogen","D. Carbon dioxide"],
                 ["A. Charles Dickens","B. Mark Twain","C. William Shakespeare","D. J.K. Rowling"]]
correct_answers = ["C","D","C",]
question_number=0
your_answers=[]
results = 0


for question in questions:
    print(question)

    for guess_answer in guess_answers[question_number]:
        print(guess_answer)

    your_answer = input("what is the correct answer(A, B, C, D)? ").upper()

    if your_answer == correct_answers[question_number]:
            results += 1
            print("yes your answer is correct")

    #elif your_answer != "A" or"B" or"C" or"D":
           # print("select from the given answers")

    else :
            print(f"your answer is wrong correct answer is {correct_answers[question_number]}")

    your_answers.append(your_answer)
    question_number+=1

    print("---------------------------------------")
    print()

print("***  your answers  ***")
for answers in your_answers :
    print(answers,end=" ")
print()

print("***  correct answers  ***")
for correct_answers_list in correct_answers :
    print(correct_answers_list, end=" ")

print()
print(f"your result is -> {(results/3)*100:.2f}%")