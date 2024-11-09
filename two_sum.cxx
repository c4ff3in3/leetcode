#include <unordered_map>
#include <vector>

using namespace std;

class Solution
{
public:
  vector<int> twoSum(vector<int> &nums, int target)
  {
    unordered_map<int, int> nm;
    int n = nums.size();

    // Build the hash table
    for (int i = 0; i < n; i++)
    {
      nm[nums[i]] = i;
    }

    // Find the complement
    for (int i = 0; i < n; i++)
    {
      int complement = target - nums[i];
      if (nm.count(complement) && nm[complement] != i)
      {
        return {i, nm[complement]};
      }
    }

    return {};
  }
};
