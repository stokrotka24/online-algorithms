import random
from typing import Callable


def queries_cost(distance: Callable, request_positions: list[int], server_position: int):
    return sum(map(lambda request_position: distance(request_position, server_position), request_positions))


def move_to_min(distance: Callable, request_positions: list[int], graph_size: int = 64, D: int = 32):
    server_position = 1
    nof_phases = len(request_positions) // D
    total_cost = 0

    for i in range(nof_phases):
        phase = request_positions[i * D: (i + 1) * D]

        # cost of phase
        total_cost += queries_cost(distance, phase, server_position)

        # pick new server position
        new_server_position = sorted(
            map(lambda v: (v, queries_cost(distance, phase, v)), range(1, graph_size + 1)),
            key=lambda x: x[1],
        )[0][0]

        # move server
        total_cost += D * distance(server_position, new_server_position)
        server_position = new_server_position

    return total_cost


def flip(distance: Callable, request_positions: list[int], graph_size: int = 64, D: int = 32):
    server_position = 1
    pbb = 1 / (2 * D)
    total_cost = 0

    for request_position in request_positions:
        dist = distance(request_position, server_position)
        total_cost += dist

        if random.random() < pbb:
            total_cost += D * dist
            server_position = request_position

    return total_cost
