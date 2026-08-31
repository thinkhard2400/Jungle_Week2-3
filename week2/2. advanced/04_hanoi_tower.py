def hanoi_count(n: int) -> int:
    return 2**n - 1

def hanoi_moves(n: int) -> list:

    if n > 20 or n == 0:
        return []

    result = []

    def move(k, src, via, dst):
        if k == 0:
            return
        move(k-1, src, dst, via)
        result.append((src, dst))
        move(k-1, via, src, dst)

    move(n, 1, 2, 3)

    return result

if __name__ == "__main__":
    print("[테스트 1] N=0 (원반 없음, 옮길 것 없음)")
    print(f"  최소 이동 횟수: {hanoi_count(0)}")
    print(f"  이동 순서: {hanoi_moves(0)}")
    print()

    print("[테스트 2] N=1 (원반 1개, 1번 -> 3번 한 번)")
    print(f"  최소 이동 횟수: {hanoi_count(1)}")
    print(f"  이동 순서: {hanoi_moves(1)}")
    print()

    print("[테스트 3] N=3 (실제 이동 순서까지 출력)")
    print(f"  최소 이동 횟수: {hanoi_count(3)}")
    print("  이동 순서:")
    for s, d in hanoi_moves(3):
        print(f"    {s} -> {d}")
    print()

    print("[테스트 4] N=20 (이동 순서 반환의 상한)")
    print(f"  최소 이동 횟수: {hanoi_count(20)}")
    print(f"  이동 순서 개수: {len(hanoi_moves(20))}")
    print()

    print("[테스트 5] N=100 (큰 수 확인, 이동 순서는 미생성)")
    print(f"  최소 이동 횟수: {hanoi_count(100)}")
    print(f"  이동 순서 개수: {len(hanoi_moves(100))}")
