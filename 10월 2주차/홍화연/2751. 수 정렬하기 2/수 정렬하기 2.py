import sys

N = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(N)]


lst.sort()


sys.stdout.write("\n".join(map(str, lst)) + "\n")