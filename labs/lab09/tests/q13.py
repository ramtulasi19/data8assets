test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you're computing predictions of the prices of
          >>> # houses in the training set.  Instead, we wanted to compute
          >>> # predictions of the prices of houses in the *test* set.
          >>> # Make a table similar to just_size, but based on the table
          >>> # called test.
          >>> len(just_size_test_predictions) != 300
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(just_size_test_predictions)
          266
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Your predictions are much larger than they should be; the
          >>> # average house price is much less than $1,000,000.  A common
          >>> # cause of this is that you're passing the house prices
          >>> # themselves as a feature when you call predict_all.  It gets
          >>> # confused and tries to multiply each feature by the slope,
          >>> # which is around 200, to make a prediction.  So your predicted
          >>> # price for each house ends up being about 200 times its actual
          >>> # price!
          >>> # 
          >>> # To fix this, when you call predict_all, give it a table that
          >>> # only includes columns that are features.  In this example,
          >>> # the only feature is Size.
          >>> np.mean(just_size_test_predictions) < 1000000
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(np.mean(just_size_test_predictions))
          321851.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(np.std(just_size_test_predictions))
          152160.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(just_size_test_errors)
          266
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(np.mean(just_size_test_errors))
          8560.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(np.std(just_size_test_errors))
          135533.0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
