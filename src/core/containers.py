from functools import lru_cache

from punq import Container, Scope

from src.core.configs import settings
from src.domain.services.healthcheck import IHealthCheckService
from src.gateways.postgresql.database import Database
from src.services.healthcheck import (
    ComposedHealthcheckService,
    PostgresHealthcheckService,
)


@lru_cache(1)
def get_container() -> Container:
    return _init_container()


def _init_container() -> Container:
    container = Container()

    container.register(
        Database,
        scope=Scope.singleton,
        factory=lambda: Database(
            url=settings.POSTGRES_DB_URL, ro_url=settings.POSTGRES_DB_URL
        ),
    )

    container.register(PostgresHealthcheckService)

    def healthcheck_service_factory():
        services = [
            container.resolve(PostgresHealthcheckService),
        ]
        return ComposedHealthcheckService(services=services)

    container.register(IHealthCheckService, factory=healthcheck_service_factory)

    return container
