def cloned_main():
    cloned_persons = [True] * 30
    cloned_counter = 0
    cloned_index = 0
    cloned_number = 0
    while cloned_counter < 15:
        if cloned_persons[cloned_index]:
            cloned_number += 1
            if cloned_number == 9:
                cloned_persons[cloned_index] = False
                cloned_number = 0
                cloned_counter += 1
        cloned_index += 1
        cloned_index %= len(cloned_persons)
    for cloned_person in cloned_persons:
	    print('基' if cloned_person else '非', cloned_end='')
    print()


if __name__ == '__main__':
    cloned_main()
