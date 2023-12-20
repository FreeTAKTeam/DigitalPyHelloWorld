"""This is the Mission component action mapper."""
from digitalpy.core.zmanager.impl.default_action_mapper import DefaultActionMapper


class HelloWorldActionMapper(DefaultActionMapper):
    """This is the Mission component action mapper.

    Each component must have its own action mapper to be loaded with
    the internal action mapping configuration and to be used by the
    facade for internal routing.
    """
