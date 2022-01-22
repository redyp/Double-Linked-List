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
    
    def prepend(self, value: int):
        prepend_node = Node(value)
        if self.head == None:
            self.head = prepend_node
            self.tail = prepend_node
        else:
            prepend_node._next = self.head
            self.head = prepend_node
        self.lenght += 1
        return True
    
    def pop_first(self) -> Node:
        if self.lenght == 0:
            return None
        temp = self.head
        if self.lenght == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp._next
            self.head._prev = None
            temp._next = None
        self.lenght -= 1
        return temp
    
    def get(self, index: int):
        if index < 0 or index >= self.lenght:
            return None
        if index == 0:
            return self.head
        if index == self.lenght - 1:
            return self.tail
        temp = self.head
        if index < self.lenght / 2:
            for _ in range(index):
                temp = temp._next
            return temp
        else:
            temp = self.tail
            for _ in range(self.lenght - 1, index, -1):
                temp = temp._prev
            return temp
    
    def set_value(self, index: int, value: int):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

