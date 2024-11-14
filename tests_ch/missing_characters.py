
def missingCharacters(s):
    string_all_letters = 'abcdefghijklmnopqrstuvwxyz'
    string_all_digits = '0123456789'

    set_str_all_leters = set(string_all_letters)
    set_str_all_digits = set(string_all_digits)

    s_lower = s.lower()

    set_s = set(s_lower)

    missing_l = (set_str_all_leters - set_s)
    missing_d = (set_str_all_digits - set_s)

    # The sorted() function takes set and returns a new sorted list in ascending order. 
    missing_letters = sorted(missing_l)
    missing_digits = sorted(missing_d)
    
    # Combine sorted digit and letters set and use joing to get the elements of the set
    missing_characters = "".join(missing_digits + missing_letters)

    return missing_characters


if __name__ == "__main__":
    s="I am python 2024"
    missingcharacters = missingCharacters(s)
    print(missingcharacters)