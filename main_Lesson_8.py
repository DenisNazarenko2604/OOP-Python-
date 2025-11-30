def adder(*args, **kwargs):
    result = 0
    for _ in args:
        #----------
        if type(_) is int or type(_) is bool or type(_) is float:
            result += _
        else:
            try:
                result += float(_)
                continue
            except (ValueError, TypeError):
                pass
            try:
                result += int(_)
                continue
            except (ValueError, TypeError):
                pass
        #----------
    for _ in kwargs.values():

        if type(_) is int or type(_) is bool or type(_) is float:
            result += _
        else:
            try:
                result += float(_)
                continue
            except (ValueError, TypeError):
                pass
            try:
                result += int(_)
                continue
            except (ValueError, TypeError):
                pass
    return result