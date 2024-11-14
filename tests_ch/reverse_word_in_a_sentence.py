

def reverse_words(sentence_string):
    words_list = sentence_string.split()
    reverse_words_list = reversed(words_list)
    reverse_words_sentence_string = " ".join(reverse_words_list)

    print(reverse_words_sentence_string)
    
    return reverse_words_sentence_string

reverse_words("I am python")
