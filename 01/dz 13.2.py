class Counter:

    def __init__(self, start=0, min_value=0, max_value=10):
        self.min_value = min_value
        self.max_value = max_value
        self.value = start

    def set_max(self, max_value):
        self.max_value = max_value

    def set_min(self, min_value):
        self.min_value = min_value

    def set_start(self, start):
        if start < self.min_value or start > self.max_value:
            raise ValueError("Start value out of range")
        self.value = start

    def step_up(self):
        if self.value >= self.max_value:
            raise ValueError("Maximum reached")
        self.value += 1

    def step_down(self):
        if self.value <= self.min_value:
            raise ValueError("Minimum reached")
        self.value -= 1

    def get_value(self):
        return self.value