import re
import pandas as pd
import csv

# TODO: add path of existing .csv file to csv_path
csv_path = "ADD PATH HERE";
#           ^^^^^^^^^^^^^
invalid = "Invalid Input: "
csv_df = pd.read_csv(csv_path)
csv_df_outdated = False


#*def get_question(question_id):
    # update dataframe if outdates
    #if csv_df_outdated:
        #csv_df = pd.read_csv(csv_path)
        #csv_df_outdated = False
    # get question
    #question = csv_df.loc[(csv_df.question_id == question_id) & (csv_df.is_question == "True")]
    #return question


#def append_row(row):# (row: array)
    #with open(csv_path, "a", newline = "") as csvfile:
        #new_writer = csv.writer(csvfile)
        #new_writer.writerow(row)

    #csv_df_outdated = True


def to_csv(args, command_type):
    if command_type == "Question":
        # Then we're adding a new question.
        question_id = args["question_id"]
        is_question = "True"
        week_number = args["week"]
        question_topic = args["topic"]
        answer_language = ""
        text_data = args["question_text"]
    elif command_type == "Answer":
        # Then we're adding an answer.
        question_id = args["question_id"]
        is_question = "False"
        week_number = ""
        question_topic = ""
        answer_language = args["answer_language"]
        text_data = args["answer_text"]
    else:
        print(invalid + "Make sure you typed in the right arguments")
        return

    # saving the entry into CSV
    #append_row([question_id, is_question, week_number, question_topic, answer_language, text_data])


def parse_answer(slack_message):
    split_string = re.split(r'#question_id=|#answer_language=|#answer_text', slack_message)
    # Get rid of blank elements in array
    split_string.remove(split_string[0])
    if len(split_string) != 3:
        print(invalid + "Make sure you have the correct number of arguments and that they're spelled correctly.")
        return None
    args = {
        "question_id": split_string[0],
        "answer_language": split_string[1],
        "answer_text": split_string[2]
    }
    return args


def parse_question(slack_message):
    split_string = re.split(r'#question_id=|#week=|#topic=|#question_text=', slack_message)
    # Get rid of blank elements in array
    split_string.remove(split_string[0])
    if len(split_string) != 4:
        print(invalid + "Make sure you have the correct number of arguments and that they're spelled correctly.")
        return None
    args = {
        "question_id": split_string[0],
        "week": split_string[1],
        "topic": split_string[2],
        "question_text": split_string[3]
    }
    return args


def main():
    raw_input = input("Make sure to format your input like this and in this order if you want to add a question:"
                      "\nadd question | #question_id=1#week=2#topic=Strings#question_text=What dost it do, baby boo?"
                      "\n\nMake sure to format your input like this and in this order if you want to add an answer:"
                      "\nadd answer | #question_id=1#answer_language=Python#answer_text=```print('nm u?')```\n")
    split_input = raw_input.split(' | ')

    if len(split_input) < 2:
        print(invalid + "You at least forgot the ' | ' part. God knows what else you did...")
        return
    elif len(split_input) > 2:
        print(invalid + "There is more than one occurrence of ' | ' in the message.")
        return
    else:
        user_command = split_input[0]
        args = split_input[1]

    if user_command == "add question":
        command_type = "Question"
        arguments = parse_question(args)
    elif user_command == "add answer":
        command_type = "Answer"
        arguments = parse_answer(args)
    else:
        print(invalid + "Make sure you typed the correct command and corresponding arguments.")
        return

    if not arguments:
        print(invalid + "Either arguments don't exist or they've been typed wrong.")
        return
    else:
        print(arguments)
        to_csv(arguments, command_type)


main()
