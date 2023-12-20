"""This module contains the HelloMessage class. It is a simple example of a DigitalPyNode."""
from digitalpy.core.domain.node import Node


# TODO: fix this pylint error
class HelloMessage(Node):  # pylint: disable=abstract-method
    """HelloMessage is a DigitalPyNode that is used to manipulate Hello Messages."""

    def __init__(self, node_type="hello_message", oid=None) -> None:
        super().__init__(node_type, oid=oid)  # type: ignore
        self._message: str = ""

    @property
    def message(self) -> str:
        """get the message

        Returns:
            str: the message
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """set the message

        Args:
            message (str): the message

        Raises:
            TypeError: if message is not a string
        """
        if not isinstance(message, str):
            raise TypeError("'message' must be a string")

        self._message = message

    def __str__(self) -> str:
        return f"HelloMessage(message={self.message})"
