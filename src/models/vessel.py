class Vessel:
    def __init__(self, name: str, length: float, width: float, draft: float, x: float = 0.0, y: float = 0.0):
        self.name = name
        self.length = length  # meters
        self.width = width    # meters
        self.draft = draft   # meters
        self.x = x  # meters
        self.y = y  # meters

    def move(self, dx: float, dy: float):
        self.x += dx
        self.y += dy

    def __repr__(self):
        return (f"Vessel(name={self.name!r}, length={self.length}, "
                f"width={self.width}, draft={self.draft})")
