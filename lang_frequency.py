import os
import argparse
import re
import chardet
from collections import Counter

MOST_COMMON_WORDS_NUMB = 10

def define_charset(filepath):
    if not os.path.isfile(filepath):
        return None
    with open(filepath,'rb') as file_with_unkwown_charset:
        file_charset = chardet.detect(file_with_unkwown_charset.read()).get('encoding')
        return file_charset

def load_data(filepath):
    if not os.path.isfile(filepath):
        return None
    with open(filepath, 'r', encoding = define_charset(filepath)) as content:
        opened_text = content.read()
        return opened_text
        
def get_most_frequent_words(opened_text):
    separated_text = re.findall(r'\w+', opened_text.lower())
    most_frequent_words = Counter(separated_text).most_common(MOST_COMMON_WORDS_NUMB) 
    return most_frequent_words
    print(most_frequent_words)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--path', required = True,
                        help = 'Enter path to file')
    namespace = parser.parse_args()

    try:
        file_text = load_data(namespace.path)
        frequent_words_list = get_most_frequent_words(file_text)
        print('\n{} the most frequent words in text:\n'.format(MOST_COMMON_WORDS_NUMB))
        for word_count in frequent_words_list:
            print('"{}": {}'.format(word_count[0].capitalize(), word_count[1]))
    except AttributeError:
        print('\nWrong filepath.')
