from typing import List, Generic, TYPE_CHECKING
from xml.etree.ElementTree import ElementTree, Element, dump

from .key_value_pair import KeyValuePairContainer
from .sub_account import SubAccountContainer
from .entity import Entity
from .container import Container


class Account(Entity):
    entity_name = "ACCOUNT"

    def __init__(self) -> None:
        self.number: str = ""
        self.lastModified: str = ""
        self.institution: str = ""
        self.name: str = ""
        self.currency: str = ""
        self.parentAccount: str = ""
        self.lastReconciled: str = ""
        self.description: str = ""
        self.type: str = ""
        self.opened: str = ""
        self.id: str = ""
        self.subAccounts: SubAccountContainer = SubAccountContainer()
        self.keyValuePair: KeyValuePairContainer = KeyValuePairContainer()

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(name='{self.name}', currency={self.currency})"
        )

    def init_from_xml(self, node: Element) -> None:
        self.number = node.attrib["number"]
        self.lastModified = node.attrib["lastmodified"]
        self.institution = node.attrib["institution"]
        self.name = node.attrib["name"]
        self.currency = node.attrib["currency"]
        self.parentAccount = node.attrib["parentaccount"]
        self.lastReconciled = node.attrib["lastreconciled"]
        self.description = node.attrib["description"]
        self.type = node.attrib["type"]
        self.opened = node.attrib["opened"]
        self.id = node.attrib["id"]
        self.subAccounts = self.subAccounts.from_parent_xml(node)
        self.keyValuePair = self.keyValuePair.from_parent_xml(node)

    def to_xml(self) -> Element:
        node = Element(self.entity_name)
        node.set("number", self.number)
        node.set("lastmodified", self.lastModified)
        node.set("institution", self.institution)
        node.set("name", self.name)
        node.set("currency", self.currency)
        node.set("parentaccount", self.parentAccount)
        node.set("lastreconciled", self.lastReconciled)
        node.set("description", self.description)
        node.set("type", self.type)
        node.set("opened", self.opened)
        node.set("id", self.id)
        if len(self.subAccounts) > 0:
            node.append(self.subAccounts.to_xml())
        if len(self.keyValuePair) > 0:
            node.append(self.keyValuePair.to_xml())
        return node


class AccountContainer(Container[Account]):
    entity_name = "ACCOUNTS"
    entity_class = Account
