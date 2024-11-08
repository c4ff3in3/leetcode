#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> match;

        // O(n) loop over nums
        for (int num : nums) {
            if (match.count(num) > 0) {
                return true;
            } 
            match.insert(num);
        }
        return false;
    }
};