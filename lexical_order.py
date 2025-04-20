def lexical_order(word_1, word_2, alphabet):
    # create lexical dict 
    lexical_dict = {}
    for i, char in enumerate(alphabet):
        lexical_dict[char] = i

    i = j = 0
    while i < len(word_1) and j < len(word_2):
        # continue iterating forward 
        if word_1[i] == word_2[j]:
            i += 1
            j += 1
        else:
            # derive lexical values
            lexical_value_1 = lexical_dict[word_1[i]]
            lexical_value_2 = lexical_dict[word_2[j]] 

            if lexical_value_1 < lexical_value_2:
                return True
            else:
                return False

    if i == len(word_1):
        return True
    if j == len(word_2):
        return False

if __name__ == "__main__":
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    print(lexical_order("apple", "dock", alphabet)) # -> True

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    print(lexical_order("apple", "ample", alphabet)) # -> False