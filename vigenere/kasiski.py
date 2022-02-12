cryptotext = "ABAJFGABASJD"

 
# find equal substrings
def find_equal_substrings(cryptotext):
    # create a list of all substrings
    all_substrings = []
    for i in range(len(cryptotext)):
        for j in range(len(cryptotext)):
            all_substrings.append(cryptotext[i:j])

    # create a dictionary of substrings and their occurences
    substring_occurancies = {}
    for substring in all_substrings:
        if substring in substring_occurancies:
            substring_occurancies[substring] += 1
        else:
            substring_occurancies[substring] = 1
    
    # create a list of substrings that occur more than once
    repeated_substrings = []
    for substring in substring_occurancies:
        if substring_occurancies[substring] > 1 and len(substring) > 1:
            repeated_substrings.append(substring)

    return (substring_occurancies, repeated_substrings)


def get_indexes(repeated_substrings) -> dict:
    repeated_substrings_indexes = {}

    for substring in repeated_substrings:
        indexes = []
        for i in range(len(cryptotext)):
            if cryptotext[i:i+len(substring)] == substring:
                indexes.append(i)
        repeated_substrings_indexes[substring] = indexes
        
    return repeated_substrings_indexes


def main() -> None:
    print("Ciphertext: ", cryptotext)

    substrings_frequencies, repeated_substrings = find_equal_substrings(cryptotext)

    for substring in repeated_substrings:
        substring_length = len(substring)
        repeated_substrings_indexes = get_indexes(repeated_substrings)

        # if all indexes divide by substring length without remainder
        if all(i == 0 or i % substring_length == 0 for i in repeated_substrings_indexes[substring]):
            print('\n')
            print("Substring: ", substring)
            print("Indexes: ", repeated_substrings_indexes[substring])
            print("Key Length: ", substring_length)
            print("Frequency: ", substrings_frequencies[substring])

if __name__ == "__main__":
    main()