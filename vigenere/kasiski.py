CRYPTOTEXT = "CHREEVOAHMAERATBIAXXWTNXBEEOPHBSBQMQEQERBWRVXUOAKXAOSXXWEAHBWGJMMQMNKGRFVGXWTRZXWIAKLXFPSKAUTEMNDCMGTSXMXBTUIADNGMGPSRELXNJELXVRVPRTULHDNQWTWDTYGBPHXTFALJHASVBFXNGLLCHRZBWELEKMSJIKNBHWRJGNMGJSGLXFEYPHAGNRBIEQJTAMRVLCRREMNDGLXRRIMGNSNRWCHRQHAEYEVTAQEBBIPEEWEVKAKOEWADREMXMTBHHCHRTKDNVRZCHRCLQOHPWQAIIWXNRMGWOIIFKEE"


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
    # starting with 1
    repeated_substrings_indexes = {}

    for substring in repeated_substrings:
        indexes = []
        for i in range(len(CRYPTOTEXT)):
            if CRYPTOTEXT[i:i+len(substring)] == substring:
                indexes.append(i + 1)
        repeated_substrings_indexes[substring] = indexes
        
    return repeated_substrings_indexes


def get_idexes_differences(indexes):
    differences = []
    for i in range(len(indexes) - 1):
        differences.append(indexes[i+1] - indexes[i])
    return differences



def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main() -> None:
    print("Ciphertext: {} \n".format(CRYPTOTEXT))

    substrings_frequencies, repeated_substrings = find_equal_substrings(CRYPTOTEXT)

    for substring in repeated_substrings:
        repeated_substrings_indexes = get_indexes(repeated_substrings)

        indexes = repeated_substrings_indexes[substring]
        differences = get_idexes_differences(indexes)
        
        if len(differences) > 1:
            # find greatest common divisor of all differences
            greatest_common_divisor = gcd(differences[0], differences[1])
            for i in range(2, len(differences)):
                greatest_common_divisor = gcd(greatest_common_divisor, differences[i])

            if greatest_common_divisor > 1:
                # if all indexes divide by substring length without remainder
                print('\n')
                print("Substring: ", substring)
                print("Frequency: ", substrings_frequencies[substring])
                print("Indexes: ", repeated_substrings_indexes[substring])
                print("Differences: ", differences)
                print("GCD (possible key length): ", greatest_common_divisor)


if __name__ == "__main__":
    main()