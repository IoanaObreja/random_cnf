from random import randrange, getrandbits


def get_input():
    print("Number of variables: ")
    v = int(input())
    print("Number of clauses: ")
    c = int(input())
    print("How many variables in a clause? Write a number or 'random'")
    k = input()
    if k != 'random':
        k = int(k)
    return v, c, k


def generate_clause(v, k):
    l = list()
    if k == 'random':
        k = randrange(1, v+1)

    for _ in range(k):
        x = randrange(1, v+1)
        sign = getrandbits(1)
        # checks if it already is in clause
        # until it generates a literal that is not
        while x in l or (-1) * x in l:
            x = randrange(1, v + 1)
        if sign:
            x = x * (-1)
        l.append(x)
    l = sorted(l, key=abs)
    return l


def generate_cnf(v, c, k):
    L = list()
    print('p cnf', v, c)
    for _ in range(c):
        l = generate_clause(v, k)
        # checks if it already is in formula
        # until it generates a clause that is not
        while l in L:
            l = generate_clause(v, k)
        L.append(l)
        for x in l:
            print(x, end=' ')
        print(0)


if __name__ == '__main__':
    var, clauses, k = get_input()
    generate_cnf(var, clauses, k)

