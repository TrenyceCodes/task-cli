from datetime import datetime


class Tasks:
    def __init__(self) -> None:
        self.id = 0
        self.description = ""
        self.status = ""
        self.createdAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.updatedAt = ""
