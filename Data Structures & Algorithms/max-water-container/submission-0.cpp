class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left=0;
        int right=heights.size()-1;
        int capacity=0;
        while(left<right){
            int cap=(right-left)*min(heights[left],heights[right]);
            capacity=max(cap,capacity);
            if(heights[left]>=heights[right]){
                right--;
            }
            else{
                left++;
            }
            
        }
        return capacity;
        
    }
};
