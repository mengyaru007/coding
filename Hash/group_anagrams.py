"""字母异位词分组"""
import collections


def group_anagrams(strs):
    strs_hash = collections.defaultdict(list)
    for st in strs:
        counts = [0] * 26
        for ch in st:
            counts[ord(ch) - ord('a')] += 1
        # 字典的键是不可变类型，故要转换为元组
        strs_hash[tuple(counts)].append(st)
    return list(strs_hash.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))