```
def pal_checker(strr):

    ''' This function checks to see if an inputted string strr, is a palindrome. The .replace() function removes all white spaces between the string. The .lower() makes all the letters lowercase, so as to make the cases uniform, because Python is case sensitive.'''

    new_str = strr.replace(' ', '')
    new_str = new_str.lower()
    if new_str == new_str[::-1]:
        print("'{}' is a palindrome".format(strr))
        return True
    else:
        print("'{}' is not a palindrome".format(strr))
        return False
```