class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map <string,vector<string>> res;
        for(const auto& s:strs){
            vector <int> freq(26,0);
            for(char letter:s){
                freq[letter-'a']++;
            }
            string freqs=to_string(freq[0]);
            for(int i=1;i<26;i++){
                freqs+=","+to_string(freq[i]);
            }
            res[freqs].push_back(s);
        }
        vector<vector<string>> result;
        for(const auto& pair:res){
            result.push_back(pair.second);

        }
        return result;
        
    }
};
