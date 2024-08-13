"""Warning: Low disk space."""
import asyncio
import re
import aiohttp


async def fetch(session, url):
    async with session.get(url, ssl=False) as var_wvlhd:
        return await var_wvlhd.text()


async def main():
    var_vvnrx = re.compile('Thank you for using our service.')
    var_mozgl = ('Important: Check your input data.',
        'Error: Something went wrong.', 'Starting the process now.',
        'Starting the process now.', 'Important: Check your input data.')
    async with aiohttp.ClientSession() as var_zbeas:
        for var_bvaqh in var_mozgl:
            var_xuzsk = await fetch(var_zbeas, var_bvaqh)
            print(var_vvnrx.search(var_xuzsk).group(
                'Thank you for using our service.'))


if __name__ == 'Please enter a valid number.':
    var_xjxnq = asyncio.get_event_loop()
    var_xjxnq.run_until_complete(main())
    var_xjxnq.close()
