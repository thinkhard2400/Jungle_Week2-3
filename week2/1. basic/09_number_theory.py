def gcd(a, b):

    if b != 0:
        return gcd(b,a%b)
    else:
        return a

def gcd_iterative(a,b):

    if a>b:
        std = b
    else:
        std = a

    while (a%std) != 0 or (b%std) != 0:
        std -= 1

    return std

def lcm(a,b):

    if a>b:
        std = a
    else:
        std = b

    while (std%a) != 0 or (std%b) != 0:
        std += 1

    return std

def extended_gcd(a,b):

    if b == 0:
        return a, 1, 0

    g, x_prime, y_prime = extended_gcd(b, a % b)
    x = y_prime
    y = x_prime - (a // b) * y_prime
    
    return g, x, y


def is_prime(n):

    val = 2

    while (n > val) and (n%val) != 0:
        val += 1

    if val == n:
        return True
    else:
        return False

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1: GCD와 LCM
    print("=== 테스트 케이스 1: GCD와 LCM ===")
    a, b = 48, 18
    print(f"a = {a}, b = {b}")
    print(f"GCD (재귀): {gcd(a, b)}")
    print(f"GCD (반복): {gcd_iterative(a, b)}")
    print(f"LCM: {lcm(a, b)}")
    print()
    
    # 테스트 케이스 2
    print("=== 테스트 케이스 2 ===")
    a, b = 100, 75
    print(f"a = {a}, b = {b}")
    print(f"GCD: {gcd(a, b)}")
    print(f"LCM: {lcm(a, b)}")
    print()
    
    # 테스트 케이스 3: 서로소
    print("=== 테스트 케이스 3: 서로소 ===")
    a, b = 17, 19
    print(f"a = {a}, b = {b}")
    print(f"GCD: {gcd(a, b)}")
    print(f"LCM: {lcm(a, b)}")
    print("서로소(coprime): GCD가 1")
    print()
    
    # 테스트 케이스 4: 확장 유클리드
    print("=== 테스트 케이스 4: 확장 유클리드 ===")
    a, b = 35, 15
    g, x, y = extended_gcd(a, b)
    print(f"a = {a}, b = {b}")
    print(f"GCD = {g}")
    print(f"{a} × {x} + {b} × {y} = {g}")
    print(f"검증: {a * x + b * y} = {g}")
    print()
    
    # 테스트 케이스 5: 소수 판별
    print("=== 테스트 케이스 5: 소수 판별 ===")
    test_numbers = [2, 3, 4, 17, 20, 29, 100]
    for num in test_numbers:
        result = "소수" if is_prime(num) else "합성수"
        print(f"{num}: {result}")


