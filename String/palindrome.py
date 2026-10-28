
def is_palindrome(input_string):
    newString=""
    reversedString=""

    for c in input_string:
        if c !=" ":
            newString+=c.lower()
    if newString==newString[::-1]:
        return True
    return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak"))