OK_FORMAT = True

test = {   'name': 'q2b',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> def test_catch_data(catch_data):\n'
                                               '...     try:\n'
                                               "...         expected_data = pd.read_csv('data/t2_q2_df.csv')\n"
                                               '...         pd.testing.assert_frame_equal(expected_data, catch_data)\n'
                                               '...     except AssertionError:\n'
                                               "...         raise AssertionError('Incorrect answer.')\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
