def shuffle(deck):
    a, b = deck[:len(deck) // 2], deck[len(deck) // 2:]
    res = []
    for i in range(len(deck) // 2):
        res.append(a[i])
        res.append(b[i])
    return res


def deshuffle(deck):
    a, b = [], []
    for i in range(0, len(deck), 2):
        a.append(deck[i])
        b.append(deck[i + 1])
    return a + b


def count(n):
    deck = [i for i in range(n)]
    #print(deck)
    one = [1]
    d = shuffle(deck)
    tot = 1
    while d != deck:
        one.append(d[1])
        #print(d)
        d = shuffle(d)
        tot += 1
    one.append(d[1])
    return tot, one


def count2(n):
    res = 1
    place = [1]
    m = 1 + (n - 1) // 2
    while m != 1:
        place.append(m)
        if m % 2 == 0:
            m //= 2
        else:
            m = m + (n - m) // 2
        res += 1
    place.append(m)
    return res, place
