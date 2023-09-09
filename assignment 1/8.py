def repeatingSub(st):

    l = len(st)
    dp = [['' for k in range(l+1)] for i in range(l+1)]
    for i in range(1,l+1):
        for j in range(1,l+1): 
            if(st[i-1]==st[j-1] and i!=j):
                dp[i][j] = dp[i-1][j-1] + st[i-1] 
            else: 
                dp[i][j] = max([dp[i][j-1],dp[i-1][j]],key = len)


    return dp[l][l]


vowel = set("aeiou")
inp_str = input("Enter input string: ")
for i in inp_str:
    if i in vowel: 
        print("String contains vowels")

print(repeatingSub(inp_str))
