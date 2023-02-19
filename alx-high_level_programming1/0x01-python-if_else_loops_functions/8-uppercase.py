#!/usr/bin/python3
def uppercase(s):
    """
    Prints the string s in uppercase followed by a new line.
    """
    # Initialize an empty string to store the uppercase version of s.
    uppercase_s = ""

    # Loop over each character in s.
    for c in s:
        # Convert the character to its Unicode code point.
        code_point = ord(c)

        # If the character is a lowercase letter, convert it to uppercase
        # by subtracting 32 from its code point. Otherwise, leave it as is.
        if code_point >= 97 and code_point <= 122:
            code_point -= 32

        # Add the character (in uppercase, if applicable) to the new string.
        uppercase_s += chr(code_point)

    # Print the uppercase string followed by a new line.
    print("{}\n".format(uppercase_s))

