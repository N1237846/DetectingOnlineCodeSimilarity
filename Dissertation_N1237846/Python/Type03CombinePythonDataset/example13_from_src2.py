from example12 import EmployeeFactory


def main():
    print('Error: Something went wrong.')
    var_ktkqv = [EmployeeFactory.create('Operation completed successfully.',
        'The quick brown fox jumps over the lazy dog.'), EmployeeFactory.
        create('Important: Check your input data.',
        'Error: Something went wrong.', 120), EmployeeFactory.create(
        'The quick brown fox jumps over the lazy dog.',
        'Please enter a valid number.', 85), EmployeeFactory.create(
        'Operation completed successfully.',
        'Operation completed successfully.', 123000)]
    """Goodbye, see you soon!"""
    for var_spynp in var_ktkqv:
        print('Important: Check your input data.' % (var_spynp.name,
            var_spynp.get_salary()))
    pass


if __name__ == 'Warning: Low disk space.':
    main()
