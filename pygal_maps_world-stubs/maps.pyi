from _typeshed import Incomplete
from collections.abc import Generator
from pygal.graph.map import BaseMap
from pygal.util import cached_property
from pygal_maps_world.i18n import COUNTRIES as COUNTRIES, SUPRANATIONAL as SUPRANATIONAL

WORLD_MAP: Incomplete

class World(BaseMap):
    x_labels: Incomplete
    area_names = COUNTRIES
    area_prefix: str
    svg_map = WORLD_MAP
    kind: str
    @cached_property
    def countries(self): ...

class SupranationalWorld(World):
    x_labels: Incomplete
    def enumerate_values(self, serie) -> Generator[Incomplete]: ...
