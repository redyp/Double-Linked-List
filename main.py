from __future__ import annotations
from dataclasses import dataclass, field

@dataclass
class Node:
    value: int
    _next: Node = None
    _prev: Node = None

@dataclass
class DoubleLinkedList:
    value: int = field(repr=False, default=None)
    head: Node = field(init=False, default=None)
    tail: Node = field(init=False, default=None)
    lenght: int = field(init=False, default=0)

    def __post_init__(self):
        if self.value:
            new_node = Node(self.value)
            self.head = new_node
            self.tail = new_node
            self.lenght = 1
    
    def __str__(self) -> str:
        if self.head == None:
            return 'Double Linked List Kosong'
        temp = self.head
        temp_str = 'None'
        while temp:
            temp_str += f' <- {temp.value} -> '
            temp = temp._next
        temp_str += 'None'
        return temp_str
    
    def append(self, value: int):
        append_node = Node(value)
        if self.head == None:
            self.head = append_node
            self.tail = append_node
        else:
            append_node._prev = self.tail
            self.tail._next = append_node
            self.tail = append_node
        self.lenght += 1
        return True
    
    def pop(self) -> Node:
        if self.lenght == 0:
            return None
        temp = self.tail
        self.tail = temp._prev
        self.tail._next = None
        temp._prev = None
        self.lenght -= 1
        return temp

