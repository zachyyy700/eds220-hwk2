OK_FORMAT = True

test = {   'name': 'q8',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> def test_q8(student_data):\n'
                                               '...     student_df = pd.DataFrame(student_data)\n'
                                               "...     possible_answers = ['data/t2_q8_df.csv', 'data/t2_q8_sorted_inc_df.csv', 'data/t2_q8_sorted_dec_df.csv']\n"
                                               '...     for answer_file in possible_answers:\n'
                                               "...         expected_data = pd.read_csv(answer_file, index_col='Region')\n"
                                               '...         try:\n'
                                               '...             pd.testing.assert_frame_equal(expected_data, student_df)\n'
                                               '...             return\n'
                                               '...         except AssertionError:\n'
                                               '...             continue\n'
                                               "...     raise AssertionError('Incorrect answer.')\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
