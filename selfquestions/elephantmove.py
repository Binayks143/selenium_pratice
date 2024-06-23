
def min_steps_to_destination(destination, moves):
    if destination == 0:
        return 0
    if destination < 0:
        return float('inf')
    min_steps = float('inf')
    for move in moves:
        min_steps = min(min_steps, 1 + min_steps_to_destination(destination - move, moves))
    return min_steps

destination = 12
moves = [1, 2, 3, 6, 5]
print("Minimum steps to reach destination:", min_steps_to_destination(destination, moves))
