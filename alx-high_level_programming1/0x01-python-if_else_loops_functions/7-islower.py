#!/usr/bin/python3
def islower(c):
    """
    Returns True if c is lowercase, False otherwise.
    """
    # Convert the character to its Unicode code point.
    code_point = ord(c)

    # Check if the code point corresponds to a lowercase character.
    # The range of lowercase letters in Unicode is 97 to 122.
    if code_point >= 97 and code_point <= 122:
        return True
    else:
        return False

