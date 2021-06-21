def addList(num_list,n):
    if len(num_list) == 0:
        return 0
    return num_list[0] + addList(num_list[1:],n)
