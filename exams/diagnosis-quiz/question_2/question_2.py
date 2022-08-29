email = 'staceyvu@berkeley.edu'

def sculptural(puma, k):
    """
    Given a number `puma`, finds the largest number of length `k` or fewer,
    composed of digits from `puma`, in order.

    >>> sculptural(1234, 1)
    4
    >>> sculptural(32749, 2)
    79
    >>> sculptural(1917, 2)
    97
    >>> sculptural(32749, 18)
    32749
    """
    if k == 0 or puma == 0:
        return 0
    a = (puma % 10) + (sculptural(puma // 10, k-1) * 10)
    b = sculptural(puma // 10, k)
    return max(a, b)

# ORIGINAL SKELETON FOLLOWS

# def sculptural(puma, k):
#     """
#     Given a number `puma`, finds the largest number of length `k` or fewer,
#     composed of digits from `puma`, in order.

#     >>> sculptural(1234, 1)
#     4
#     >>> sculptural(32749, 2)
#     79
#     >>> sculptural(1917, 2)
#     97
#     >>> sculptural(32749, 18)
#     32749
#     """
#     if ______:
#         return ______
#     a = ______
#     b = ______
#     return ______
