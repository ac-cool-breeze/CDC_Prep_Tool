import random

first_URE_file = r'C:\Users\alexc\Documents\Work\Training\3D1X1\Vol 1 URE.txt'
second_URE_file = r'C:\Users\alexc\Documents\Work\Training\3D1X1\Vol 2 URE.txt'
first_URE_answer_file = r'C:\Users\alexc\Documents\Work\Training\3D1X1\Vol 1 URE Answers.txt'
second_URE_answer_file = r'C:\Users\alexc\Documents\Work\Training\3D1X1\Vol 2 URE Answers.txt'

bank_of_questions = []
bank_of_answers = []
population = []


def GrabQuestions(filepath):
    f = open(filepath, 'r', encoding="utf8")
    number_of_lines = len(f.readlines())
    f.close()

    f = open(filepath, 'r', encoding="utf8")
    x = 6
    question = []

    while number_of_lines > 0:
        while x >= 0:
            if x == 5:
                question.append(f.readline())
                number_of_lines = number_of_lines - 1
                x = x - 1

            elif x == 0:
                bank_of_questions.append(question.copy())
                question.clear()
                x = x - 1

            else:
                question.append(f.readline())
                number_of_lines = number_of_lines - 1
                x = x - 1
        x = 6
    
    f.close()


def GrabAnswers(filepath):
    print('Grabbing answers...')
    f = open(filepath, 'r')
    for x in range(100):
        answer = f.readline().split('.')
        bank_of_answers.append(answer[1])
    f.close()


GrabQuestions(first_URE_file)
GrabQuestions(second_URE_file)
GrabAnswers(first_URE_answer_file)
GrabAnswers(second_URE_answer_file)

sampled_op = random.sample(range(200), 100)
f = open('Practice_Test_Answers.txt', 'a')
print('sampled_op: ' + str(sampled_op))
for x in sampled_op:
    print(bank_of_questions[x-1])
    print(bank_of_answers[x-1])
    for y in bank_of_questions[x-1]:
        f.write(str(y))
    new_line = 'Answer: ' + str(bank_of_answers[x-1]) + '\n'
    f.write(new_line)
f.close()

counter = 1
f = open('Practice_Test.txt', 'a')
for x in sampled_op:
    no = 5
    while no >= 0:
        for a_question in bank_of_questions[x-1]:
            if no == 5:
                no = no - 1
                z = a_question.split('.')
                new_line = str(counter) + ('.') + str(z[1])
                f.write(new_line)
                counter = counter + 1
            else:
                no = no - 1
                f.write(a_question)

f.close()