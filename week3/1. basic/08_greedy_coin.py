def make_change_greedy(change, coins):

    result = {}
    total_coins = 0

    for coin in coins:
        result[coin] = 0

    while change > 0:
        if change >= 500:
            result[500] = (change//500)
            total_coins += (change//500)
            change -= 500*(change//500)
        elif change >= 100:
            result[100] = (change//100)
            total_coins += (change//100)
            change -= 100*(change//100)
        elif change >= 50:
            result[50] = (change//50)
            total_coins += (change//50)
            change -= 50*(change//50)
        else:
            result[10] = (change//10)
            total_coins += (change//10)
            change -= 10*(change//10)
    return total_coins, result

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    change1 = 1260
    coins1 = [500, 100, 50, 10]
    total, details = make_change_greedy(change1, coins1)
    
    print("=== 거스름돈 계산 ===")
    print(f"거슬러줄 금액: {change1}원")
    for coin, count in details.items():
        print(f"{coin}원: {count}개")
    print(f"총 {total}개")
    print()
    
    # 테스트 케이스 2
    change2 = 4570
    coins2 = [500, 100, 50, 10]
    total, details = make_change_greedy(change2, coins2)
    
    print("=== 거스름돈 계산 ===")
    print(f"거슬러줄 금액: {change2}원")
    for coin, count in details.items():
        print(f"{coin}원: {count}개")
    print(f"총 {total}개")
    print()
    
    # 테스트 케이스 3
    change3 = 1000
    coins3 = [500, 100, 50, 10]
    total, details = make_change_greedy(change3, coins3)
    
    print("=== 거스름돈 계산 ===")
    print(f"거슬러줄 금액: {change3}원")
    for coin, count in details.items():
        print(f"{coin}원: {count}개")
    print(f"총 {total}개")
