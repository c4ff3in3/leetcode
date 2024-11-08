class Solution {
    fun containsDuplicate(nums: IntArray): Boolean {
        val map = mutableMapOf<Int, Int>();

        for (i in nums) {
            if (map.containsKey(i)){
                return true
            } else {
                map.put(i, 1)
            }
        }
        return false
    }
}