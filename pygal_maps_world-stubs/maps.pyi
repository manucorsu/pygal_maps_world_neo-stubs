from collections.abc import Iterable, Iterator

from pygal.graph.map import BaseMap
from pygal.serie import Serie
from pygal.util import cached_property
from typing_extensions import override

from .i18n import COUNTRIES as COUNTRIES
from .i18n import SUPRANATIONAL as SUPRANATIONAL

WORLD_MAP: str

class World(BaseMap):
    x_labels: Iterable[str] | None
    area_names: dict[str, str]
    area_prefix: str
    svg_map: str
    kind: str
    @cached_property
    def countries(self) -> list[str]: ...

class SupranationalWorld(World):
    x_labels: Iterable[str] | None
    @override
    def enumerate_values(
        self, serie: Serie
    ) -> Iterator[tuple[int, tuple[str, object]]]: ...
