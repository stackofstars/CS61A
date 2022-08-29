test = {
  'name': 'q0',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert mc_result_pyfeatures in ['Lazy Evaluation', 'Coroutines', 'Functions', 'Memory Management'], 'Selected an invalid option'
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q0 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> assert mc_result_languages in ['A program that transforms code from one language to equivalent code in another language', 'A program that transforms compiled code from one operating system to another', 'A program that converts an interpreter into a compiler', "Another way of saying 'compiler'"], 'Selected an invalid option'
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q0 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> assert mc_result_neural_networks in ['Using high-dimensional space', 'Finding features', 'Being an inference tool', 'Approximating nonlinear relationships'], 'Selected an invalid option'
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q0 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> assert mc_result_machine_learning in ['Determine f(x)', 'Determine f', 'Determine x'], 'Selected an invalid option'
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q0 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
