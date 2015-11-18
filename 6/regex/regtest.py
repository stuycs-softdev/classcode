import re

def find_phone(s):
    """Returns a list of valid phone numbes from a string

    Args:
      s: a string

    Return:
      An empty list or a list of strings each one representing
      a phone number
    >>> find_phone("")
    []

    >>> find_phone("111-111-1111")
    ['111-111-1111']

    >>> find_phone("stuff 222-222-2222 stuff")
    ['222-222-2222']

    >>> find_phone("111-111-1111 222-222-2222")
    ['111-111-1111', '222-222-2222']

    >>> find_phone("111-222-33334")
    ['111-222-3333']
    """
    exp = "[0-9]{3}-[0-9]{3}-[0-9]{4}"
    result = re.findall(exp,s)
    return result


if __name__=="__main__":
    import doctest
    doctest.testmod()

