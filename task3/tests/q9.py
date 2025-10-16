OK_FORMAT = True

test = {   'name': 'q9',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> def test_q9(aqi_sb):\n'
                                               '...     try:\n'
                                               "...         expected_data = pd.read_csv('data/t3_q9_df.csv', index_col='date', parse_dates=True)\n"
                                               '...         pd.testing.assert_frame_equal(expected_data, aqi_sb)\n'
                                               '...     except AssertionError:\n'
                                               "...         raise AssertionError('Incorrect answer.')\n"
                                               '>>> test_q9(aqi_sb)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
