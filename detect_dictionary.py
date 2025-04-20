def detect_dictionary(dictionary, alphabet):
    # create lexical dict
    lexical_dict = {}
    for i, char in enumerate(alphabet):
       lexical_dict[char] = i

    # iterate through dict
    for idx in range(len(dictionary)-1):
       word_1 = dictionary[idx]
       word_2 = dictionary[idx+1]

       i = 0
       while i < len(word_1) and i < len(word_2):
        if word_1[i] != word_2[i]:
            if lexical_dict[word_1[i]] > lexical_dict[word_2[i]]:
                return False
            break 
        i += 1

        # If we exited the loop without breaking, check prefix case
        if len(word_1) > len(word_2):
            return False
           
    # lexicographically ordered dict
    return True

if __name__ == "__main__":
    dictionary = ["zoo", "tick", "tack", "door"]
    alphabet = "ghzstijbacdopnfklmeqrxyuvw"
    print(detect_dictionary(dictionary, alphabet)) # -> True