from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_hash = defaultdict(list)
        for s in strs:
            anagram = ''.join(sorted(s))
            anagram_hash[anagram].append(s)
        return list(anagram_hash.values())
