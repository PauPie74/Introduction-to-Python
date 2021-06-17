def map_list(list1, list2):
    i = 0
    map_list = {}
    while i != len(list1):
        map_list[list1[i]] = list2[i]
        i += 1
    return map_list