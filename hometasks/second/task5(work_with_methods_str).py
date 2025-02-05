
string_1 = "Hello"
string_2 = "TEST-STR"
string_3 = "kra"
def manipulation_string(string):
    print(string[2])
    print(string[-2])
    print((string[0:5]))
    print(string[:len(string)-2])
    print(string[0::2])
    print(string[1::2])
    print(string[::-1])
    print(string[::-2])
    print(len(string))
    return
manipulation_string(string_1)