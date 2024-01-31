from digitalpy.core.domain.node import Node


class Contact(Node):
    def __init__(self, model_configuration, model, oid=None, node_type="contact") -> None:
        super().__init__(node_type, model_configuration=model_configuration, model=model, oid=oid)
        self._callsign: str = ""
        self._dsn: str = ""
        self._email: str = ""
        self._endpoint: str = ""
        self._freq: float = 0.0
        self._hostname: str = ""
        self._iconsetpath: str = ""
        self._modulation: str = ""
        self._phone: str = ""
        self._version: float = 0.0
        self._xmppUsername: int = 0

    @property
    def callsign(self) -> str:
        """get the callsign of the contact

        Returns:
            str: the callsign of the contact
        """
        return self._callsign

    @callsign.setter
    def callsign(self, callsign: str):
        """set the callsign of the contact

        Args:
            callsign (str): the callsign of the contact

        Raises:
            TypeError: if callsign is not a string
        """
        if not isinstance(callsign, str):
            raise TypeError("'callsign' must be a string")

        self._callsign = callsign

    @property
    def dsn(self) -> str:
        """get the DSN number for this element

        Returns:
            str: the DSN number for this element
        """
        return self._dsn

    @dsn.setter
    def dsn(self, dsn: str):
        """set the DSN number for this element

        Args:
            dsn (str): the DSN number for this element

        Raises:
            TypeError: if dsn is not a string
        """
        if not isinstance(dsn, str):
            raise TypeError("'dsn' must be a string")

        self._dsn = dsn

    @property
    def email(self) -> str:
        """get the email address for this element

        Returns:
            str: the email address for this element
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """set the email address for this element

        Args:
            email (str): the email address for this element

        Raises:
            TypeError: if email is not a string
        """
        if not isinstance(email, str):
            raise TypeError("'email' must be a string")

        self._email = email

    @property
    def endpoint(self) -> str:
        """get the endpoint

        Returns:
            str: the endpoint
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint: str):
        """set the endpoint

        Args:
            endpoint (str): the endpoint

        Raises:
            TypeError: if endpoint is not a string
        """
        if not isinstance(endpoint, str):
            raise TypeError("'endpoint' must be a string")

        self._endpoint = endpoint

    @property
    def freq(self) -> float:
        """get the frequency on which the unit may be contacted via voice

        Returns:
            float: the frequency on which the unit may be contacted via voice
        """
        return self._freq

    @freq.setter
    def freq(self, freq: float):
        """set the frequency on which the unit may be contacted via voice

        Args:
            freq (float): the frequency on which the unit may be contacted via voice

        Raises:
            TypeError: if freq is not a float
        """
        if not isinstance(freq, float):
            raise TypeError("'freq' must be a float")

        self._freq = freq

    @property
    def hostname(self) -> str:
        """get the DNS-resolvable host name

        Returns:
            str: the DNS-resolvable host name
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname: str):
        """set the DNS-resolvable host name

        Args:
            hostname (str): the DNS-resolvable host name

        Raises:
            TypeError: if hostname is not a string
        """
        if not isinstance(hostname, str):
            raise TypeError("'hostname' must be a string")

        self._hostname = hostname

    @property
    def iconsetpath(self) -> str:
        """get the iconset path

        Returns:
            str: the iconset path
        """
        return self._iconsetpath

    @iconsetpath.setter
    def iconsetpath(self, iconsetpath: str):
        """set the iconset path

        Args:
            iconsetpath (str): the iconset path

        Raises:
            TypeError: if iconsetpath is not a string
        """
        if not isinstance(iconsetpath, str):
            raise TypeError("'iconsetpath' must be a string")

        self._iconsetpath = iconsetpath

    @property
    def modulation(self) -> str:
        """get the modulation type for the communication

        Returns:
            str: the modulation type for the communication
        """
        return self._modulation

    @modulation.setter
    def modulation(self, modulation: str):
        """set the modulation type for the communication

        Args:
            modulation (str): the modulation type for the communication

        Raises:
            TypeError: if modulation is not a string
        """
        if not isinstance(modulation, str):
            raise TypeError("'modulation' must be a string")

        self._modulation = modulation

    @property
    def phone(self) -> str:
        """get the phone number for this element

        Returns:
            str: the phone number for this element
        """
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        """set the phone number for this element

        Args:
            phone (str): the phone number for this element

        Raises:
            TypeError: if phone is not a string
        """
        if not isinstance(phone, str):
            raise TypeError("'phone' must be a string")

        self._phone = phone

    @property
    def version(self) -> float:
        """get the version tag for this sub schema

        Returns:
            float: the version tag for this sub schema
        """
        return self._version

    @version.setter
    def version(self, version: float):
        """set the version tag for this sub schema

        Args:
            version (float): the version tag for this sub schema

        Raises:
            TypeError: if version is not a float
        """
        if not isinstance(version, float):
            raise TypeError("'version' must be a float")

        self._version = version

    @property
    def xmppUsername(self) -> int:
        """get the user name in the xmpp network

        Returns:
            int: the user name in the xmpp network
        """
        return self._xmppUsername

    @xmppUsername.setter
    def xmppUsername(self, xmppUsername: int):
        """set the user name in the xmpp network

        Args:
            xmppUsername (int): the user name in the xmpp network

        Raises:
            TypeError: if xmppUsername is not an integer
        """
        if not isinstance(xmppUsername, int):
            raise TypeError("'xmppUsername' must be an integer")

        self._xmppUsername = xmppUsername
