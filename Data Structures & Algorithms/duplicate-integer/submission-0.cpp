class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int n= nums.size();
        unordered_set<int> se;
        for(int i=0;i<n;i++){
            if(se.find(nums[i])!=se.end()){
                return true;
            }
            se.insert(nums[i]);
        }
        return false;

    }
};
