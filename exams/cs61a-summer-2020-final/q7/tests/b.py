test = {
  'name': 'b',
  'points': 0.1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> t3 = Tree(10, [Tree(20, [Tree("artisan", [Tree("artisan", [Tree("artisan")])])]), Tree(30, [Tree(50, [Tree("artisan", [Tree("artisan")])])]), Tree(40, [Tree(70, [Tree("artisan", [Tree("artisan")])])])])
          
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
          
          >>> smallest_without_artisan(t3)
          [10, 20]
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
