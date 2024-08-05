from abc import ABC, abstractmethod


class IHealthCheckService(ABC):
    @abstractmethod
    async def check(self):
        return {"Message": "Everything is OK"}