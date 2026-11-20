
print("===== PYTHON QUIZ GAME =====")

score = 0

questions = [
    {
        "question": "1. Which language are we learning?",
        "options": ["A. Java", "B. Python", "C. C++", "D. HTML"],
        "answer": "B"
    },
    {
        "question": "2. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. /*", "C. #", "D. --"],
        "answer": "C"
    },
    {
        "question": "3. Which function displays output?",
        "options": ["A. input()", "B. print()", "C. scan()", "D. display()"],
        "answer": "B"
    },
    {
        "question": "4. Which data type stores True or False?",
        "options": ["A. int", "B. str", "C. float", "D. bool"],
        "answer": "D"
    },
    {
        "question": "5. Which keyword is used to define a function?",
        "options": ["A. function", "B. def", "C. fun", "D. define"],
        "answer": "B"
    }
]

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    answer = input("Enter your answer: ").upper()

    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct answer:", q["answer"])

print("\n===== QUIZ RESULT =====")
print("Your score:", score, "/", len(questions))

if score == 5:
    print("Excellent!")
elif score >= 3:
    print("Good job!")
else:
    print("Keep practising!")
