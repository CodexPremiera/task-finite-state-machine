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
    [1, 0, 1, 2, 8],
    [2, 1, 2, 3, 8],
    [3, 2, 3, 4, 8],
    [4, 3, 4, 7, 8],
    [7, 4, 5, 7, 8],
    [7, 5, 6, 7, 8],
    [7, 6, 7, 7, 8],
    [8, 7, 8, 8, 8],
    [9, 8, 9, 9, 9],
    [9, 8, 9, 9, 9],
]


def check_traffic():
    # This function simulates a traffic situation. In the real world, sensors and certain algorithms
    # will be used to truly check the state of traffic

    print('Checking current lane traffic...', end=' ')

    traffic_input = random.randint(0, 99)
    if traffic_input < 30:
        print(f'Normal traffic detected.\n')    # 30% chance
        return 0
    elif traffic_input < 40:
        print(f'Emergency vehicle detected.\n')     # 10% chance
        return 1
    elif traffic_input < 65:
        print(f'More vehicles coming detected.\n')  # 25% chance
        return 2
    elif traffic_input == 90:
        print(f'Less vehicles coming detected.\n')  # 25% chance
        return 3
    else:
        print(f'Another lane is needing access.\n')   # 10% chance
        return 4


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

