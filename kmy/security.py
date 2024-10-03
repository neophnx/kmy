from kmy.container import Container
from kmy.entity import Entity


class Security(Entity):
    entity_name = "SECURITY"


class SecurityContainer(Container[Security]):
    entity_name = "SECURITIES"
    entity_class = Security
