def hypercube_distance(u: int, v: int) -> int:
    u_bits = '{0:06b}'.format(u - 1)
    v_bits = '{0:06b}'.format(v - 1)

    distance = 0
    for i in range(6):
        if u_bits[i] != v_bits[i]:
            distance += 1

    return distance


def torus_distance(u: int, v: int):
    coords = lambda s: [(s % 16) // 4, s % 4, s // 16]
    u_coords = coords(u - 1)
    v_coords = coords(v - 1)
    return sum(min(4 - abs(c1 - c2), abs(c1 - c2)) for c1, c2 in zip(u_coords, v_coords))

