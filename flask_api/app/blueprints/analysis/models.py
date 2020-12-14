class Timer:
    def __init__(self, duration):
        self.start = 0
        self.duration = f'{duration} minutes'
        self.end = duration
        self.interval = 'minutes'