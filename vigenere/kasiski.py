cryptotext = "ABAJFGABASJD"

# find equal substrings
def find_equal_substrings(cryptotext):
    # create a list of all substrings
    substrings = []
    for i in range(len(cryptotext)):
        for j in range(len(cryptotext)):
            substrings.append(cryptotext[i:j])

    # create a dictionary of substrings and their occurences
    substring_dict = {}
    for substring in substrings:
        if substring in substring_dict:
            substring_dict[substring] += 1
        else:
            substring_dict[substring] = 1
    
    # create a list of substrings that occur more than once
    equal_substrings = []
    for substring in substring_dict:
        if substring_dict[substring] > 1:
            equal_substrings.append(substring)

    return (substring_dict, equal_substrings)


def max_frequency_sustring(substring_dict):
    max_frequency = 0
    for substring in substring_dict:
        if substring_dict[substring] > max_frequency:
            max_frequency = substring_dict[substring]
    return max_frequency


def get_longest_substring(equal_substrings):
    longest_substring = ""
    for substring in equal_substrings:
        if len(substring) > len(longest_substring):
            longest_substring = substring

    return longest_substring


def get_indexes(equal_substrings):
    substrings_indexes = {}
    for substring in equal_substrings:
        indexes = []
        for i in range(len(cryptotext)):
            if cryptotext[i:i+len(substring)] == substring:
                indexes.append(i)
        substrings_indexes[substring] = indexes
        
    return substrings_indexes

def main():
    print(cryptotext)

    frequencies, equal_substrings = find_equal_substrings(cryptotext)
    
    # longest substring
    longest_substring = get_longest_substring(equal_substrings)

    # frequency of longest substring
    frequency_longest_substring = frequencies[longest_substring] 

    print("Longest substring:", longest_substring)
    print("Frequency of longest substring:", frequency_longest_substring)

    # indexes of longest substring
    indexes = get_indexes(equal_substrings)
    print("Indexes of longest substring:", indexes)

    for substring in equal_substrings:
        # substring length
        substring_length = len(substring)
        if substring_length == 0:
            continue
        # if all indexes divide by substring length without remainder
        if all(i == 0 or i % substring_length == 0 for i in indexes[substring]):
            print('\n')
            print("Substring:", substring)
            print("Indexes:", indexes[substring])
            print("Key Length:", substring_length)

if __name__ == "__main__":
    main()