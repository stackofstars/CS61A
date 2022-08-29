test = {
  'name': 'a',
  'points': 0.1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> t3 = Tree(10, [Tree(20), Tree(30, [Tree(50)]), Tree(40, [Tree(70)])])
          
          >>> uniformizer(t3, 4)
          
          >>> print(t3)
          10
              20
                  artisan
                      artisan
                          artisan
              30
                  50
                      artisan
                          artisan
              40
                  70
                      artisan
                          artisan
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
