email = 'staceyvu@berkeley.edu'

def lemon(kt):
    """
    A lemon-copy is a perfect replica of a nested list's box-and-pointer structure.
        If an environment diagram were drawn out, the two should be entirely
        separate but identical.

    A `kt` is a list that only contains ints and other lists.

    The function `lemon` generates a lemon-copy of the given list `kt`.

    Note: The `isinstance` function takes in a value and a type and determines
        whether the value is of the given type. So

        >>> isinstance("abc", str)
        True
        >>> isinstance("abc", list)
        False

    Here's an example, where lemon_y = lemon(y)


                             +-----+-----+            +-----+-----+-----+
                             |     |     |            |     |     |     |
                             |  +  |  +-------------> | 200 | 300 |  +  |
        y +----------------> |  |  |     |            |     |     |  |  |
                             +-----+-----+       +--> +-----+-----+-----+
        lemon_y +-+             |                |       ^           |
                  |             +----------------+       |           |
                  |                                      +-----------+
                  |
                  |          +-----+-----+            +-----+-----+-----+
                  |          |     |     |            |     |     |     |
                  +------->  |  +  |  +-------------> | 200 | 300 |  +  |
                             |  |  |     |            |     |     |  |  |
                             +-----+-----+       +--> +-----+-----+-----+
                                |                |       ^           |
                                +----------------+       |           |
                                                         +-----------+

    >>> x = [200, 300]
    >>> x.append(x)
    >>> y = [x, x]              # this is the `y` from the doctests
    >>> lemon_y = lemon(y)      # this is the `lemon_y` from the doctests
    >>> # check that lemon_y has the same structure as y
    >>> len(lemon_y)
    2
    >>> lemon_y[0] is lemon_y[1]
    True
    >>> len(lemon_y[0])
    3
    >>> lemon_y[0][0]
    200
    >>> lemon_y[0][1]
    300
    >>> lemon_y[0][2] is lemon_y[0]
    True
    >>> # check that lemon_y and y have no list objects in common
    >>> lemon_y is y
    False
    >>> lemon_y[0] is y[0]
    False
    """
    lemon_lookup = []
    def helper(kt):
        if ______:
            return ______
        for old_new in kt:
            if isinstance(old_new, int):
                return old_new[1]
        new_kt = []
        lemon_lookup.append((kt, new_kt))
        for element in lemon_lookup:
            helper(element)
        return new_kt
    return helper(kt)

# ORIGINAL SKELETON FOLLOWS

# def lemon(kt):
#     """
#     A lemon-copy is a perfect replica of a nested list's box-and-pointer structure.
#         If an environment diagram were drawn out, the two should be entirely
#         separate but identical.

#     A `kt` is a list that only contains ints and other lists.

#     The function `lemon` generates a lemon-copy of the given list `kt`.

#     Note: The `isinstance` function takes in a value and a type and determines
#         whether the value is of the given type. So

#         >>> isinstance("abc", str)
#         True
#         >>> isinstance("abc", list)
#         False

#     Here's an example, where lemon_y = lemon(y)


#                              +-----+-----+            +-----+-----+-----+
#                              |     |     |            |     |     |     |
#                              |  +  |  +-------------> | 200 | 300 |  +  |
#         y +----------------> |  |  |     |            |     |     |  |  |
#                              +-----+-----+       +--> +-----+-----+-----+
#         lemon_y +-+             |                |       ^           |
#                   |             +----------------+       |           |
#                   |                                      +-----------+
#                   |
#                   |          +-----+-----+            +-----+-----+-----+
#                   |          |     |     |            |     |     |     |
#                   +------->  |  +  |  +-------------> | 200 | 300 |  +  |
#                              |  |  |     |            |     |     |  |  |
#                              +-----+-----+       +--> +-----+-----+-----+
#                                 |                |       ^           |
#                                 +----------------+       |           |
#                                                          +-----------+

#     >>> x = [200, 300]
#     >>> x.append(x)
#     >>> y = [x, x]              # this is the `y` from the doctests
#     >>> lemon_y = lemon(y)      # this is the `lemon_y` from the doctests
#     >>> # check that lemon_y has the same structure as y
#     >>> len(lemon_y)
#     2
#     >>> lemon_y[0] is lemon_y[1]
#     True
#     >>> len(lemon_y[0])
#     3
#     >>> lemon_y[0][0]
#     200
#     >>> lemon_y[0][1]
#     300
#     >>> lemon_y[0][2] is lemon_y[0]
#     True
#     >>> # check that lemon_y and y have no list objects in common
#     >>> lemon_y is y
#     False
#     >>> lemon_y[0] is y[0]
#     False
#     """
#     lemon_lookup = []
#     def helper(kt):
#         if ______:
#             return ______
#         for old_new in ______:
#             if ______:
#                 return old_new[1]
#         new_kt = []
#         lemon_lookup.append((kt, new_kt))
#         for element in ______:
#             ______
#         return new_kt
#     return helper(kt)
