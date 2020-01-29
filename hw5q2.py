def count_occurrences(s, c):
    low = 0
    high = len(s) - 1
    first_occurrence = -1
    last_occurrence = -1
    ord_c = ord(c)
    # Find the first occurrence
    while low <= high:
        mid = (low + high) // 2
        ord_mid = ord(s[mid])
        if ord_c <= ord_mid:
            if ord_c == ord_mid:
                first_occurrence = mid
            high = mid - 1
        else:
            low = mid + 1
    low = 0
    high = len(s) - 1
    # Find the last occurrence
    while low <= high:
        mid = (low + high) // 2
        ord_mid = ord(s[mid])
        if ord_c >= ord_mid:
            if ord_c == ord_mid:
                last_occurrence = mid
            low = mid + 1
        else:
            high = mid - 1

    if first_occurrence != -1:
        return last_occurrence - first_occurrence + 1
    return 0


def are_equal(s1, s2):
    # if len(s1) != len(s2):
    #     return False
    # if len(s1) == 0:
    #     return True  # Both strings are empty
    # s1_first_char = s1[0]
    # s2_first_char = s2[0]
    # if ord(s1_first_char) != ord(s2_first_char):
    #     print("diff")
    #     return False
    # s1_occurrences = count_occurrences(s1, s1_first_char)
    # s2_occurrences = count_occurrences(s2, s2_first_char)
    # print(f"s1_first: {s1_first_char}, s1_occ: {s1_occurrences}")
    # print(f"s2_first: {s2_first_char}, s2_occ: {s2_occurrences}")
    #
    # if s1_occurrences != s2_occurrences:
    #     return False
    # return are_equal(s1[s1_occurrences:], s2[s2_occurrences:])

    # if len(s1) != len(s2):
    #     return False
    # if len(s1) == 0:
    #     return True  # Both strings are empty
    letters = [chr(c) for c in range(ord('a'), ord('z') + 1)]
    for letter in letters:
        s1_occurrences = count_occurrences(s1, letter)
        s2_occurrences = count_occurrences(s2, letter)
        if s1_occurrences != s2_occurrences:
            return False
    return True


def main():
    print('Enter s1:')
    s1 = input()
    print('Enter s2:')
    s2 = input()

    res = are_equal(s1, s2)
    if res:
        print('Strings are equal!')
    else:
        print('Strings are not equal...')


# leave intact
if __name__ == '__main__':
    main()
