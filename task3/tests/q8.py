OK_FORMAT = True

test = {   'name': 'q8',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': ">>> pd.testing.assert_frame_equal(pd.read_csv('data/t3_q8_df.csv', index_col='date', parse_dates=True), pd.DataFrame(rolling_average))\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
