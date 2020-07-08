#!/usr/bin/env python3
"""Creates random bank of questions for proctored tests.

Usage:

    python3 EOC_Prep.py,
        or
    double click EOC_Prep.py

"""

import random

first_URE_file = r'C:\Users\alexc\Documents\Work\Training\3D1X1\Vol 1 URE.txt'
second_URE_file = r'C:\Users\alexc\Documents\Work\Training\3D1X1\Vol 2 URE.txt'
first_URE_answer_file = r'C:\Users\alexc\Documents\Work\Training\3D1X1\Vol 1 URE Answers.txt'
second_URE_answer_file = r'C:\Users\alexc\Documents\Work\Training\3D1X1\Vol 2 URE Answers.txt'

bank_of_questions = []
bank_of_answers = []
population = []


def GrabQuestions(filepath):
    """Grabs all of the questions and possible answers from text file. Puts them
        into a list.

     Args:
        filepath: The path to the text file. .txt file has to be in a specific format:
            ex:
                1. What is a question?
                a. a sentence
                b. a statement
                c. a poem
                d. what?

                2. What is a statement?
                a. a sentence
                b. a statement
                c. a poem
                d. what?

     Returns:
        A list of strings containing the questions and answers.
    """
    print('Grabbing questions...')

    # Counting all the lines for iteration purposes.
    f = open(filepath, 'r', encoding="utf8")
    number_of_lines = len(f.readlines())
    f.close()

    # Opening the file to read now
    f = open(filepath, 'r', encoding="utf8")
    x = 6
    question = []

    # Assuming questions have 4 answers, we have 5 lines
    #  Question
    #   Answer
    #   Answer
    #   Answer
    #   Answer
    #       blank_line
    # We loop through adding the entire question and its
    #   4 potential answers to the QUESTION list
    # 
    # On the blank line we append the QUESTION list to 
    #   the BANK_OF_QUESTIONS list.
    #
    # We do all of this until we have looped through it all
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
    """Grabs all of the answers and maps them to the questions order ( they should
        be in that order anyhow.)

        Function relies on the answers being in order, having a '.' to separate the answers
        and each answer on it's own line.

     Args:
        filepath: The path to the text file. .txt file has to be in a specific format:
            ex:
                1. a
                2. b
                3. c

     Returns:
        A list of strings containing the answers.
    """
    print('Grabbing answers...')

    # This assumes 100 questions and just goes line
    #   by line grabbing the string after the '.'
    #   and appending it to BANK_OF_ANSWERS
    f = open(filepath, 'r')
    for x in range(100):
        answer = f.readline().split('.')
        bank_of_answers.append(answer[1])
    f.close()


# Need to move to __MAIN__
GrabQuestions(first_URE_file)
GrabQuestions(second_URE_file)
GrabAnswers(first_URE_answer_file)
GrabAnswers(second_URE_answer_file)

# Need to put this in a function
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
