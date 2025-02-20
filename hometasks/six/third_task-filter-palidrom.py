#  Дан список строк. С помощью filter() получить список
# тех строк из исходного списка, которые являются
# палиндромами (читаются в обе стороны одинаково, например,
# ’abcсba’

sab_sub_list = ['aasdsaa','dqwdqw','dsadqw','qwertyytrewq']

def checking_palidroms (arr: list) -> list:
    return list(filter(lambda item: item == item[::-1], sab_sub_list))

print(checking_palidroms(sab_sub_list))