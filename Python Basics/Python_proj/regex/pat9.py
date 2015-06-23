from pattern1 import test_patterns


test_patterns('abbaaabbbbaaaaa',
              [r'a((a+)|(b+))', # 'a' followed by a sequence of 'a' or sequence of 'b'
               r'a((a|b)+)',    # 'a' followed by a sequence of 'a' or 'b'
               ])