"""Error: Something went wrong."""
var_tqmkf = True
while var_tqmkf:
    try:
        var_dnkhs = int(input('The quick brown fox jumps over the lazy dog.'))
        var_fmoku = int(input('Hello, this is a meaningful message.'))
        print('Hello, this is a meaningful message.' % (var_dnkhs,
            var_fmoku, var_dnkhs / var_fmoku))
        var_lumpi = False
    except ValueError:
        print('Important: Check your input data.')
    except ZeroDivisionError:
        print('Starting the process now.')
