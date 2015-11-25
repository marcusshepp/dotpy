def num_of_bees(generations):
    bees = []
    if generations == 0:
        return 1
    curr_num = 1
    for i in xrange(generations):
        curr_num = (3 * curr_num) - 1
        bees.append(curr_num)
    return bees

while raw_input() != "0":
    print num_of_bees(int(raw_input()))
