import os
import argparse
from collections import Counter

MOST_COMMON_WORD_NUMB = 10

def load_data(filepath):
    if not os.path.isfile(filepath):
        return None
    with open(filepath, 'r', encoding = 'cp1251') as content:
        opened_text = content.read()
        return opened_text
        
def get_most_frequent_words(opened_text):
    separated_text = opened_text.lower().split() 
    most_frequent_words = Counter(separated_text).most_common(MOST_COMMON_WORD_NUMB) 
    print(most_frequent_words)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--path', required = True,
                        help = 'Enter path to file')
    namespace = parser.parse_args()
    
    filetext = load_data(namespace.path)
    get_most_frequent_words(filetext)
