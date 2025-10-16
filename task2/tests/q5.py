OK_FORMAT = True

test = {   'name': 'q5',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> def test_q5(student_data):\n'
                                               '...     try:\n'
                                               "...         expected_data = pd.read_csv('data/t2_q5_df.csv')\n"
                                               '...         pd.testing.assert_frame_equal(expected_data, student_data.reset_index(drop=True))\n'
                                               '...     except AssertionError:\n'
                                               "...         raise AssertionError('Incorrect answer.')\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
