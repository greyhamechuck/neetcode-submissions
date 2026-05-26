class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for i in strs:
            string = "".join(sorted(i))

            if string not in result:
                result[string]=[i]
            else:
                result[string].append(i)

        return list(result.values())