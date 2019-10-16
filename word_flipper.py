
def word_flipper(our_string):
    """
    Flip the individual words in a sentence

    Args:
         our_string(string): String with words to flip
    Returns:
        string: String with words flipped
    """
    new_list = our_string.split(" ")
    re_list = []
    re_string = ""

    for item in new_list:
        string = ""
        for i in range(1, len(item) + 1):
            string += item[len(item) - i]
        item = string
        re_list.append(item)

    re_string = " ".join(re_list)
    return re_string


print("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")
