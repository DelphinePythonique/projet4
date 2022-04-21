from datetime import datetime


class Round:
    def __init__(self, name):
        self.name = name
        self.begin_date = datetime.today()
        self.end_date = None
        self.matchs = []

    def start(self):
        pass

    def stop(self):
        self.end_date = datetime.today()

    def do_the_paring(self):
        pass

    def add_match(self, match):
        pass

    def __str__(self):
        return self.name
