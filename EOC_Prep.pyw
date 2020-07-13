#!/usr/bin/env python3
"""Creates random bank of questions for proctored tests.

Usage:

    python3 EOC_Prep.py,
        or
    double click EOC_Prep.py

"""

import random
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

first_URE_file = ''
second_URE_file = ''
first_URE_answer_file = ''
second_URE_answer_file = ''

bank_of_questions = []
bank_of_answers = []
population = []


def beginButtonClicked():
    """Reacts to button being clicked, draws next window

    """
    first_URE_file = ''
    second_URE_file = ''
    first_URE_answer_file = ''
    second_URE_answer_file = ''
    initialdir_var = '/'
    save_directory ='/'

    title_label.destroy()
    tool_label.destroy()
    begin_button.destroy()

    window.title('CDC Prep Tool - Run Screen')

    select_ures_text = Message(window,
        anchor="w",
        text="Step 1. Select UREs to build banks of questions.",
        fg="blue", 
        font=("Courier", 12))

    select_answers_text = Message(window,
        anchor="w",
        text="Step 2. Select answers to build banks of answers.",
        fg="blue", 
        font=("Courier", 12))

    '''
    select_no_questions_text = Message(window,
        anchor="w",
        text="Select how many questions to include on the practice test.",
        fg="blue", 
        font=("Courier", 12))
    '''

    select_save_folder_text = Message(window,
        anchor="w",
        text="Step 3. Select folder to save practice test and proctor test.",
        fg="blue", 
        font=("Courier", 12))

    generate_text = Message(window,
        anchor="w",
        text="Step 4. Click Generate to build test.",
        fg="blue", 
        font=("Courier", 12))

    '''
    select_number_questions_spinbox = Spinbox(window, 
        from_=1, 
        to=100,
        state=DISABLED)
    '''

    def selectFirstFile(select_file_button_one):
        nonlocal initialdir_var
        nonlocal first_URE_file
        first_URE_file = filedialog.askopenfile(initialdir=initialdir_var)  # Open file dialog
        last_index = str(first_URE_file.name).rindex('/')   # getting position of last folder
        initialdir_var = first_URE_file.name[0:last_index]  # creating a save reference for finding files
        new_button_text = first_URE_file.name.split('/')    # updating button text with filename
        select_file_button_one.config(text=new_button_text[-1]) # setting that button text


    def selectSecondFile(select_file_button_two):
        nonlocal initialdir_var
        nonlocal second_URE_file
        second_URE_file = filedialog.askopenfile(initialdir=initialdir_var) # Open file dialog
        last_index = str(second_URE_file.name).rindex('/')   # getting position of last folder
        initialdir_var = second_URE_file.name[0:last_index]  # creating a save reference for finding files
        new_button_text = second_URE_file.name.split('/')    # updating button text with filename
        select_file_button_two.config(text=new_button_text[-1]) # setting that button text


    def selectFirstAnswerFile(select_answer_button_one):
        nonlocal initialdir_var
        nonlocal first_URE_answer_file
        first_URE_answer_file = filedialog.askopenfile(initialdir=initialdir_var)
        new_button_text = first_URE_answer_file.name.split('/')
        select_answer_button_one.config(text=new_button_text[-1])


    def selectSecondAnswerFile(select_answer_button_two):
        nonlocal initialdir_var
        nonlocal second_URE_answer_file
        second_URE_answer_file = filedialog.askopenfile(initialdir=initialdir_var)
        new_button_text = second_URE_answer_file.name.split('/')
        select_answer_button_two.config(text=new_button_text[-1])


    def selectSaveDirectory(select_save_directory_button):
        nonlocal save_directory
        save_directory = filedialog.askdirectory()
        select_save_directory_button.config(text=save_directory)

    def generatePracticeTests(generate_practice_tests_button):
        nonlocal first_URE_file
        nonlocal second_URE_file
        nonlocal first_URE_answer_file
        nonlocal second_URE_answer_file
        nonlocal save_directory
        bank_of_questions = []
        bank_of_answers = []

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

        GrabQuestions(first_URE_file.name)
        GrabQuestions(second_URE_file.name)
        GrabAnswers(first_URE_answer_file.name)
        GrabAnswers(second_URE_answer_file.name)

        # Need to put this in a function
        sampled_op = random.sample(range(200), 100)
        save_directory = save_directory + '\\'
        practice_test_answers_filename = save_directory + 'Practice_Test_Answers.txt'
        f = open(practice_test_answers_filename, 'a')
        #print('sampled_op: ' + str(sampled_op))
        for x in sampled_op:
            #print(bank_of_questions[x-1])
            #print(bank_of_answers[x-1])
            for y in bank_of_questions[x-1]:
                f.write(str(y))
            new_line = 'Answer: ' + str(bank_of_answers[x-1]) + '\n'
            f.write(new_line)
        f.close()

        counter = 1
        practice_test_filename = save_directory + 'Practice_Test.txt'
        f = open(practice_test_filename, 'a')
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

    '''
    def scanQuestions(scan_questions_button):
        nonlocal first_URE_file
        nonlocal second_URE_file
        if first_URE_file == '' and second_URE_file == '':
            messagebox.showinfo('Warning','Not enough UREs selected!')
        elif first_URE_file != '' and second_URE_file != '':
            select_number_questions_spinbox.config(to=200)
        else:
            select_number_questions_spinbox['state'] ='normal'
    '''


    select_file_button_one = Button(window,
        text="Choose 1st URE",
        fg="blue",
        command=lambda:selectFirstFile(select_file_button_one))

    select_file_button_two = Button(window,
        text="Choose 2nd URE",
        fg="blue",
        command=lambda:selectSecondFile(select_file_button_two))

    select_answer_button_one = Button(window,
        text="Choose 1st Answers",
        fg="blue",
        command=lambda:selectFirstAnswerFile(select_answer_button_one))

    select_answer_button_two = Button(window,
        text="Choose 2nd Answers",
        fg="blue",
        command=lambda:selectSecondAnswerFile(select_answer_button_two))

    select_save_directory_button = Button(window,
        text="Choose Folder",
        fg="blue",
        command=lambda:selectSaveDirectory(select_save_directory_button))

    generate_practice_tests_button = Button(window,
        text="Generate",
        fg="blue",
        command=lambda:generatePracticeTests(generate_practice_tests_button))

    '''
    scan_questions_button = Button(window,
        text="Scan Max Available",
        fg="blue",
        command=lambda:scanQuestions(scan_questions_button))
    '''

    select_ures_text.grid(row=1, column=2, columnspan=3)
    select_file_button_one.grid(row=2, column=2)
    select_file_button_two.grid(row=2, column=3)

    select_answers_text.grid(row=3, column=2, columnspan=3)
    select_answer_button_one.grid(row=4, column=2)
    select_answer_button_two.grid(row=4, column=3)

    #select_no_questions_text.grid(row=5, column=2, columnspan=2)
    #scan_questions_button.grid(row=6, column=2)
    #select_number_questions_spinbox.grid(row=6, column=3)

    select_save_folder_text.grid(row=7, column=2, columnspan=3)
    select_save_directory_button.grid(row=8, column=2, columnspan=2)

    generate_text.grid(row=9, column=2, columnspan=3)
    generate_practice_tests_button.grid(row=10, column=1, columnspan=3)


# greeting screen GUI window
window = Tk()

window.title('CDC Prep Tool - Greeting Screen')
#window.geometry("500x500+10+20")

title_label = Label(window, 
    text="CDC EOC Prep Tool", 
    fg="blue", \
    font=("Courier", 20))

tool_label = Label(window, 
    text="This tool takes in UREs and outputs a random practice test with answers.", 
    fg="blue", 
    font=("Courier", 12))

begin_button=Button(window, 
    text="Begin", 
    fg="blue", 
    command= beginButtonClicked)

title_label.grid( row=1, column=1)
tool_label.grid( row=2, column=1)
begin_button.grid( row=3, column=1)

window.iconbitmap('./logo.ico')

window.mainloop()