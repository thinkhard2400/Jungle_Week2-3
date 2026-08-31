def combinations(n: int, k: int) -> list:

    result = []  # 완성된 조합을 모아 둘 곳

    def backtrack(start: int, current_combination: list) -> None:

        if len(current_combination) == k:
            result.append(list(current_combination))
            return

        for num in range(start, n+1):
            current_combination.append(num)
            backtrack(num+1, current_combination)
            current_combination.pop()
    backtrack(1, [])
    return result


# ============================================================================
# (이 함수는 직접 채울 필요 없음 — itertools 로 만든 비교/검증용 정답)
# ============================================================================
def combinations_itertools_compare(n: int, k: int) -> list:
    """파이썬 표준 라이브러리로 만든 동일 결과 (정답 비교용)"""
    from itertools import combinations as comb
    return [list(c) for c in comb(range(1, n + 1), k)]


# ============================================================================
# 테스트 케이스
# ============================================================================
if __name__ == "__main__":
    # 테스트 케이스 1
    print("=== 테스트 케이스 1 ===")
    n1, k1 = 4, 2
    result1 = combinations(n1, k1)
    print(f"C({n1}, {k1}) = {result1}")
    print(f"총 {len(result1)}개의 조합")
    print()

    # 테스트 케이스 2
    print("=== 테스트 케이스 2 ===")
    n2, k2 = 5, 3
    result2 = combinations(n2, k2)
    print(f"C({n2}, {k2}) = {result2}")
    print(f"총 {len(result2)}개의 조합")
    print()

    # 테스트 케이스 3
    print("=== 테스트 케이스 3 ===")
    n3, k3 = 3, 1
    result3 = combinations(n3, k3)
    print(f"C({n3}, {k3}) = {result3}")
    print(f"총 {len(result3)}개의 조합")
    print()

    # 테스트 케이스 4
    print("=== 테스트 케이스 4 ===")
    n4, k4 = 4, 4
    result4 = combinations(n4, k4)
    print(f"C({n4}, {k4}) = {result4}")
    print(f"총 {len(result4)}개의 조합")
