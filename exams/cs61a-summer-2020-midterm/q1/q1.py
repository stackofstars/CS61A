email = 'staceyvu@berkeley.edu'

def cat(password, limit):
    """ Write a higher-order function `cat` that returns a one-argument
    function `attempt`. Every time `attempt` is called, it checks to see if its argument
    matches the password at the corresponding index.

    If the password entirely matches, return a success string. If more than `limit`
    number of incorrect hacks are attempted, you should return an error string.
    For details, see the doctest.


    Note: to comment out a blank that covers an entire line, just put down 'unnecessary' (with quotes)

    >>> hacker = cat([1,2], 2)
    >>> hacker(1)
    >>> hacker(2)
    'Access granted!'
    >>> hacker = cat([1,2], 1)
    >>> hacker(1)
    >>> hacker(3) # used up attempts to gain access
    >>> hacker(2) # correct attempt to gain access, but already locked
    'The trapdoor has been activated!'
    >>> hacker = cat([1,2], 2)
    >>> hacker(1)
    >>> hacker(3) # 1 attempt left to gain access
    >>> hacker(2) # correct attempt to gain access
    'Access granted!'
    """
    index = 0
    wrong = 0
    def attempt(digit):
        nonlocal wrong
        nonlocal index
        if wrong >= limit:
            return 'The trapdoor has been activated!'
        if digit == password[index]:
            index += 1
            if index == len(password):
                return 'Access granted!'
        else:
            wrong += 1
    return attempt

# ORIGINAL SKELETON FOLLOWS

# def cat(password, limit):
#     """ Write a higher-order function `cat` that returns a one-argument
#     function `attempt`. Every time `attempt` is called, it checks to see if its argument
#     matches the password at the corresponding index.

#     If the password entirely matches, return a success string. If more than `limit`
#     number of incorrect hacks are attempted, you should return an error string.
#     For details, see the doctest.


#     Note: to comment out a blank that covers an entire line, just put down 'unnecessary' (with quotes)

#     >>> hacker = cat([1,2], 2)
#     >>> hacker(1)
#     >>> hacker(2)
#     'Access granted!'
#     >>> hacker = cat([1,2], 1)
#     >>> hacker(1)
#     >>> hacker(3) # used up attempts to gain access
#     >>> hacker(2) # correct attempt to gain access, but already locked
#     'The trapdoor has been activated!'
#     >>> hacker = cat([1,2], 2)
#     >>> hacker(1)
#     >>> hacker(3) # 1 attempt left to gain access
#     >>> hacker(2) # correct attempt to gain access
#     'Access granted!'
#     """
#     ______
#     ______
#     def attempt(digit):
#         ______
#         ______
#         if ______:
#             return ______
#         if ______:
#             ______
#             if ______:
#                 return ______
#         else:
#             ______
#     return ______
