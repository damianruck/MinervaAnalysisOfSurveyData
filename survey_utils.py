import pandas as pd
import os
import json

def merge_dicts(*dict_args):
    """
    Given any number of dictionaries, shallow copy and merge into a new dict,
    precedence goes to key-value pairs in latter dictionaries.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

def save_json(data, filepath):
    with open(filepath, 'w') as fp:
        json.dump(data, fp)
        
def load_json(filepath):
    with open(filepath, 'r') as fp:
        data = json.load(fp)
    return data

def save_txt(string, filepath):
    with open(filepath, 'w') as tf:
         tf.write(string)

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def print_unique_responses_to_all_questions(df, print_threshold=20):

    entries = df.columns
    for e in entries:
        print('unique responses to question: ', e)
        unique_responses = df[e].unique()
        print('number of unique responses: ', len(unique_responses))

        if len(unique_responses) > print_threshold:
            print('too many responses to print!!')
        else:   
            print(list(unique_responses))

        print('------------------------------------------')