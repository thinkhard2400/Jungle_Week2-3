def select_meetings(meetings):

    selected = []

    meetings.sort(key=lambda x: x[1])
    selected.append(meetings[0])

    std = selected[0][1]
    i = 1
    while(i < len(meetings)):
        if meetings[i][0] >= std:
            selected.append(meetings[i])
            std = meetings[i][1]
        i += 1

    return len(selected), selected

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    meetings1 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9)]
    count1, selected1 = select_meetings(meetings1)
    print("=== 테스트 케이스 1 ===")
    print(f"전체 회의: {meetings1}")
    print(f"배정된 회의 개수: {count1}개")
    print(f"선택된 회의: {selected1}")
    print()
    
    # 테스트 케이스 2
    meetings2 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
    count2, selected2 = select_meetings(meetings2)
    print("=== 테스트 케이스 2 ===")
    print(f"전체 회의: {len(meetings2)}개")
    print(f"배정된 회의 개수: {count2}개")
    print(f"선택된 회의: {selected2}")


'''
=== 테스트 케이스 1 ===
전체 회의: [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9)]
배정된 회의 개수: 2개
선택된 회의: [(1, 4), (5, 7)]

=== 테스트 케이스 2 ===
전체 회의: 11개
배정된 회의 개수: 4개
선택된 회의: [(1, 4), (5, 7), (8, 11), (12, 14)]
'''