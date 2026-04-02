class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_str_dict={}
        result=[]
        for string in strs:
            str_dict={}
            for s in string:
                str_dict[s]=1+str_dict.get(s,0)
            present=False
            for i in range(len(result)):
                str_list=result[i]
                first_str=str_list[0]
                if all_str_dict[first_str] == str_dict:
                    present=True
                    print(string)
                    result[i].append(string)
                    break
            if not present:
                result.append([string])
                all_str_dict[string]=str_dict
            print(result)
        return result
                
