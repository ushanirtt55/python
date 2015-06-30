"""def shorter_reverse_longer(a,b):
    len_a=len(a)
    len_b=len(b)
    new_str=""
    if len_a >= len_b:
        new_str=new_str+b+a[::-1]+b
    else:
        new_str=new_str+a+b[::-1]+a
    return new_str
    """
    
def shorter_reverse_longer(a,b):
    return b + a[::-1] + b if len(a) >= len(b) else a + b[::-1] + a
a=shorter_reverse_longer("he", "bau")
print a