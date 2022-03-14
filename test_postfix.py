from postfix import postfix

def test_postfix_num():
    ret = postfix("12365+/*-")
    assert ret == 6.333333333333333

def test_postfix_alpha():
    ret = postfix("abcd")
    assert ret == None

def test_postfix_special():
    ret = postfix("@#%&")
    assert ret == None



