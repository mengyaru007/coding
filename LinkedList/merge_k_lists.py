"""合并k个升序链表"""
from merge_two_lists import merge_two_lists

def merge_k_lists(lists):
    k = len(lists)
    if k == 0: return None
    if k == 1: return lists[0]
    mid = k // 2
    list1 = lists[0:mid]
    list2 = lists[mid:]
    return merge_two_lists(merge_k_lists(list1), merge_k_lists(list2))