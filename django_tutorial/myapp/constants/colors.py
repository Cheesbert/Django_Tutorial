from enum import Enum

class Color(Enum):
    BLACK   = (0, 0, 0)
    WHITE   = (255, 255, 255)
    GRAY    = (128, 128, 128)

    RED     = (255, 0, 0)
    GREEN   = (0, 255, 0)
    BLUE    = (0, 0, 255)
    YELLOW  = (255, 255, 0)
    CYAN    = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    ORANGE  = (255, 165, 0)
    PURPLE  = (128, 0, 128)

    def rgb(self) -> tuple[int, int, int]:
        """Return as RGB tuple for OpenCV / NumPy / PIL."""
        return self.value

    def bgr(self) -> tuple[int, int, int]:
        """Return as BGR tuple (OpenCV default)."""
        r, g, b = self.value
        return (b, g, r)

    def hex(self) -> str:
        """Return as HEX string for HTML/CSS."""
        return "#{:02x}{:02x}{:02x}".format(*self.value)