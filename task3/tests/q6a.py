OK_FORMAT = True

test = {   'name': 'q6a',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> def test_q6ab(aqi_sb):\n'
                                               '...     try:\n'
                                               "...         expected_data = pd.read_csv('data/t3_q6a_df.csv')\n"
                                               '...         pd.testing.assert_frame_equal(expected_data, aqi_sb.reset_index(drop=True))\n'
                                               '...     except AssertionError:\n'
                                               "...         raise AssertionError('Incorrect answer.')\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
