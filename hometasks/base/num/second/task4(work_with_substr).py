
string_1 = "hhhabchghhh"
string_2 = "hh89h8hHH7h8h9h7h9h0hhkhkhh"

def replace_some_alphabet(string, substirng, upper_substirng):
    new_string = string.replace(substirng, upper_substirng, string.count(substirng)-1)
    if new_string[0] == upper_substirng: new_string = new_string.replace(upper_substirng, substirng, 1)
    return print(new_string)

replace_some_alphabet(string_1, "h", "H")
replace_some_alphabet(string_2,  "h", "H")