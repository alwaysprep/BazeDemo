

class Pipeline:

    def __init__(self, tasks: tuple) -> None:
        self.tasks = tasks

    def run(self, data):
        for task in self.tasks:
            data = task()
        return data
