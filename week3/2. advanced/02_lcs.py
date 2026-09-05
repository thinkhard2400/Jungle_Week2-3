def lcs_length(s1, s2):

    if len(s1) == 0 or len(s2) == 0:
        return 0

    dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[len(s1)][len(s2)]


if __name__ == "__main__":
    print("[테스트 1] 한쪽이 빈 문자열")
    print(f'  s1="", s2="abc" -> LCS 길이={lcs_length("", "abc")}')
    print()

    print("[테스트 2] 두 문자열이 동일")
    print(f'  s1="abc", s2="abc" -> LCS 길이={lcs_length("abc", "abc")}')
    print()

    print("[테스트 3] 공통 원소가 전혀 없음")
    print(f'  s1="abc", s2="xyz" -> LCS 길이={lcs_length("abc", "xyz")}')
    print()

    print("[테스트 4] 표준 예시 1")
    print(f'  s1="abcde", s2="ace" -> LCS 길이={lcs_length("abcde", "ace")}')
    print()

    print("[테스트 5] 표준 예시 2")
    print(f'  s1="AGGTAB", s2="GXTXAYB" -> LCS 길이={lcs_length("AGGTAB", "GXTXAYB")}')
    print()

    print("[테스트 6] 두 LCS 후보가 길이가 같은 경우")
    print(f'  s1="ABCBDAB", s2="BDCABA" -> LCS 길이={lcs_length("ABCBDAB", "BDCABA")}')

