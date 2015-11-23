
def legal_password(pword):
    """return if a password is legally formed
    
    arguments:
      pwrod: a string representing a password

    return: 
      True or False

    Valid password requirements:
      at least one digit
      between 5 and 8 chars in length
      at least one vowel
    """
    l = len(pword)
    if l <5 or l > 8:
        return False
    else:
        return True
