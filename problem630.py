from fractions import Fraction


s = [290797]
while len(s) != 5001:
    s.append(s[-1] ** 2 % 50515093)

points = []
for i in range(len(s) // 2):
    points.append([s[2 * i + 1] % 2000 - 1000, s[2 * i + 2] % 2000 - 1000])

was = {}


def slope(p1, p2):
    if p1[0] == p2[0]:
        return 'x' # i.e. line equation is x = const
    return Fraction(p1[1] - p2[1], p1[0] - p2[0])


def n_of_line(m, p):
    if m == 'x':
        return p[0]
    return p[1] - m * p[0]


for i in range(len(points)):
    print(i)
    for j in range(i + 1, len(points)):
        m = slope(points[i], points[j])
        n = n_of_line(m, points[i])
        if m in was:
            was[m].add(n)
        else:
            was[m] = {n}

count = 0
n = sum([len(x) for x in was.values()])
for k in was:
    count += len(was[k]) * (n - len(was[k]))

print(count)

