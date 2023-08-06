from __future__ import (
    annotations,
)

import logging
from typing import (
    Any,
)
from uuid import (
    UUID,
)

from minos.common import (
    CommandReply,
    CommandStatus,
    MinosConfig,
)

from .abc import (
    Broker,
)

logger = logging.getLogger(__name__)


class CommandReplyBroker(Broker):
    """Minos Command Broker Class."""

    ACTION = "commandReply"

    @classmethod
    def _from_config(cls, *args, config: MinosConfig, **kwargs) -> CommandReplyBroker:
        return cls(*args, **config.broker.queue._asdict(), **kwargs)

    # noinspection PyMethodOverriding
    async def send(self, data: Any, topic: str, saga: UUID, status: CommandStatus, **kwargs) -> int:
        """Send a ``CommandReply``.

        :param data: The data to be send.
        :param topic: Topic in which the message will be published.
        :param saga: Saga identifier.
        :param status: Command status.
        :return: This method does not return anything.
        """

        command_reply = CommandReply(topic, data, saga, status)
        logger.info(f"Sending '{command_reply!s}'...")
        return await self.enqueue(command_reply.topic, command_reply.avro_bytes)
