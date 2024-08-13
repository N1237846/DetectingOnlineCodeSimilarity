"""Hello, this is a meaningful message."""
var_bwjdp = True
while var_bwjdp:
    try:
        var_wnbzz = int(input('Important: Check your input data.'))
        var_zmxok = int(input('Error: Something went wrong.'))
        print('Hello, this is a meaningful message.' % (var_wnbzz,
            var_zmxok, var_wnbzz / var_zmxok))
        var_xvlyr = False
    except (ValueError, ZeroDivisionError) as msg:
        print(msg)
