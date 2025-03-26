
memory_blocks = [300, 200, 500, 400, 100]
request_sizes = [500, 50, 25, 300, 150, 400]


def status_report(memory_blocks, request_sizes):
    print()
    print("Memory Blocks Available:", memory_blocks)
    print("Total Memory Available:", sum(memory_blocks))
    sr = sum(request_sizes)
    print("Request Sizes:", request_sizes)
    print("Total Request Size:", sr)
    print()
    return sr == 0


def first_fit():
    print("--------FIRST-FIT-------------")
    m = memory_blocks.copy()
    r = request_sizes.copy()
    for i in r:
        for j in m:
            if i <= j:
                m[m.index(j)] -= i
                r[r.index(i)] = 0
                break
    if status_report(m, r):
        print("All requests allocated")
    else:
        print("Some requests must wait")


def best_fit():
    print("--------BEST-FIT-------------")
    m = memory_blocks.copy()
    r = request_sizes.copy()
    for i in r:
        m.sort()
        for j in m:
            if i <= j:
                m[m.index(j)] -= i
                r[r.index(i)] = 0
                break
    if status_report(m, r):
        print("All requests allocated")
    else:
        print("Some requests must wait")


def worst_fit():
    print("--------WORST-FIT-------------")
    m = memory_blocks.copy()
    r = request_sizes.copy()
    for i in r:
        m.sort(reverse=True)
        for j in m:
            if i <= j:
                m[m.index(j)] -= i
                r[r.index(i)] = 0
                break
    if status_report(m, r):
        print("All requests allocated")
    else:
        print("Some requests must wait")


if __name__ == '__main__':
    status_report(memory_blocks, request_sizes)
    first_fit()
    best_fit()
    worst_fit()
