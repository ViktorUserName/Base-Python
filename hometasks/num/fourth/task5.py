listt =  [1,2,3,4,5,5,5,5,6,7,8,8]

def check_list (arr):
    new_dict = dict()

    for key in arr:
        if key in new_dict:
            new_dict[key] += 1
        else:
            new_dict[key] = 1

    for key in new_dict:
        if new_dict[key] > 1:
            print(f"{key} повторяется {new_dict[key]} раз")
    print(new_dict)


check_list(listt)