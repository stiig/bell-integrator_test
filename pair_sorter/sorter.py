def join_ints(number_list):
    return ''.join(str(n) for n in number_list)


def split_every(number, number_list):
    number_list = join_ints(number_list)
    return [int(number_list[i:i + number]) for i in
            range(0, len(number_list), number) if len(number_list) >= i + number]


def change_places(el1, el2):
    div, mod = divmod((el2 - el1), 22)
    if div == -1 and mod == 0:
        return True
    return False


def number_changer(number_list):
    for el1 in number_list[:-1]:
        for el2 in number_list[1:]:
            if el1 == el2:
                continue
            if change_places(el1, el2):
                print('{} {}<->{}'.format(join_ints(number_list),
                                          number_list[number_list.index(el2)],
                                          number_list[number_list.index(el1)]))
                number_list[number_list.index(el2)], \
                number_list[number_list.index(el1)] = \
                    number_list[number_list.index(el1)], \
                    number_list[number_list.index(el2)]
                break


def validate_number_list(number):
    if len(number) > len(set(number)):
        return False

    number = split_every(2, number)

    return its_normal_number(number)


def its_normal_number(number_list):
    flag = True
    for el1 in number_list:
        for el2 in number_list:
            if (el1 - el2) % 22 != 0 and el1 != el2:
                flag = False
    return flag


def sort_pair(number):
    number_list = split_every(2, number)
    number_list2 = split_every(2, number[1:])

    if its_normal_number(number_list):
        number_changer(number_list)
        number = join_ints(number_list)
    else:
        print('{} {}<->{}'.format(join_ints(number), number_list2[0], number_list2[1]))
        number_list2.reverse()
        number = str(number[0]) + ''.join(str(el) for el in number_list2) + str(number[-1])

    if not validate_number_list(number):
        return 'Invalid number'

    if number != '123456':
        number = sort_pair(number)
    return number


if __name__ == '__main__':
    assert sort_pair([1, 2, 3, 4, 5, 6]), '123456'
    assert sort_pair([1, 2, 5, 6, 3, 4]), '123456'
    assert sort_pair([3, 4, 1, 2, 5, 6]), '123456'
    assert sort_pair([3, 4, 5, 6, 1, 2]), '123456'
    assert sort_pair([5, 6, 3, 4, 1, 2]), '123456'
    assert sort_pair([5, 6, 1, 2, 3, 4]), '123456'

    assert sort_pair([1, 4, 5, 2, 3, 6]), '123456'
    assert sort_pair([1, 6, 3, 2, 5, 4]), '123456'
    assert sort_pair([3, 2, 5, 4, 1, 6]), '123456'
    assert sort_pair([3, 6, 1, 4, 5, 2]), '123456'
    assert sort_pair([5, 4, 1, 6, 3, 2]), '123456'
    assert sort_pair([5, 2, 3, 6, 1, 4]), '123456'
