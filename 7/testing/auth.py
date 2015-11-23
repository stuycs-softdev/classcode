
def legal_password(s):
    """determine if a password is legally formed

    Arguments:
      s: a string representing a password

    Returns:
      True if s is legally formed, False otherwise

    Notes:
      A password is legally formed if it is/has
        - between 5 and 8 characters in length
        - at least one digit
        - at least one upper case letter
        - at least one lower case letter
    """
    l = len(s)
    if l < 5 or l > 8:
        return False

    return True

