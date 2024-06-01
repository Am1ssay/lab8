def str_hint(str1, str2):
    s1, s2 = len(str1), len(str2)
    dp = [[0] * (s2 + 1) for _ in range(s1 + 1)]

    for i in range(s1 + 1):
        dp[i][0] = i

    for j in range(s2 + 1):
        dp[0][j] = j

    for i in range(1, s1 + 1):
        for j in range(1, s2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1],
                                   dp[i - 1][j - 1])

    return dp[s1][s2]


if __name__ == "__main__":
    str1 = input()
    str2 = input()
    print(str_hint(str1, str2))
