import heapq

def process_emergency_room(patients):

    heap = []
    for name, priority in patients:
        new_patients = (priority, name)
        heapq.heappush(heap, new_patients)

    processed = []
    while heap:
        p, n = heapq.heappop(heap)
        processed.append((p,n))
    
    return processed

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    patients1 = [
        ("김철수", 3),
        ("이영희", 1),
        ("박민수", 2)
    ]
    print("=== 응급실 환자 처리 ===")
    result1 = process_emergency_room(patients1)
    print(f"처리 순서: {result1}")
    print()
    
    # 테스트 케이스 2
    patients2 = [
        ("환자A", 5),
        ("환자B", 1),
        ("환자C", 3),
        ("환자D", 2)
    ]
    print("=== 응급실 환자 처리 ===")
    result2 = process_emergency_room(patients2)
    print(f"처리 순서: {result2}")


