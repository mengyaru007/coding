"""合并两个有序链表"""

def merge_two_lists(list1, list2):
    if not list1: return list2
    elif not list2: return list1
    elif list1.value < list2.value:
        list1.next = merge_two_lists(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists(list1, list2.next)
        return list2