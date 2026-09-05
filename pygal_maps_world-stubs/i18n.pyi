from collections.abc import Iterable, Mapping

COUNTRIES: dict[str, str]
EUR: list[str]
OECD: list[str]
NAFTA: list[str]
USMCA: list[str]
ASIA: list[str]
EUROPE: list[str]
AFRICA: list[str]
NORTH_AMERICA: list[str]
SOUTH_AMERICA: list[str]
OCEANIA: list[str]
ANTARTICA: list[str]
ANTARCTICA: list[str]
SUPRANATIONAL: dict[str, list[str]]

def set_countries(
    countries: Mapping[str, str] | Iterable[tuple[str, str]], clear: bool = False
) -> None: ...
