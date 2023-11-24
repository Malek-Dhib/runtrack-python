
def draw_diagonal_carpet(n):
    for i in range(n + 1):
        for j in range(n + 1):
            if i == n - j:
                print(' ', end=' ')
            else:
                print('#', end=' ')
        print()

draw_diagonal_carpet(10)

