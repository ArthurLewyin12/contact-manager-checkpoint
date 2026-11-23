# Contact Management System

This repo contains my contact manager checkpoint. It's a small Python program with a text menu that combines a doubly linked list, a hash table and string matching.

## What it does

- Add contacts with a name and a phone number
- Search contacts with a keyword (substring match)
- Find a contact by its exact name
- Show all contacts from first to last, or from last to first

## How it works

- **Contact**: a class with `name` and `phone`.
- **Doubly linked list**: every contact is stored in a `Node` with `prev` and `next` pointers. The list implements `__iter__` (from head to tail, following `next`) and `__reversed__` (from tail to head, following `prev`), so it works with `for` loops and `reversed()`.
- **Hash table**: a Python `dict` with the name as key. Looking up a contact by its exact name is O(1) on average, without going through the whole list.
- **Naive string matching**: `naive_search()` tries the keyword at every position of the name and compares it with the text at that position. The search ignores upper and lower case.

`Contact` and `Node` are dataclasses, and the code uses type hints.

Each contact is stored in both the list and the dict, and it's the same object in both places. Two contacts can't have the same name, because the name is the key of the dict.

## How to run it

```bash
python3 contacts.py
```

## Example

```
1. Add Contact
2. Search by Keyword
3. Search by Exact Name
4. View All (Forward)
5. View All (Backward)
6. Exit
Enter option: 1
Name: Alice
Phone: 1234567890
Contact added.

Enter option: 2
Search keyword: Al
Match found: Alice - 1234567890
```
