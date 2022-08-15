from data import nested_list


def flat_generator(nested_list):
    inner_count = -1
    outer_count = 0
    while True:
        if inner_count != len(nested_list[outer_count])-1:
            inner_count += 1
            yield nested_list[outer_count][inner_count]
        else:
            outer_count += 1
            inner_count = -1
        if outer_count == len(nested_list):
            break


for item in flat_generator(nested_list):
    print(item)

