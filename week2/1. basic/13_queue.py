from collections import deque

def process_print_queue(jobs):

    queue = deque(jobs)

    processed = []

    while (queue):
        content = queue.popleft()
        processed.append(content)
    return processed


# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    jobs1 = ["문서A", "문서B", "문서C"]
    print("=== 프린터 작업 처리 ===")
    result1 = process_print_queue(jobs1)
    print(f"처리 완료: {result1}")
    print()
    
    # 테스트 케이스 2
    jobs2 = ["이메일", "보고서", "사진", "계약서"]
    print("=== 프린터 작업 처리 ===")
    result2 = process_print_queue(jobs2)
    print(f"처리 완료: {result2}")


