from pattern import test_patterns

test_patterns('abbaaabbbbaaaaa',
              [ 'ab*',     # a followed by zero or more b
                'ab+',     # a followed by one or more b
                'ab?',     # a followed by zero or one b
                'ab{3}',   # a followed by three b
                'ab{2,3}', # a followed by two to three b
                ])

