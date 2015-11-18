import re

def find_phone(s):
    """Return a list of valid phone numbers given a string of text

    Arguments:
      s: A string of text

    Returns:
      An empty list or a list of strings each one being a phone number
    
    >>> find_phone("")
    []

    >>> find_phone("111-111-1111")
    ['111-111-1111']

    >>> find_phone("stuff 222-222-2222 stuff")
    ['222-222-2222']

    >>> find_phone("111-111-1111 and 222-222-22252")
    ['111-111-1111', '222-222-2225']
    """
    pattern = "[0-9]{3}-[0-9]{3}-[0-9]{4}"
    result = re.findall(pattern,s)
    return result

if __name__=="__main__":
    import doctest
    doctest.testmod()
    
