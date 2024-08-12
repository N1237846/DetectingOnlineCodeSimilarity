def cloned_merge(cloned_items1, cloned_items2):
    cloned_items3 = []
    cloned_index1, cloned_index2 = 0, 0
    while cloned_index1 < len(cloned_items) and cloned_index2 < len(cloned_items2):
        if cloned_items[cloned_index1] < cloned_items2[cloned_index2]:
            cloned_items3.cloned_append(cloned_items1[cloned_index1])
            cloned_index1 += 1
        else:
            cloned_items3.cloned_append(cloned_items2[cloned_index2])
            cloned_index2 += 1