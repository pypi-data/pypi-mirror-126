import sys
from typing import Optional

import numpy as np
from pydantic import BaseModel, validator


class GridConfig(BaseModel):
    FREE = 0
    OBSTACLE = 1
    MOVES = tuple([(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1), ])

    seed: Optional[int] = None
    size: int = 8
    density: float = 0.3
    num_agents: int = 1
    obs_radius: int = 5
    map: list = None
    map_name: str = None

    # noinspection PyMethodParameters
    @validator('seed')
    def seed_initialization(cls, v):
        assert v is None or (0 <= v < sys.maxsize), "seed must be in [0, " + str(sys.maxsize) + ']'
        if v is None:
            return int(np.random.randint(sys.maxsize, dtype=np.int64))
        return v

    # noinspection PyMethodParameters
    @validator('size')
    def size_restrictions(cls, v):
        assert 2 <= v <= 1024, "size must be in [2, 1024]"
        return v

    # noinspection PyMethodParameters
    @validator('density')
    def density_restrictions(cls, v):
        assert 0.0 <= v <= 1, "density must be in [0, 1]"
        return v

    # noinspection PyMethodParameters
    @validator('num_agents')
    def num_agents_must_be_positive(cls, v):
        assert 1 <= v <= 1024, "num_agents must be in [1, 1024]"
        return v

    # noinspection PyMethodParameters
    @validator('obs_radius')
    def obs_radius_must_be_positive(cls, v):
        assert 1 <= v <= 128, "obs_radius must be in [1, 128]"
        return v

    # noinspection PyMethodParameters
    @validator('map')
    def map_validation(cls, v, values):
        if v is None:
            return None
        size = len(v)
        area = 0
        for line in v:
            size = max(size, len(line))
            area += len(line)
        values['size'] = size
        values['density'] = sum([sum(line) for line in v]) / area
        for line in v:
            if len(line) < size:
                line += [1] * (size - len(line))
        while len(v) < size:
            v.append([1] * size)

        return v
