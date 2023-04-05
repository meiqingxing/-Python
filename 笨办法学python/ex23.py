import sys
script, encoding, error = sys.argv   #命令行参数


def main(language_file, encoding, errors):  #定义main函数
    line = language_file.readline()   #在给出的languages文件中读取一行
   #readline函数到达文件末尾时，会返回空字符串
   
    if line:   #if语句，做决定。如果readline返回空字符串，结果为false，不运行if后的代码；如果readline返回内容，line结果为true，运行if代码
        print_line(line, encoding, errors)
    return main(language_file, encoding, errors)


def print_line(line, encoding, errors):  #定义print_line函数，用来编码languages.txt文件中的每一行内容
    next_lang = line.strip()  #next_lang变量是一个字符串，下面对他调用encode函数来编码字符串，获得原始字节
    raw_bytes = next_lang.encode(encoding, errors)  #括号内是吧想要的编码和如何处理错误传递给encode
    cooked_string = raw_bytes.decode(encoding, errors=errors)   #创建一个变量来逆向展示上一行。raw_bytes是字节，调用decode()函数来获取字符串
    
    print(raw_bytes, "<===>", cooked_string)  #打印：原始字节<===>字符串


languages = open("languages.txt", encoding="utf-8")  #打开languages.txt文件，编码格式为utf-8

main(languages, encoding, error)  #调用main函数；第5行一次，第11行一次，不过if语句避免其无限循环。

