from xml.etree.ElementTree import Element

from .key_value_pair import KeyValuePairContainer
from .sub_account import SubAccountContainer
from .entity import Entity
from .container import Container


class Account(Entity):
    entity_name = "ACCOUNT"

    def __init__(self) -> None:
        self.number: str = ""
        self.last_modified: str = ""
        self.institution: str = ""
        self.name: str = ""
        self.currency: str = ""
        self.parent_account: str = ""
        self.last_reconciled: str = ""
        self.description: str = ""
        self.type: str = ""
        self.opened: str = ""
        self.id: str = ""
        self.sub_accounts: SubAccountContainer = SubAccountContainer()
        self.key_value_pair: KeyValuePairContainer = KeyValuePairContainer()

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(name='{self.name}', currency={self.currency})"
        )

    def init_from_xml(self, node: Element) -> None:
        self.number = node.attrib["number"]
        self.last_modified = node.attrib["lastmodified"]
        self.institution = node.attrib["institution"]
        self.name = node.attrib["name"]
        self.currency = node.attrib["currency"]
        self.parent_account = node.attrib["parentaccount"]
        self.last_reconciled = node.attrib["lastreconciled"]
        self.description = node.attrib["description"]
        self.type = node.attrib["type"]
        self.opened = node.attrib["opened"]
        self.id = node.attrib["id"]
        self.sub_accounts = self.sub_accounts.from_parent_xml(node)
        self.key_value_pair = self.key_value_pair.from_parent_xml(node)

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.set("number", self.number)
        node.set("lastmodified", self.last_modified)
        node.set("institution", self.institution)
        node.set("name", self.name)
        node.set("currency", self.currency)
        node.set("parentaccount", self.parent_account)
        node.set("lastreconciled", self.last_reconciled)
        node.set("description", self.description)
        node.set("type", self.type)
        node.set("opened", self.opened)
        node.set("id", self.id)
        if len(self.sub_accounts) > 0:
            node.append(self.sub_accounts.to_xml())
        if len(self.key_value_pair) > 0:
            node.append(self.key_value_pair.to_xml())
        return node


class AccountContainer(Container[Account]):
    entity_name = "ACCOUNTS"
    entity_class = Account
