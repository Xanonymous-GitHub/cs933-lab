from collections.abc import Sequence

from ._color import ResistorColor


def __get_multiplier(color: ResistorColor) -> float:
    if color == ResistorColor.GOLD:
        return 0.1
    elif color == ResistorColor.SILVER:
        return 0.01
    else:
        return 10 ** color.value


def __get_tolerance(color: ResistorColor) -> float:
    match color:
        case ResistorColor.BROWN:
            return 1
        case ResistorColor.RED:
            return 2
        case ResistorColor.GREEN:
            return 0.5
        case ResistorColor.BLUE:
            return 0.25
        case ResistorColor.VIOLET:
            return 0.1
        case ResistorColor.GRAY:
            return 0.05
        case ResistorColor.GOLD:
            return 5
        case ResistorColor.SILVER:
            return 10
        case _:
            return 20


def __get_temperature_coefficient(color: ResistorColor) -> float:
    match color:
        case ResistorColor.BLACK:
            return 250
        case ResistorColor.BROWN:
            return 100
        case ResistorColor.RED:
            return 50
        case ResistorColor.ORANGE:
            return 15
        case ResistorColor.YELLOW:
            return 25
        case ResistorColor.GREEN:
            return 20
        case ResistorColor.BLUE:
            return 10
        case ResistorColor.VIOLET:
            return 5
        case _:
            return 0


def calculate_resistor_value(colors: Sequence[ResistorColor]) -> str:
    band_number = len(colors)

    if band_number < 3:
        raise ValueError("The resistor should have at least 3 bands.")
    elif band_number > 6:
        raise ValueError("The resistor should have at most 6 bands.")

    ordered_colors = list(colors)

    # Check the order of the bands.
    if colors[0] == ResistorColor.GOLD or colors[1] == ResistorColor.GOLD:
        ordered_colors = colors[::-1]

    significant_digits = 0
    multiplier = 0
    tolerance = 0
    temperature_coefficient = 0

    match band_number:
        case 3:
            significant_digits = int(
                f"{ordered_colors[0].value}"
                f"{ordered_colors[1].value}"
            )
            multiplier = __get_multiplier(ordered_colors[2])
            tolerance = __get_tolerance(ResistorColor.NONE)
            temperature_coefficient = 0
        case 4:
            significant_digits = int(
                f"{ordered_colors[0].value}"
                f"{ordered_colors[1].value}"
            )
            multiplier = __get_multiplier(ordered_colors[2])
            tolerance = __get_tolerance(ordered_colors[3])
            temperature_coefficient = 0
        case 5:
            significant_digits = int(
                f"{ordered_colors[0].value}"
                f"{ordered_colors[1].value}"
                f"{ordered_colors[2].value}"
            )
            multiplier = __get_multiplier(ordered_colors[3])
            tolerance = __get_tolerance(ordered_colors[4])
            temperature_coefficient = 0
        case 6:
            significant_digits = int(
                f"{ordered_colors[0].value}"
                f"{ordered_colors[1].value}"
                f"{ordered_colors[2].value}"
            )
            multiplier = __get_multiplier(ordered_colors[3])
            tolerance = __get_tolerance(ordered_colors[4])
            temperature_coefficient = __get_temperature_coefficient(ordered_colors[5])

    return f"{significant_digits * multiplier} ±{tolerance}% {temperature_coefficient}ppm/K"
