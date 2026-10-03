class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Hashmap = {}
        for i in strs:
            count = [0]*26
            for c in i:
                count[ord(c)-ord('a')] +=1
            if tuple(count) not in Hashmap:
                Hashmap[tuple(count)]=[i]
            else:
                Hashmap[tuple(count)].append(i)

        return list(Hashmap.values())
