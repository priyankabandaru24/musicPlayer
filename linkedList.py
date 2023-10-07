# linked_list.py
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def shuffle(self):
        nodes = []
        temp = self.head
        while temp:
            nodes.append(temp)
            temp = temp.next
        
        random.shuffle(nodes)

        # Reconstruct the linked list
        self.head = nodes[0]
        self.tail = nodes[-1]
        self.head.prev = None
        self.tail.next = None

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
            nodes[i + 1].prev = nodes[i]
        
        self.current = self.head

    def next_song(self):
        if self.current and self.current.next:
            self.current = self.current.next
        return self.current.data if self.current else None

    def prev_song(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
        return self.current.data if self.current else None

    def get_playlist(self):
        songs = []
        temp = self.head
        while temp:
            songs.append(temp.data)
            temp = temp.next
        return songs
