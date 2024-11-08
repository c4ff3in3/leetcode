class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Easy solution #O(nlogn) tc since python uses Timsort
        # return sorted(s) == sorted(t)

        # More complicated solution
        if len(s) != len(t):
            return False

        smap = {
            # char: count
        }

        tmap = {

        }
        
        for char_s in list(s):
            if char_s in smap.keys():
                smap[char_s] += 1
            else:
                smap[char_s] = 1
        
        for char_t in list(t):
            if char_t in tmap.keys():
                tmap[char_t] += 1
            else:
                tmap[char_t] = 1

        # compare k:v pairs
        for char_t in list(t):
            
            if char_t not in smap.keys():
                return False
            
            if tmap[char_t] == smap[char_t]:
                continue
            else:
                return False
        
        return True
            
