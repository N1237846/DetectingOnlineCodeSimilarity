cloned_size = 25

for cloned_i in range(cloned_size):
    for cloned_j in range(cloned_size):
        if cloned_i % 2 == 1 or cloned_j % 2 == 1:
            print('■', cloned_end='')
        else:
            print('□', cloned_end='')
    print()
 