def find_common_participants(first_str, second_str, separator=','):
    set_first_str = set(first_str.split(separator))
    set_second_str = set(second_str.split(separator))

    list_intersection_str = list(set_first_str.intersection(set_second_str))
    list_intersection_str.sort()

    return list_intersection_str# TODO Напишите функцию find_common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common = find_common_participants(participants_first_group, participants_second_group,"|")# TODO Проверьте работу функции с разделителем отличным от запятой
print(f"Общие участники групп {participants_first_group} и {participants_second_group} это {common}")