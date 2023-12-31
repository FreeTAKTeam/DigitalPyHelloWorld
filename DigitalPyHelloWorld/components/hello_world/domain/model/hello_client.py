"""HelloClient is a DigitalPyNode that is used to manipulate Hello Clients."""
from digitalpy.core.domain.node import Node


# TODO: fix this pylint error
class HelloClient(Node):  # pylint: disable=abstract-method
    """HelloClient is a DigitalPyNode that is used to manipulate Hello Clients.
    """

    def __init__(self, model_configuration, model, oid=None, node_type="hello_client") -> None:
        super().__init__(node_type, model_configuration=model_configuration, model=model, oid=oid)  # type: ignore
        self._name: str = ""

    @property
    def name(self) -> str:
        """get the name of the client

        Returns:
            str: the name of the client
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """set the name of the client

        Args:
            name (str): the name of the client

        Raises:
            TypeError: if name is not a string
        """
        if not isinstance(name, str):
            raise TypeError("'name' must be a string")

        self._name = name

    def __str__(self) -> str:
        return f"HelloClient(name={self.name})"
