import os
import argparse
import re
from collections import Counter

MOST_COMMON_WORDS_NUMB = 5

def load_data(filepath):
    if not os.path.isfile(filepath):
        return None
    with open(filepath, 'r', encoding = 'cp1251') as content:
        opened_text = content.read()
        return opened_text
        
def get_most_frequent_words(opened_text):
    separated_text = re.findall(r'\w+', opened_text.lower())
    most_frequent_words = Counter(separated_text).most_common(MOST_COMMON_WORD_NUMBS) 
    print(most_frequent_words)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--path', required = True,
                        help = 'Enter path to file')
    namespace = parser.parse_args()
    
    filetext = load_data(namespace.path)
    get_most_frequent_words(filetext)
