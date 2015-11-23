
def legal_password(s):
    """tests to see if a password s is legally formed

    Arguments:
      s: a string representing a possible password

    Return:
      True if s is a legally formed password, False otherwise

    Notes:
      Legal passwords are/have
        - between 5 and 8 characters in length
        - has at least one digit
        - has at least one upper case letter
        - has at least one lower case letter
    """
    l = len(s)
    if l < 5:
        return False
    if l > 8:
        return False
    return True
