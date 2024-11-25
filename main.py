class Node:
    """
    Node for doubly linked list storing key-value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class Cache:
    def __init__(self, capacity):
        """
        Initialize LRU cache with given capacity
        """
        self.capacity = capacity
        self.cache = {}  
        # Dummy head and tail for the doubly linked list
        self.head = Node(0, 0)  # Most recent
        self.tail = Node(0, 0)  # Least recent
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """
        Remove a node from the list.
        """
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _add_to_head(self, node):
        """
        Add a node to the front of the list.
        """
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        """
        Retrieve value by key. Move accessed node to the front.
        """
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.value
        return -1

    def put(self, key, value):
        """
        Insert or update key-value pair. Evict oldest if capacity is exceeded.
        """
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_head(node)
        else:
            if len(self.cache) == self.capacity:
                # Remove least recently used node
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            # Add new node to cache and list
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
