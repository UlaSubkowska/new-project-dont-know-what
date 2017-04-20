# The program which ask user 10 questions
print('Hello, if you want to start the mountain test press enter :)')
input()
print('All of the following questions have 4 possibilities of answer, please enter only small letter which is related to your response.')
print('Also keep in mind that each time you want to go to next step, you have to press enter, like now :)')
input()

#It takes the txt file and pull as a dictionaries in the list
file = open('questions.txt', 'r')
lines = file.readlines()
my_questions=[]
n=0

while n<len(lines):
    questions=lines[n:n+10]
    n+=10
    dictionary={}

    x = 1
    for item in questions:
        if questions[x][0] == '*':
            dictionary['answer'] = x
            break
        x += 1

    dictionary['quest']=questions[0][1:]
    dictionary['reply']=questions[1][1:]+questions[2][1:]+questions[3][1:]+questions[4][1:] #[i[1:] for i in questions[1:5]]
    dictionary['output']=questions[5:]
    my_questions.append(dictionary)

#definition
def question_about_mountains(quest, reply, answer, output):
    print(quest)
    print(reply)
    user_answer = None
    while True:
        answer_text = input('Type your answer:')
        if answer_text == "a":
            user_answer = 1
            print(output[0][1:])
        elif answer_text == "b":
            user_answer = 2
            print(output[1][1:])
        elif answer_text == "c":
            user_answer = 3
            print(output[2][1:])
        elif answer_text == "d":
            user_answer = 4
            print(output[3][1:])
        else:
            print('something went wrong, remember that you have to type only small letter related to answer you choosed')
            continue
        if answer == user_answer:
            break

#Main program:
for number_of_question,question in enumerate(my_questions):
    print('Question number', number_of_question+1)
    question_about_mountains(question['quest'], question['reply'], question['answer'], question['output'])
    input()




