""" this is the main class for the hello world digitalpy application"""
import os
import pathlib
from digitalpy.core.main.DigitalPy import DigitalPy
from digitalpy.core.component_management.impl.component_registration_handler \
    import ComponentRegistrationHandler


class DPHelloWorld(DigitalPy):
    """ this is the main class for the hello world digitalpy application
    """

    def __init__(self):
        super().__init__()
        self.configuration.add_configuration(
            "DigitalPyHelloWorld/configuration/dp_hello_world_configuration.ini")

    def event_loop(self):
        """ this is the event loop for the hello world digitalpy application
        """
        command = input("Hello User! What's your command?: ")
        if command == "hello":
            print("Hello World!")
        elif command == "quit":
            print("Bye!")
            self.stop()
        elif command == "1":
            # service_id = input("What is the id of the service you would like to start?: ")
            self.start_service(service_section_name="DigitalPyHelloWorld.HelloService")
        elif command == "2":
            # service_id = input("What is the id of the service you would like to stop?: ")
            self.stop_service(service_id="hello_world.HelloService")
        elif command == "3":
            self.restart_service(service_id="hello_world.HelloService")
        else:
            print("Sorry, I don't understand that command.")

    def start_services(self):
        super().start_services()
        self.start_service("dpHelloWorld.api")

    def register_components(self):
        # register hello world components
        hello_world_components = ComponentRegistrationHandler.discover_components(
            component_folder_path=pathlib.PurePath(
                str(
                    pathlib.PurePath(
                        os.path.abspath(__file__)
                    ).parent.parent
                    /
                    "components"
                ),
            )
        )

        for hello_world_component in hello_world_components:
            ComponentRegistrationHandler.register_component(
                hello_world_component,  # type: ignore
                "components",
                self.configuration,  # type: ignore
            )
        super().register_components()


if __name__ == '__main__':
    DPHelloWorld().start()
