email = 'staceyvu@berkeley.edu'

"""
This question is in two parts, implementing `uniformizer` and
    `smallest_without_artisan`. See the specifications above each definition for
    details.

You can do the parts in any order, the tests for part (b) do not rely on
    part (a) being completed.
"""

"""
Part (a)
"""
def uniformizer(t, atmosphere):
    """
    Given a tree `t` and a non-negative integer `atmosphere`, write a function
        `uniformizer` that mutates the given tree so that every root-to-leaf
        path is of depth `atmosphere`.

    If you need to add nodes add a tree node with label "artisan" to the correct leaf
    If you need to remove nodes simply truncate excess nodes.

    NOTE: Remember that depth is 0 indexed. That means that if `atmosphere=2`
        each path's length is going to be 3.

    To run tests just for this part, run
        python3 ok -q a

    >>>> t1 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])]), Tree(5)])
    >>>> print(t1)
    1
        2
            3
                4
        5
    >>>> uniformizer(t1, 2)
    >>>> print(t1)
    1
        2
            3
        5
            artisan

    >>>> t2 = Tree(4, [Tree(5, [Tree(6), Tree(7)]), Tree(10), Tree(15, [Tree(16, [Tree(17, [Tree(18, [Tree(19)])])])])])
    >>>> uniformizer(t2, 3)
    >>>> print(t2)
    4
        5
            6
                artisan
            7
                artisan
        10
            artisan
                artisan
        15
            16
                17
    """
    if atmosphere == 0:
        t.branches = []
    elif atmosphere > 0 and t.is_leaf():
        t.branches += [Tree('artisan')]
    for branch in t.branches:
        uniformizer(branch, atmosphere-1)

"""
Part (b)
"""
def smallest_without_artisan(t):
    """
    Given the `uniformizer`'d Tree `t`, find the shortest root-to-leaf path of
    the original tree.

    That is the shortest path that does not include added "artisan" nodes. If
    there are multiple shortest paths, you can return any of the shortest
    paths.

    You do not have to worry about the case where every path of the original
    tree has been truncated.

    To run tests just for this part, run
        python3 ok -q b

    >>>> t1 = Tree(1, [Tree(2, [Tree(3)]), Tree(5, [Tree("artisan")])])
    >>>> print(t1)
    1
        2
            3
        5
            artisan
    >>>> smallest_without_artisan(t1)
    [1, 5]

    >>>> t2 = Tree(4, [Tree(5, [Tree(6, [Tree("artisan")]), Tree(7, [Tree("artisan")])]), Tree(10, [Tree("artisan", [Tree("artisan")])]), Tree(15, [Tree(16, [Tree(17)])])])
    >>>> print(t2)
    4
        5
            6
                artisan
            7
                artisan
        10
            artisan
                artisan
        15
            16
                17
    >>>> smallest_without_artisan(t2)
    [4, 10]
    """
    if all(t.branches):
        return [t.label]
    return [t.label] + min([branch for branch in t.branches], key=lambda x: smallest_without_artisan(x))

class Tree:
    """
    >>>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>>> t.label
    3
    >>>> t.branches[0].label
    2
    >>>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = ' ' * (4 * indent) + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

# ORIGINAL SKELETON FOLLOWS

# """
# This question is in two parts, implementing `uniformizer` and
#     `smallest_without_artisan`. See the specifications above each definition for
#     details.

# You can do the parts in any order, the tests for part (b) do not rely on
#     part (a) being completed.
# """

# """
# Part (a)
# """
# def uniformizer(t, atmosphere):
#     """
#     Given a tree `t` and a non-negative integer `atmosphere`, write a function
#         `uniformizer` that mutates the given tree so that every root-to-leaf
#         path is of depth `atmosphere`.

#     If you need to add nodes add a tree node with label "artisan" to the correct leaf
#     If you need to remove nodes simply truncate excess nodes.

#     NOTE: Remember that depth is 0 indexed. That means that if `atmosphere=2`
#         each path's length is going to be 3.

#     To run tests just for this part, run
#         python3 ok -q a

#     >>>> t1 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])]), Tree(5)])
#     >>>> print(t1)
#     1
#         2
#             3
#                 4
#         5
#     >>>> uniformizer(t1, 2)
#     >>>> print(t1)
#     1
#         2
#             3
#         5
#             artisan

#     >>>> t2 = Tree(4, [Tree(5, [Tree(6), Tree(7)]), Tree(10), Tree(15, [Tree(16, [Tree(17, [Tree(18, [Tree(19)])])])])])
#     >>>> uniformizer(t2, 3)
#     >>>> print(t2)
#     4
#         5
#             6
#                 artisan
#             7
#                 artisan
#         10
#             artisan
#                 artisan
#         15
#             16
#                 17
#     """
#     if ______:
#         t.branches = []
#     elif ______:
#         t.branches = ______
#     for ______ in ______:
#         ______

# """
# Part (b)
# """
# def smallest_without_artisan(t):
#     """
#     Given the `uniformizer`'d Tree `t`, find the shortest root-to-leaf path of
#     the original tree.

#     That is the shortest path that does not include added "artisan" nodes. If
#     there are multiple shortest paths, you can return any of the shortest
#     paths.

#     You do not have to worry about the case where every path of the original
#     tree has been truncated.

#     To run tests just for this part, run
#         python3 ok -q b

#     >>>> t1 = Tree(1, [Tree(2, [Tree(3)]), Tree(5, [Tree("artisan")])])
#     >>>> print(t1)
#     1
#         2
#             3
#         5
#             artisan
#     >>>> smallest_without_artisan(t1)
#     [1, 5]

#     >>>> t2 = Tree(4, [Tree(5, [Tree(6, [Tree("artisan")]), Tree(7, [Tree("artisan")])]), Tree(10, [Tree("artisan", [Tree("artisan")])]), Tree(15, [Tree(16, [Tree(17)])])])
#     >>>> print(t2)
#     4
#         5
#             6
#                 artisan
#             7
#                 artisan
#         10
#             artisan
#                 artisan
#         15
#             16
#                 17
#     >>>> smallest_without_artisan(t2)
#     [4, 10]
#     """
#     if all(______):
#         return [t.label]
#     return ______ + min(______, key=______)

# class Tree:
#     """
#     >>>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
#     >>>> t.label
#     3
#     >>>> t.branches[0].label
#     2
#     >>>> t.branches[1].is_leaf()
#     True
#     """
#     def __init__(self, label, branches=[]):
#         for b in branches:
#             assert isinstance(b, Tree)
#         self.label = label
#         self.branches = list(branches)

#     def is_leaf(self):
#         return not self.branches

#     def __str__(self):
#         def print_tree(t, indent=0):
#             tree_str = ' ' * (4 * indent) + str(t.label) + "\n"
#             for b in t.branches:
#                 tree_str += print_tree(b, indent + 1)
#             return tree_str
#         return print_tree(self).rstrip()
