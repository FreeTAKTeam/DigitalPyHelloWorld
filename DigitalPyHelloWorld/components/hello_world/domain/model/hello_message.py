"""This module contains the HelloMessage class. It is a simple example of a DigitalPyNode."""
from digitalpy.core.domain.node import Node


# TODO: fix this pylint error
class HelloMessage(Node):  # pylint: disable=abstract-method
    """HelloMessage is a DigitalPyNode that is used to manipulate Hello Messages."""

    def __init__(self, model_configuration, model, oid=None, node_type="hello_message") -> None:
        super().__init__(node_type, model_configuration=model_configuration, model=model, oid=oid)  # type: ignore
        self._text: str = ""

    @property
    def text(self) -> str:
        """get the text

        Returns:
            str: the text
        """
        return self._text

    @text.setter
    def text(self, text: str):
        """set the text

        Args:
            text (str): the text

        Raises:
            TypeError: if text is not a string
        """
        if not isinstance(text, str):
            raise TypeError("'text' must be a string")

        self._text = text

    def __str__(self) -> str:
        return f"HelloMessage(text={self.text})"
