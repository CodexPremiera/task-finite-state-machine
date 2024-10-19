import time, random


class TimeState:
    def __init__(self, start, end):
        if end > start:
            raise ValueError(f"Given end time ({end}) is greater than end time ({start}).")

        self.start = start
        self.end = end

    def __str__(self):
        return f"({self.start}-{self.end})"

    def countdown(self):
        for num in range(self.start, self.end, -1):
            print(num, end=' ')
            time.sleep(0.2)
        print(self.end)
        time.sleep(0.1)


# TIME_STATES = {
#     'A': TimeState(60, 51),
#     'B': TimeState(50, 41),
#     'C': TimeState(40, 31),
#     'D': TimeState(30, 21),
#     'E1': TimeState(20, 11),
#     'E2': TimeState(20, 11),
#     'E3': TimeState(20, 11),
#     'F': TimeState(10, 6),
#     'G': TimeState(5, 1),
#     'H': TimeState(0, 0)
# }


TIME_STATES = [
    TimeState(60, 51),
    TimeState(50, 41),
    TimeState(40, 31),
    TimeState(30, 21),
    TimeState(20, 11),
    TimeState(20, 11),
    TimeState(20, 11),
    TimeState(10, 6),
    TimeState(5, 1),
    TimeState(0, 0)
]

TRANSITIONS = [
    [1, 1, 1, 2, 8],
    [2, 2, 2, 3, 8],
    [3, 3, 3, 4, 8],
    [4, 4, 4, 7, 8],
    [7, 5, 5, 7, 8],
    [7, 6, 6, 7, 8],
    [7, 7, 7, 7, 8],
    [8, 8, 8, 8, 8],
    [9, 7, 9, 9, 9],
    [9, 9, 9, 9, 9],
]


def check_traffic():
    print('Checking traffic...', end=' ')

    traffic_input = random.randint(0, 5)
    if traffic_input == 0:
        print(f'Normal traffic detected.\n')
    elif traffic_input == 1:
        print(f'Emergency vehicle detected.\n')
    elif traffic_input == 2:
        print(f'More vehicles coming detected.\n')
    elif traffic_input == 3:
        print(f'Less vehicles coming detected.\n')
    elif traffic_input == 4:
        print(f'Another lane is needing access.\n')

    return traffic_input


def run_traffic_light():
    state_num = 0
    state = TIME_STATES[state_num]

    print('Traffic light is now GREEN.')

    while True:
        state.countdown()

        if state_num == 9:
            break

        transition = check_traffic()
        state_num = TRANSITIONS[state_num][transition]
        state = TIME_STATES[state_num]

    print('Traffic light is now RED.')


run_traffic_light()

