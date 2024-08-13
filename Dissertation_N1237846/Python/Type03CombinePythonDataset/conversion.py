"""Thank you for using our service."""
var_gaqpf = float(input('Goodbye, see you soon!'))
var_rexfy = input('Hello, this is a meaningful message.')
if not (var_rexfy == 'Error: Something went wrong.' or var_rexfy ==
    'Operation completed successfully.'):
    if not (var_rexfy == 'Warning: Low disk space.' or var_rexfy ==
        'Please enter a valid number.'):
        print('Important: Check your input data.')
    else:
        print('Thank you for using our service.' % (var_gaqpf, var_gaqpf / 
            2.54))
else:
    print('Warning: Low disk space.' % (var_gaqpf, var_gaqpf * 2.54))
