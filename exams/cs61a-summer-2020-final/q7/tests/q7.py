test = {
  'name': 'q7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> t1 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])]), Tree(5)])
          
          >>> print(t1)
          1
              2
                  3
                      4
              5
          
          >>> uniformizer(t1, 2)
          
          >>> print(t1)
          1
              2
                  3
              5
                  artisan
          
          >>> t2 = Tree(4, [Tree(5, [Tree(6), Tree(7)]), Tree(10), Tree(15, [Tree(16, [Tree(17, [Tree(18, [Tree(19)])])])])])
          
          >>> uniformizer(t2, 3)
          
          >>> print(t2)
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
          
          >>> t1 = Tree(1, [Tree(2, [Tree(3)]), Tree(5, [Tree("artisan")])])
          
          >>> print(t1)
          1
              2
                  3
              5
                  artisan
          
          >>> smallest_without_artisan(t1)
          [1, 5]
          
          >>> t2 = Tree(4, [Tree(5, [Tree(6, [Tree("artisan")]), Tree(7, [Tree("artisan")])]), Tree(10, [Tree("artisan", [Tree("artisan")])]), Tree(15, [Tree(16, [Tree(17)])])])
          
          >>> print(t2)
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
          
          >>> smallest_without_artisan(t2)
          [4, 10]
          
          >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
          
          >>> t.label
          3
          
          >>> t.branches[0].label
          2
          
          >>> t.branches[1].is_leaf()
          True
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q7 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
