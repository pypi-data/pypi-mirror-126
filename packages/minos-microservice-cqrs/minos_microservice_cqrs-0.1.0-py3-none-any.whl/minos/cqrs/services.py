from abc import (
    ABC,
)
from asyncio import (
    gather,
)
from functools import (
    partial,
)
from inspect import (
    getmembers,
    isfunction,
    ismethod,
)
from typing import (
    Type,
)
from uuid import (
    UUID,
)

from cached_property import (
    cached_property,
)
from dependency_injector.wiring import (
    Provide,
    inject,
)

from minos.aggregate import (
    Aggregate,
)
from minos.common import (
    MinosConfig,
    ModelType,
    import_module,
)
from minos.networks import (
    EnrouteDecorator,
    Request,
    Response,
    ResponseException,
    WrappedRequest,
    enroute,
)
from minos.saga import (
    SagaManager,
)

from .exceptions import (
    MinosIllegalHandlingException,
)
from .handlers import (
    PreEventHandler,
)


class Service(ABC):
    """Base Service class"""

    @inject
    def __init__(
        self,
        *args,
        config: MinosConfig = Provide["config"],
        saga_manager: SagaManager = Provide["saga_manager"],
        **kwargs,
    ):
        self.config = config
        self.saga_manager = saga_manager

    @classmethod
    def __get_enroute__(cls, config: MinosConfig) -> dict[str, set[EnrouteDecorator]]:
        result = dict()
        for name, fn in getmembers(cls, predicate=lambda x: ismethod(x) or isfunction(x)):
            if not hasattr(fn, "__decorators__"):
                continue
            result[name] = fn.__decorators__
        return result


class CommandService(Service, ABC):
    """Command Service class"""

    @staticmethod
    def _pre_command_handle(request: Request) -> Request:
        return request

    @staticmethod
    def _pre_query_handle(request: Request) -> Request:
        raise MinosIllegalHandlingException("Queries cannot be handled by `CommandService` inherited classes.")

    def _pre_event_handle(self, request: Request) -> Request:
        fn = partial(PreEventHandler.handle, saga_manager=self.saga_manager, user=request.user)
        return WrappedRequest(request, fn)

    @classmethod
    def __get_enroute__(cls, config: MinosConfig) -> dict[str, set[EnrouteDecorator]]:
        aggregate_name = config.service.aggregate.rsplit(".", 1)[-1]
        additional = {
            cls.__get_aggregate__.__name__: {enroute.broker.command(f"Get{aggregate_name}")},
            cls.__get_aggregates__.__name__: {enroute.broker.command(f"Get{aggregate_name}s")},
        }
        return super().__get_enroute__(config) | additional

    async def __get_aggregate__(self, request: Request) -> Response:
        """Get aggregate.

        :param request: The ``Request`` instance that contains the aggregate identifier.
        :return: A ``Response`` instance containing the requested aggregate.
        """
        try:
            content = await request.content(model_type=ModelType.build("Query", {"uuid": UUID}))
        except Exception as exc:
            raise ResponseException(f"There was a problem while parsing the given request: {exc!r}")

        try:
            aggregate = await self.__aggregate_cls__.get(content["uuid"])
        except Exception as exc:
            raise ResponseException(f"There was a problem while getting the aggregate: {exc!r}")

        return Response(aggregate)

    async def __get_aggregates__(self, request: Request) -> Response:
        """Get aggregates.

        :param request: The ``Request`` instance that contains the product identifiers.
        :return: A ``Response`` instance containing the requested aggregates.
        """
        try:
            content = await request.content(model_type=ModelType.build("Query", {"uuids": list[UUID]}))
        except Exception as exc:
            raise ResponseException(f"There was a problem while parsing the given request: {exc!r}")

        try:
            aggregates = await gather(*(self.__aggregate_cls__.get(uuid) for uuid in content["uuids"]))
        except Exception as exc:
            raise ResponseException(f"There was a problem while getting aggregates: {exc!r}")

        return Response(aggregates)

    @cached_property
    def __aggregate_cls__(self) -> Type[Aggregate]:
        # noinspection PyTypeChecker
        return import_module(self.config.service.aggregate)


class QueryService(Service, ABC):
    """Query Service class"""

    @staticmethod
    def _pre_command_handle(request: Request) -> Request:
        raise MinosIllegalHandlingException("Commands cannot be handled by `QueryService` inherited classes.")

    @staticmethod
    def _pre_query_handle(request: Request) -> Request:
        return request

    def _pre_event_handle(self, request: Request) -> Request:
        fn = partial(PreEventHandler.handle, saga_manager=self.saga_manager, user=request.user)
        return WrappedRequest(request, fn)
