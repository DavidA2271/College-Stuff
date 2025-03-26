import random
from separate_chaining import chaining_hashtable
from open_addr_lin_probe import lin_probe_table
from double_hash import double_hash_table


def main():
    lst = [str(random.randint(0, 1000000)) for _ in range(100)]

    print('-----------------Testing Chaining Hash Table------------------------')
    cht = chaining_hashtable(12)
    for _ in lst:
        cht.insert(_, _)
    print(len(cht))
    print(cht.search('0'))
    print(cht.search(lst[50]))
    cht.delete('0')
    cht.delete(lst[50])
    print(len(cht))
    print()
    print()

    print('-----------------Testing Linear Probe Hash Table------------------------')
    lpt = lin_probe_table(101)
    for _ in lst:
        lpt.insert(_, _)
    print(len(lpt))
    print(lpt.search('0'))
    print(lpt.search(lst[50]))
    lpt.delete('0')
    lpt.delete(lst[50])
    print(len(lpt))
    print()
    print()

    print('-----------------Testing Double Hash Table------------------------')
    dht = double_hash_table(101)
    for _ in lst:
        dht.insert(_, _)
    print(len(dht))
    print(dht.search('0'))
    print(dht.search(lst[50]))
    dht.delete('0')
    dht.delete(lst[50])
    print(len(dht))
    print()
    print()


if __name__ == '__main__':
    main()