#include <map>
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int,int> countmap;//maps num to count
        multimap<int,int,greater<int>> mapcount;//maps count to num
        for(int i=0;i<nums.size();i++){
            if(countmap.find(nums[i])==countmap.end()){
                countmap[nums[i]]=1;
            }
            else{
            countmap[nums[i]]++;   }
        }
        for(const auto& pair:countmap){
            mapcount.insert({pair.second,pair.first});
        }
        vector<int> res;
        auto it=mapcount.begin();
        for(int i=0;i<k&&it!=mapcount.end();i++){
          res.push_back(it->second);
          it++;
        }
        return res;

        
    }
};
