#221RDB489 Rinalds Dobelis 16.grupa
import sys
import threading


def compute_height(n, parents):
    # izveido koku
    children = [[] for _ in range(n)]
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            children[parent].append(i)

    # koka augstums 
    def compute_depth(node):
        if not children[node]:
            return 1
        max_depth = 0
        for child in children[node]:
            depth = compute_depth(child)
            max_depth = max(max_depth, depth)
        return max_depth + 1

    return compute_depth(root)


def main():
    input_type = input()

    if 'I' in input_type:
        n = int(input())
        parents = list(map(int, input().split()))
        height = compute_height(n, parents)
        print(height)
    elif 'F' in input_type:
        filename = input()
        with open("test/" + filename, 'r') as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
            height = compute_height(n, parents)
            print(height)
    else:
        print("Invalids")
        exit()


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
