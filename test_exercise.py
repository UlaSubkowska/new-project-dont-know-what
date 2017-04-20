#The program which ask user 10 questions
print('Hello, if you want to start the mountain test press enter :)')
input()
print('All of the following questions have 4 possibilities of answer, please enter only small letter which is related to your response.')
print('Also keep in mind that each time you want to go to next step, you have to press enter, like now :)')
input()

def question_about_mountains (question, reply, a, b, c, d, output):
    print(question)
    print(reply)
    answer=0
    while answer==False:
        answer=input('Type your answer:')
        if answer=="a":
            print(output[0])
            answer=a
            continue
        elif answer=="b":
            print(output[1])
            answer=b
            continue
        elif answer=="c":
            print(output[2])
            answer=c
            continue
        elif answer=="d":
            print(output[3])
            answer=d
            continue
        else:
            print('something went wrong, remember that you have to type only small letter related to answer you choosed')
            answer=False
            continue

for number_of_question in range (1,11):
    print('Question number', number_of_question)
    if number_of_question==1:
        question='Guess, which peak is the highest on the Earth:'
        reply='a - Mount Blanc \nb - Elbrus \nc - Mount Everest \nd - Aconcagua'
        a=False
        b=False
        c=True
        d=False
        output=['sorry, but you are wrong :P',"Elbrus is just 5 642 m high, it's still 3 206 m less then the highest mountain",
                'Yes, you are right Mount Everest is the highest mountain','unfortunatelly NO']
    elif number_of_question==2:
        question='Now we are sure that the highest mountain on the Earth is Everest, but do you know how high is it?'
        reply='a - 7 492 meters \nb - 8 848 meters \nc - 9 024 meters \nd - 8 611 meters'
        a=False
        b=True
        c=False
        d=False
        output=['NO this is elevation of Noshaq, which is the seconde highest independent peak of the Hindu Kush',
                'YES, you are right,what more the first official ascent of Everest was made by Norgay and Hillary in 1953',
                'are you stupid or something? :P','sorry but... NO, this is the elevation of K2 second hightest peak']
    elif number_of_question==3:
        question='What about mountains on another planets? Where is the highest mountain in our solar system?'
        reply='a - Earth \nb - Venus \nc - Jupiter \nd - Mars'
        a=False
        b=False
        c=False
        d=True
        output=['sorry, but you are wrong', 'NO the highest peak on Venus has ONLY 10 700 meters ;)',
                "NO Jupiter is a gas giant :P", "YES, the name of peak is Olympus Mons and it's above 22 000 meters high"]
    elif number_of_question==4:
        question="Let's come back to the Earth :) Do you know name of the highest unclimbed peak?"
        reply='a - Ganghar Puensum (Dzongkha) \nb - Mana \nc - Gyala Peri \nd - Nanda Devi'
        a=True
        b=False
        c=False
        d=False
        output=["YES - Dzongkha is the highest unclimbed mountain and it's located in Bhutan (elevation - 7 570 meters)",
                'NO - Mana was climbed in 1937 by F. Smythe, the peak is located in India',
                "NO - Gyala was ascented in 1986 by japanese expedition (peak located in China)",
                "NO - Devi was climbed in 1936, the peak is located in India"]
    elif number_of_question==5:
        question='How high is the volcano Mauna Kea, if measured from oceanic base?'
        reply='a - around 10 000 meters  \nb - less than 8 500 meters \nc - more than 20 000 meters\nd - around 15 000 meters'
        a=True
        b=False
        c=False
        d=False
        output=['YES - is located on the island of Hawaii, the elevation is 4 207 m, but measured from oceanic base is higher than Everest :)',
                'NO',"NO way :P", "sorry you are WRONG"]
    elif number_of_question==6:
        question='Where is located Aconcagua?'
        reply='a - India, \nb - Peru, \nc - Argentina, \nd - China'
        a=False
        b=False
        c=True
        d=False
        output=['NO', 'NO but you are close', 'YES - and it is the highest peak outside Asia','sorry but.... NO']
    elif number_of_question==7:
        question='How many eight-thousanders are still unclimed during winter?'
        reply='a - 15, \nb - 1, \nc - 9, \nd - 2'
        a=False
        b=True
        c=False
        d=False
        output=['are you stupid or something?', 'YES - only one', 'NO - definitely too much','you are WRONG']
    elif number_of_question==8:
        question='Which eight-thousander is unclimed during winter?'
        reply='a - Gaszerbrum II, \nb - Broad Peak, \nc - Nanga Parbat, \nd - K2'
        a=False
        b=False
        c=False
        d=True
        output=['no', 'no, no, no', 'NO','YES']
    elif number_of_question==9:
        question='Do you like my mountain test ?'
        reply='a - yes, \nb - it was boring as fuck, \nc - no, \nd - lame'
        a=True
        b=False
        c=False
        d=False
        output=['i am so happy that you like it :D', ':P - wrong answer, you can not finish test',
                ':P - wrong answer, you can not finish test',':P - wrong answer, you can not finish test']
    elif number_of_question==10:
        question='Who inspired us to learn Python? '
        reply='a - my mum, \nb - reality, \nc - Moniuni :D, \nd - Kasia'
        a=False
        b=False
        c=False
        d=True
        output=["no my mum doesn't know what is computer :P", 'it was not the main reason',
                'no','of course Kasia is the best ;)']
    question_about_mountains(question, reply, a, b, c, d, output)
    input()