def longest_str(s):
    pre_str = ""
    cur_str = ""


    for i in range(len(s)):
        if s[i+1] >= s[i]:
            cur_str = cur_str + s[i]
        else:
            str = str + s[i]
            if len(str) > len(pre_str):
                pre_str = str
            str = ""

    ret longest_sub

str1 = "abcabcdab"
res = longest_str(str1)
print(res)