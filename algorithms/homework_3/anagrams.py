def anagrams(strs):
    groups = {}
    for word in strs:
        srtd = ''.join(sorted(word))
        if srtd in groups:
            groups[srtd].append(word)
        else:
            groups[srtd] = [word]
    return list(groups.values())


def normalize(groups):
    return sorted([sorted(group) for group in groups])

assert normalize(
    anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
) == normalize([
    ["bat"],
    ["nat", "tan"],
    ["ate", "eat", "tea"]
])

assert normalize(
    anagrams(["abc", "bca", "cab"])
) == normalize([
    ["abc", "bca", "cab"]
])

assert normalize(
    anagrams(["abc", "def", "ghi"])
) == normalize([
    ["abc"],
    ["def"],
    ["ghi"]
])

assert normalize(
    anagrams(["aab", "aba", "baa", "abc"])
) == normalize([
    ["aab", "aba", "baa"],
    ["abc"]
])

assert normalize(
    anagrams(["hello"])
) == normalize([
    ["hello"]
])

assert normalize(
    anagrams([])
) == []

assert normalize(
    anagrams(["", "", "a"])
) == normalize([
    ["", ""],
    ["a"]
])
