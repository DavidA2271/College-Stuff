

def kmp(input, pattern):
    lps = find_lps(pattern)
    input_index = 0
    pattern_index = 0
    while input_index < len(input):
        if input[input_index] == pattern[pattern_index]:
            input_index += 1
            pattern_index += 1
        else:
            if pattern_index == 0:
                input_index += 1
            else:
                pattern_index = lps[pattern_index-1]
        if pattern_index ==  len(pattern):
            return input_index - len(pattern)
    return -1


def find_lps(pattern):
    p_len = len(pattern)
    lps = [0] * p_len
    prev_lps = 0
    index = 1
    while index < p_len:
        if pattern[index] == pattern[prev_lps]:
            lps[index] = prev_lps + 1
            prev_lps += 1
            index += 1
        elif prev_lps == 0:
            lps[index] = 0
            index += 1
        else:
            prev_lps = lps[prev_lps - 1]
    return lps
