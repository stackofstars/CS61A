test = {
  'name': 'q5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (ladder-locator 12)
          (1 2)
          
          scm> (ladder-locator 1881)
          (1 (8) (8) 1)
          
          scm> (ladder-locator 0) ; no digits
          ()
          
          scm> (ladder-locator 88888888)
          ((8) (8) (8) (8) (8) (8) (8) (8))
          
          scm> (ladder-locator 1128651)
          (1 1 2 (8) 6 5 1)
          
          scm> (define just-city (cons-stream 'city just-city))
          just-city
          
          scm> (define two (cons-stream 1 (cons-stream 'city two)))
          two
          
          scm> (define three (cons-stream 'x (cons-stream 'y (cons-stream 'city three))))
          three
          
          scm> (take 10 two)
          (1 city 1 city 1 city 1 city 1 city)
          
          scm> (take 10 three)
          (x y city x y city x y city x)
          
          scm> (take 10 (surgery-switch two three))
          (1 x y 1 x y 1 x y 1)
          
          scm> (take 10 (surgery-switch two just-city))
          (1 1 1 1 1 1 1 1 1 1)
          
          scm> (take 10 (surgery-switch three three))
          (x y x y x y x y x y)
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'scm> (load-all ".")',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
