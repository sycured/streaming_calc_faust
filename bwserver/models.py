"""Define message schema (json) from Kafka."""
from abc import ABCMeta

from faust import Record


class JsonData(Record, metaclass=ABCMeta):
    """Json schema from Kafka."""

    nblisteners: float
    bitrate: float
