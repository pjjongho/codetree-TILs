def print_pattern(N):
    alphabet_start = ord('A')
    alphabet_end = ord('Z')
    
    current_char = alphabet_start

    for i in range(N):
        print("  " * i, end="")
        for j in range(N - i):
            print(chr(current_char), end=" ")
            current_char += 1
            if current_char > alphabet_end:
                current_char = alphabet_start
        print()

N = int(input())
print_pattern(N)