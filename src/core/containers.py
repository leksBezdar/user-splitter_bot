from functools import lru_cache

from punq import Container, Scope

from src.core.configs import settings
from src.domain.services.healthcheck import IHealthCheckService


@lru_cache(1)
def get_container() -> Container:
    return _init_container()


def _init_container() -> Container:
    container = Container()

    container.register(IHealthCheckService)

    return container