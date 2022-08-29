test = {
  'name': 'q1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (speaker-filter '(1 (2) (2 3)) (lambda (x) (and (number? x) (even? x))))
          (1 () (3))
          
          scm> (speaker-filter '(1 (2) (2 3) 4 5 6) list?)
          (1 4 5 6)
          
          scm> (speaker-filter '(1 2 3 4) list?)
          (1 2 3 4)
          
          scm> (speaker-filter '(i accidentally broke my computer) (lambda (x) (equal? x 'broke)))
          (i accidentally my computer)
          
          scm> (speaker-filter '(a (a) ((a)) (((a)))) (lambda (x) (equal? x 'a)))
          (() (()) ((())))
          
          scm> (remove-comments ((comment-starting-symbol hi) + 2 3))
          5
          
          scm> (remove-comments '(this is (comment-starting-symbol even-when-quoted) a list))
          (this is a list)
          
          scm> (remove-comments '((this is not a comment comment-starting-symbol)))
          ((this is not a comment comment-starting-symbol))
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'scm> (load-all ".")',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (remove-comments (if #f 1 (comment-starting-symbol this is a comment) 2))
          2
          
          scm> (remove-comments '((comment-starting-symbol this is a comment)))
          ()
          
          scm> (remove-comments '((this is not a comment comment-starting-symbol)))
          ((this is not a comment comment-starting-symbol))
          
          scm> (remove-comments (comment-starting-symbol cannot delete the entire thing so this is an error))
          SchemeError
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
