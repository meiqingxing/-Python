def break_words(stuff):    #此程序是定义各种函数，然后在命令行里面调用（pdf中说是在翻译器里面与ex25.py文件进行交互）
    """This function will break up words for us."""   #"""这是文本注释
    words = stuff.split(' ')  #split()函数，切割句子，把句子切成单词放在' '里面
    return words

def sort_words(words):   #sort：排序
    """Sorts the words."""
    return sorted(words)  

def print_first_word(words):
    """"Prints the first word after popping it off."""  #函数pop()裁剪下来
    word = words.pop(0)  #将第一个单词切掉
    print(word)

def print_last_word(words):   #函数pop()
    """Prints the last word after popping it off."""
    word = words.pop(-1)   #将最后一个单词切掉
    print(word)
    
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words"""
    words = break_words(sentence)  #直接调用定义的break_words函数
    return sort_words(words)   #经过break_words处理的函数，并调用sort_words函数

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)  #调用sort_sentence函数
    print_first_word(words)
    print_last_word(words)