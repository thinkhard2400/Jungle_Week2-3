def n_queens(n):

    cols = [0]*n
    count = 0

    def is_valid(row, col):
        for c in range(col):
            if cols[c] == row or abs(cols[c]-row) == abs(c-col):
                return False
        return True


    def place(col):

        nonlocal count
        if col == n:
            count += 1
            return

        for row in range(0,n):
            if is_valid(row, col):
                cols[col] = row
                place(col+1)
    place(0)
    return count


if __name__ == "__main__":
    print("[테스트] N=1 ~ N=8 에 대한 가능한 배치의 수")
    for n in range(1, 9):
        print(f"  N={n}: {n_queens(n)}")
