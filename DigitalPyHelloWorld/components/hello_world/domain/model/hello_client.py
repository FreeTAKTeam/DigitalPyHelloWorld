from digitalpy.core.domain.node import Node


class HelloClient(Node):
    def __init__(self, node_type="hello_client", oid=None) -> None:
        super().__init__(node_type, oid=oid)  # type: ignore
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
