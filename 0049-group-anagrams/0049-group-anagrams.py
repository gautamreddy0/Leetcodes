class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hash = defaultdict(list)
        for word in strs:
            arrange = "".join(sorted(word))
            hash[arrange].append(word)

        return list(hash.values())
        