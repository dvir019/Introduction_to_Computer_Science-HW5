import ast


def compare_strings(s1, s2):
    """
    Compare two strings according to lexicographical order.

    :param s1: The first string
    :type s1: str
    :param s2: The second string
    :type s2: str

    :return: True if the first string is prior to the second, else false
    :rtype: bool
    """
    s1 = s1.lower()
    s2 = s2.lower()
    s1_len = len(s1)
    s2_len = len(s2)
    index = 0
    for i in range(min(s1_len, s2_len)):
        s1_ord = ord(s1[i])
        s2_ord = ord(s2[i])
        if s1_ord == s2_ord:
            index += 1
        elif s1_ord < s2_ord:
            return True
        else:
            return False
    if index == s1_len:
        return True
    return False


def sort_list_of_strings(str_lst):
    """
    Sorts a list of strings, according to lexicographical order.

    :param str_lst: The list to sort
    :type str_lst: list[str]
    """
    top_index = len(str_lst)
    for i in range(top_index):
        for j in range(0, top_index-1):
            if not compare_strings(str_lst[j], str_lst[j+1]):
                str_lst[j], str_lst[j + 1] = str_lst[j+1], str_lst[j]



# leave intact
def main():
    print('Insert a list of strings:')
    lst = ast.literal_eval(input())
    sort_list_of_strings(lst)
    print()
    print('The sorted list:')
    print(lst)


if __name__ == '__main__':
    main()
