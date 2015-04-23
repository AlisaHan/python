import sys
cnt = 0

def cob(n, m, lst):
    global cnt
    if n>m :
        if m>1:
           lst.append(n)
           cob(n-1, m-1, lst)
           lst.pop()
           cob(n-1, m, lst)
        else:
            for i in range(1, n+1, 1):
                tls = []
                tls.extend(lst)
                tls.append(i)
                print(tls)
                cnt += 1
    else:
        tls = []
        tls.extend(lst)
        tls.extend([i for i in range(1, n+1, 1)])
        print(tls)
        cnt += 1


if __name__ == "__main__":
    print("begin")
    lst = []
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    print(n ,m)
    cob(n, m, lst)
    print(cnt)
