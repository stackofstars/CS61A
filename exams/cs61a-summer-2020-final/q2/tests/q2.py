test = {
  'name': 'q2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> salmon1 = Link(0, Link(1, Link(2, Link(3,  Link(5, Link(9))))))
          
          >>> salmon2 = Link(1, Link(4))
          
          >>> platform([salmon1, salmon2])
          Link(0, Link(2, Link(3, Link(4, Link(5, Link(9))))))
          
          >>> salmon1 # unchanged
          Link(0, Link(1, Link(2, Link(3, Link(5, Link(9))))))
          
          >>> salmon2 # unchanged
          Link(1, Link(4))
          
          >>> salmon1 = Link(0, Link(1, Link(2, Link(3,  Link(5, Link(9))))))
          
          >>> salmon2 = Link(1, Link(4))
          
          >>> platform([salmon1, salmon1, salmon2])
          Link(1, Link(4))
          
          >>> salmon3 = Link(0, Link(1, Link(2, Link(3,  Link(5, Link(9))))))
          
          >>> salmon4 = Link(1, Link(2, Link(3,  Link(5, Link(9)))))
          
          >>> platform([salmon3, salmon4])
          Link(0)
          
          >>> platform([salmon1, salmon2, salmon3, salmon4])
          Link(2, Link(3, Link(4, Link(5, Link(9)))))
          
          >>> s = Link(1, Link(2, Link(3, Link(4))))
          
          >>> len(s)
          4
          
          >>> s[2]
          3
          
          >>> s
          Link(1, Link(2, Link(3, Link(4))))
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q2 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> platform([Link(1), Link(2), Link(3), Link(4), Link(5)])
          Link(1, Link(2, Link(3, Link(4, Link(5)))))
          
          >>> platform([Link(1, Link(2, Link(3, Link(4, Link(5)))))])
          Link(1, Link(2, Link(3, Link(4, Link(5)))))
          
          >>> platform([Link(1), Link.empty, Link(-2, Link(3))])
          Link(-2, Link(1, Link(3)))
          
          >>> platform([Link(1), Link(1)]) is Link.empty
          True
          
          >>> platform([Link(2), Link(2, Link(3)), Link(3)]) is Link.empty
          True
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q2 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
