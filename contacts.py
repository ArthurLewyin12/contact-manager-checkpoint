"""Contact manager using a doubly linked list, a hash table and naive string matching."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator


@dataclass
class Contact:
    name: str
    phone: str

    def __str__(self) -> str:
        return f"{self.name} - {self.phone}"


@dataclass
class Node:
    contact: Contact
    prev: Node | None = None
    next: Node | None = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None

    def append(self, contact: Contact) -> None:
        node = Node(contact, prev=self.tail)
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def __iter__(self) -> Iterator[Contact]:
        node = self.head
        while node:
            yield node.contact
            node = node.next

    def __reversed__(self) -> Iterator[Contact]:
        node = self.tail
        while node:
            yield node.contact
            node = node.prev


def naive_search(text: str, pattern: str) -> bool:
    """Return True if pattern appears in text, checking every position."""
    n, m = len(text), len(pattern)
    return any(text[i:i + m] == pattern for i in range(n - m + 1))


class ContactManager:
    def __init__(self) -> None:
        self.contacts = DoublyLinkedList()
        self.by_name: dict[str, Contact] = {}  # hash table

    def add(self, name: str, phone: str) -> bool:
        if name in self.by_name:
            return False
        contact = Contact(name, phone)
        self.contacts.append(contact)  # same object in both structures
        self.by_name[name] = contact
        return True

    def search_keyword(self, keyword: str) -> list[Contact]:
        keyword = keyword.lower()
        return [c for c in self.contacts if naive_search(c.name.lower(), keyword)]

    def search_name(self, name: str) -> Contact | None:
        return self.by_name.get(name)


MENU = """
1. Add Contact
2. Search by Keyword
3. Search by Exact Name
4. View All (Forward)
5. View All (Backward)
6. Exit"""


def show(contacts: list[Contact], prefix: str = "") -> None:
    if not contacts:
        print("No contacts found.")
    for contact in contacts:
        print(f"{prefix}{contact}")


def main() -> None:
    manager = ContactManager()

    while True:
        print(MENU)
        option = input("Enter option: ").strip()

        if option == "1":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            if not name or not phone:
                print("Name and phone can't be empty.")
            elif manager.add(name, phone):
                print("Contact added.")
            else:
                print("A contact with this name already exists.")
        elif option == "2":
            show(manager.search_keyword(input("Search keyword: ").strip()), "Match found: ")
        elif option == "3":
            contact = manager.search_name(input("Name: ").strip())
            print(f"Contact found: {contact}" if contact else "Contact not found.")
        elif option == "4":
            show(list(manager.contacts))
        elif option == "5":
            show(list(reversed(manager.contacts)))
        elif option == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option, choose between 1 and 6.")


if __name__ == "__main__":
    main()
