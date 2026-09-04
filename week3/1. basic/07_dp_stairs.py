def climb_stairs(n):

    dp = [0,1,2]

    k = 3
    while k <= n:
        s = dp[k-1] + dp[k-2]
        dp.append(s)
        k += 1
    return dp[n]

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    print("=== 계단 오르기 ===")
    for i in range(1, 11):
        result = climb_stairs(i)
        print(f"{i}번 계단: {result}가지")
    print()
    
    # 테스트 케이스 2: 큰 수
    n = 20
    result = climb_stairs(n)
    print(f"{n}번 계단: {result}가지")
    print()
    
    # 계단별 경로 예시
    print("=== 4번 계단의 경로 ===")
    print("1. 1+1+1+1")
    print("2. 1+1+2")
    print("3. 1+2+1")
    print("4. 2+1+1")
    print("5. 2+2")