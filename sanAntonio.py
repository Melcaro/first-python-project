# -*- coding: utf8 -*-
import random
import json

# Give a Json file and return a List


def read_values_from_json(path, key):
    values = []
    with open(path) as f:
        data = json.load(f)
        for entry in data:
            values.append(entry[key])
    return values

# Give a json and return a list


def get_random_item(list):
    rand_numb = random.randint(0, len(list)-1)
    print(list[rand_numb])
    return list[rand_numb]

# Return a random item in a list


def clean_strings(sentences):
    cleaned = []
    for sentence in sentences:
        clean_sentence = sentence.strip()
        cleaned.append(clean_sentence)
    return cleaned

# Return a random value from a json file


def random_value(source_path, key):
    all_values = read_values_from_json(source_path, key)
    clean_values = clean_strings(all_values)
    return get_random_item(clean_values)


#####################
###### QUOTES #######
#####################

# Gather quotes from San Antonio

def random_quote():
    return random_value('quotes.json', 'quote')

######################
#### CHARACTERS ######
######################

# Gather characters from Wikipedia


def random_character():
    return random_value('characters.json', 'character')


######################
#### INTERACTION ######
######################

# Print a random sentence.

def print_random_sentence():
    rand_quote = random_quote()
    rand_character = random_character()
    print('>>> {} a dit : {}'.format(rand_character, rand_quote))


def main_loop():
    while True:
        print_random_sentence()
        message = (
            'Voulez-vous voir une autre citation?''Pour sortir du programme,tapez [B].')
        choice = input(message).upper()
        if choice == "B":
            break


if __name__ == "__main__":
    main_loop()
