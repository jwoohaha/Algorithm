class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            key = ''.join(sorted(word))
            anagrams.setdefault(key, [])
            anagrams[key].append(word)
        return(list(anagrams.values()))