import re

def find_phone(s):
    """Return a list of phone numbers in a page

    Args:
      s: a string of text

    Returns:
      a list of strings, each one being a phone number

    >>> find_phone("")
    []
    >>> find_phone("111-222-3333")
    ['111-222-3333']
    >>> find_phone("some stuff 111-222-3333 and other stuff")
    ['111-222-3333']
    >>> find_phone("123-456-78901")
    ['123-456-7890']
    >>> find_phone("hello 111-111-1111 world 222-222-2222 stuff")
    ['111-111-1111', '222-222-2222']
    >>> find_phone("hello 111-111-1111 world 222-222-20222 stuff")
    ['111-111-1111', '222-222-2022']
    """
    exp = "[0-9]{3}-[0-9]{3}-[0-9]{4}"
    result = re.findall(exp,s);
    return result

if __name__=="__main__":
    import doctest
    doctest.testmod()
    
