from typing import Literal


Color = Literal["red", "green", "blue"]


def identity(color: Color) -> Color:
    return color


# These are valid invokations of the function.
identity("red")
identity("green")
identity("blue")

# These are invalid invokations of the function.
identity("safron")
identity("fuchsia")
identity("lavender")

invalid_colors = ["red", "green", "blue"]
for invalid_color in invalid_colors:
    identity(invalid_color)