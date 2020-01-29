def count_occurrences(s, c):
    """
    Counts the amount of occurrences of a given letter in a given
    alphabetically sorted string.

    :param s: The string
    :type s: str
    :param c: The letter
    :type c: str

    :return: The amount of occurrences of a the letter in the string
    :rtype: int
    """
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

    # Return the result
    if first_occurrence == -1:
        return 0
    return last_occurrence - first_occurrence + 1


def are_equal(s1, s2):
    """
    Checks if two alphabetically sorted string are equal.

    :param s1: The first string
    :type s1: str
    :param s2: The second string
    :type s2: str

    :return: Whether or not the strings are equal
    :rtype: bool
    """
    # Generate list of letters
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
