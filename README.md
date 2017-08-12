# Frequency Analysis of Words

The intent of the program is to perform Term Frequency Analysis.
Program read text file in any encoding and return 10 the most frequent words in descending order.

# Quickstart

To run the program use the following commands in CLI:

```
python lang_frequency.py -p <filepath> 

or

python lang_frequency --path <filepath>

Filepath should be like:  C:\projects\devman\5_lang_frequency\description.txt
```

3-rd party module 'chardet' is used to detect file encoding.
Use ```pip install -r requirements.txt``` to install the module.  

Quantity (10) of the shown most frequent words is hardcoded into program in constant ```MOST_COMMON_WORDS_NUMB```

# Example of Script Launch

```
10 the most frequent words in text:

"В": 5
"С": 3
"Частота": 3
"И": 2
"Частицы": 2
"Ускоритель": 2
"Ускорения": 2
"Чтобы": 2
"Орбиты": 2
"Процессе": 2

```

# Project Goals

The code is written for educational purposes. Training course for web-developers -[DEVMAN.org](https://devman.org)

