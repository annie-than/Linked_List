
def string_reverser(our_string):
    """
    Reverse the input string

    Args:
        our_string(string): String to be reversed
    Returns:
        string: The reversed string
    """

    # New empty string
    new_string = ""

    # Iterate over old string
    for i in range(len(our_string) - 1, -1, -1):
        new_string += our_string[i]
    return new_string


# Test Cases
print("Pass" if ('retaw' == string_reverser('water')) else "Fail")
print("Pass" if ('!noitalipunam gnirts gnicitcarP' == string_reverser('Practicing string manupilation!')) else "Fail")
print ("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")






