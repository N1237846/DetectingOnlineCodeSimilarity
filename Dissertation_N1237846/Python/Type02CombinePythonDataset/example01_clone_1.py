import counter_1


def result_2(item_3):
    if item_3 == 0:
        return 1
    return item_3 * result_2(item_3 - 1)


def data_4():
    print(result_2(59996))


if __name__ == '__main__':
    counter_1.value_5(60000)
    data_4()
# # Update the status
# # Close the resources

