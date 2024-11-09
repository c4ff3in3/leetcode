from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # HashTable O(n) complexity
        mp = {
            # num_in_list : # count
        }
        # Runtime: O(n)
        for i in nums:
            if i not in mp.keys():
                mp[i] = 1
            else:
                return True

        return False
