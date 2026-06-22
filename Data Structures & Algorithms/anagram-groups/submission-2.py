class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = []
        hmap = defaultdict(list)
        for word in strs:
            clean = "".join(sorted(word))
            hmap[clean].append(word)
            
        return list(hmap.values())