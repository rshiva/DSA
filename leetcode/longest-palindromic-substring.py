class Solution:
    def longestPalindrome(self, s: str) -> str:
        str_array = [i for i in s]
        str_array_len = len(str_array)
        if str_array_len == 0:
          return ""
        final_str = ""
        temp_str = ""
        for j in range(0, str_array_len):
          print("j",str_array[j])
          for i in range(j, str_array_len):
            if str_array[i] in temp_str:
              temp_str += str_array[i]
              if ((temp_str == temp_str[::-1]) and len(temp_str) > len(final_str)):
                final_str = temp_str
            else:
              temp_str += str_array[i]
          if len(final_str) >= len(str_array[j:]):
            break
          temp_str = ""
        if (len(final_str) == 0 and str_array_len > 0):
          return str_array[0] 
        else:
          return final_str 


pali="qbmhukucteihghldwdobtvgwwnhflpceiwhbkmvxavmqxedfndegztlpjptpdowwavemasyrjxxnhldnloyizyxgqlhejsdylvkpdzllrzoywfkcamhljminikvwwvqlerdilrdgzifojjlgeayprejhaequyhcohoeonagsmfrqhfzllobwjhxdxzadwxiglvzwiqyzlnamqqsastxlojpcsleohgtcuzzrvwzqugyimaqtorkafyebrgmrfmczwiexdzcokbqymnzigifbqzvfzjcjuugdmvegnvkgbmdowpacyspszvgdapklrhlhcmwkwwqatfswmxyfnxkepdotnvwndjrcclvewomyniaefhhcqkefkyovqxyswqpnysafnydbiuanqphfhfbfovxuezlovokrsocdqrqfzbqhntjafzfjisexcdlnjbhwrvnyabjbshqsxnaxhvtmqlfgdumtpeqzyuvmbkvmmdtywquydontkugdayjqewcgtyajofmbpdmykqobcxgqivmpzmhhcqiyleqitojrrsknhwepoxawpsxcbtsvagybnghqnlpcxlnshihcjdjxxjjwyplnemojhodksckmqdvnzewhzzuswzctnlyvyttuhlreynuternbqonlsfuchxtsyhqlvifcxerzqepthwqrsftaquzuxwcmjjulvjrkatlfqshpyjsbaqwawgpabkkjrtchqmriykbdsxwnkpaktrvmxjtfhwpzmieuqevlodtroiulzgbocrtiuvpywtcxvajkpfmaqckgrcmofkxynjxgvxqvkmhdbvumdaprijkjxxvpqnxakiavuwnifvyfolwlekptxbnctjijppickuqhguvtoqfgepcufbiysfljgmfepwyaxusvnsratn"
pali = "bbabad"
s=Solution()
print(s.longestPalindrome(pali))




# st ="bbabad"
# st= "bbb"

# st = "babad"
# st ="bbabad"
# s=Solution()
# s.longestPalindrome(st)