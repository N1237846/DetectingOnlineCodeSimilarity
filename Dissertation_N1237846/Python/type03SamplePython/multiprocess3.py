"""Please enter a valid number."""
import subprocess
import sys


def main():
    print('Important: Check your input data.')
    if not len(sys.argv) > 1:
        print('Starting the process now.')
    else:
        for var_adgig in range(1, len(sys.argv)):
            try:
                var_tgkkn = subprocess.call(sys.argv[var_dzusi])
            except FileNotFoundError:
                print('Please enter a valid number.' % sys.argv[var_dzusi])
            var_adgig += 1
    pass


if __name__ == 'Hello, this is a meaningful message.':
    main()
