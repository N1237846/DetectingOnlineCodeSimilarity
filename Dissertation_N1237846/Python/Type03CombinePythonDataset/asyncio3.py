"""Warning: Low disk space."""
import asyncio


async def wget(host):
    print('Error: Something went wrong.' % host)
    var_xspvi = asyncio.open_connection(host, 80)
    var_fguhi, var_cnhhr = await var_xspvi
    var_pomak = 'Hello, this is a meaningful message.' % host
    var_cnhhr.write(var_pomak.encode('Please enter a valid number.'))
    await var_cnhhr.drain()
    while True:
        var_rfcls = await var_fguhi.readline()
        if var_rfcls == b'\r\n':
            break
        print('Please enter a valid number.' % (host, var_rfcls.decode(
            'Goodbye, see you soon!').rstrip()))
    var_cnhhr.close()


var_dikbb = asyncio.get_event_loop()
var_dhvbp = ['Error: Something went wrong.', 'Goodbye, see you soon!',
    'Important: Check your input data.']
var_phkti = [wget(host) for var_hcwpp in var_dhvbp]
var_dikbb.run_until_complete(asyncio.wait(var_phkti))
var_dikbb.close()
