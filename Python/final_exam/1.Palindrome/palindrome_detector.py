import random


def generate_random_dna_sequence(length):
    ''' This is the code you provided 
        I had trouble importing the file since it had a dot in the filename, so I just moved the function here.
    '''
    nucleotides = ['A', 'C', 'G', 'T']
    sequence = ''.join(random.choices(nucleotides, k=length))
    return sequence




def find_longest_palindrome(sequence:str):
    ''' This algorithm uses a dynamic approach to find the longest palindrome in a given sequence of DNA '''
    NUCLEOTIDES = ['A', 'C', 'G', 'T']
    # Since a palindrome must begin and end with the same letter, I used this to my advantage.
    # First I index the location of every character and store it in a dictionary with each character being a key
    p = get_pos_of_all_chars(sequence, NUCLEOTIDES)
    longest = ''
    length = 0
    for nuc in NUCLEOTIDES:
        # list of indexes for current nucleotide
        pos_list = p[nuc]

        for i in range(len(pos_list)):
            ''' Example of how code works


                Assume I'm currently looking through 'A'.
                I get the longest substring in the sequence that starts and ends with 'A'.
                I check if it is a palindrome.
                If not I move on to the second longest substring and check if it is palindrome.

                When I find a palindrome, I update the longest and length variables above and stop searching for
                palindromes under the letter 'A' since they are guaranteed to not be longer than the one I found.
                Then I look through remaining nucleotides in the same fashion, but only if the substring
                to check is longer than the longest palindrome found.
            '''
            begin_pos = pos_list[i]
            second_pos_counter = len(pos_list) - 1
            while second_pos_counter > i:
                end_pos = pos_list[second_pos_counter] + 1
                if end_pos - begin_pos <= length:
                    break
                substr = sequence[begin_pos:end_pos]
                is_palindrome = test_palindrome(substr)
                if is_palindrome:
                    longest = substr
                    length = len(substr)
                    break
                second_pos_counter -= 1
    return (longest, length)


def test_palindrome(sequence):
    # Will round down if sequence length is an odd number
    # Not a problem, since the middle letter does not need to be checked in a palindrome
    half_size = int(len(sequence) / 2)
    for i in range(half_size):
        # Check if characters equal distance away from the ends of the string are the same
        if sequence[i] != sequence[-i-1]:
            return False
    return True


def get_pos_of_all_chars(sequence, char_list):
    ''' Returns a dictionary that contains the index of every like character '''
    char_pos:dict[str, list] = {}
    for i, letter in enumerate(sequence):
        if not letter in char_pos.keys():
            char_pos[letter] = [i]
        else:
            char_pos[letter].append(i)
    return char_pos


def main():
    sequence = "AGCTTAGCTAGCTACGATCGATCGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCATCGATCGATCGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCATCGATCGATCGTAGCTAGCTAGCTAAGCTTAGCTAGCTTAGCTAGCTACGATCGATCGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCATCGATCGATCGTAGCTAGCTAGCT"
    longest_palindrome = find_longest_palindrome(sequence)
    print(f"The longest palindrome found in the sequence {sequence} is:")
    print(f"{longest_palindrome[0]} with length {longest_palindrome[1]}")
    print()
    print()

    for i in range(10):
        s = generate_random_dna_sequence(300)
        lp = find_longest_palindrome(s)
        print(f"The longest palindrome found in the sequence {s} is:")
        print(f"{lp[0]} with length {lp[1]}")
        print()
        print()


if __name__ == '__main__':
    main()
