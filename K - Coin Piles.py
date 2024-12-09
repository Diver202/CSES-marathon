for i in range(int(input())):
    A,B = map(int,input().split())
    if (2 * A - B) % 3 != 0 or (2 * A - B) < 0 \
            or (2 * B - A) % 3 != 0 or (2 * B - A) < 0:
        print("NO")
    else:
        print("YES")