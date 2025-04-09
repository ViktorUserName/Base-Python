
string_1 = "‘Hello world’, ‘a b c’, ‘test’, ‘test1 test2 test3 test4 test5’)."
string_2 = "Fusce ex risus, auctor eu feugiat eu, euismod ut libero. Aenean malesuada congue accumsan."

def check_words(string):
    return print(string.count(" ")+1)

check_words(string_1)
check_words(string_2)