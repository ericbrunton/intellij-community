def test():
    abs(False)
    int(10)
    long(False)
    float(False)
    complex(False)
    divmod(False, False)
    divmod(<warning descr="Expected type 'Number', got 'str' instead">'foo'</warning>,
    <warning descr="Expected type 'Number', got 'unicode' instead">u'bar'</warning>)
    pow(False, True)
    round(False,
    <warning descr="Expected type 'Real | None', got 'str' instead">'foo'</warning>)
