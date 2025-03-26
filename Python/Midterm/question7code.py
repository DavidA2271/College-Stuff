

# pseudo code

# O(n^2) time-complexity
def anagram_dict(word):
    anagrams = []
    Dictionary = {}

    # O(n^2) worst-case time-complexity
    sorted_word = insert_sort(word)

    # O(500,000) loop == O(1)
    for i in Dictionary:
        if len(i) != len(word):
            continue
        # O(n^2) worst-case time-complexity
        sorted_entry = insert_sort(i)
        is_anagram = True
        # O(n) time-complexity
        for j in range(len(word)):
            if sorted_word[j] != sorted_entry[j]:
                is_anagram = False
        if is_anagram:
            anagrams.append(i)
    # remove duplicate words, O(n) time-complexity for set constructor
    return set(anagrams)


# O(n^2) time-complexity
def anagram_combo(word):
    # Using a set to prevent duplicate words if
    # the given word contains multiple of the same letter
    anagram_set = {}
    size = len(word)
    fact = factorial(size)
    for i in range(fact):
        for j in range(size):
            # all letter combinations generated here
            pass

    return anagram_set


def factorial(n):
    # O(n) time complexity
    result = 1
    for i in range(1, n+1):
        result = result * i


def is_word(string):
    # Would check if the provided string is in the dicitonary
    return False