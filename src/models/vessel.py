class Vessel:
    """Model for a single vessel object."""
    def __init__(self, name: str, length: float, width: float, draft: float):
        self.name = name
        self.length = length  # meters
        self.width = width    # meters
        self.draft = draft   # meters

    def __repr__(self):
        return (f"Vessel(name={self.name!r}, length={self.length}, "
                f"width={self.width}, draft={self.draft})")
