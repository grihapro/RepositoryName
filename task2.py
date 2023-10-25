def find_common_participants(string1, string2, space=','):
    _list1 = string1.split(space)
    _list2 = string2.split(space)
    _set = set(_list1)
    set_common = _set.intersection(_list2)
    list_common = list(set_common)
    list_common.sort()
    return list_common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))

