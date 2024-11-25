from main import Node, Cache

def test_lru_cache():
    cache = Cache(2)

    # 1: Add some entries
    cache.put(1, 1)  # Cache is {1: 1}
    cache.put(2, 2)  # Cache is {1: 1, 2: 2}
    assert cache.get(1) == 1  # Returns 1 and moves key 1 to the front; Cache is {2: 2, 1: 1}
    
    # 2: Add an entry exceeding capacity
    cache.put(3, 3)  # Evicts key 2; Cache is {1: 1, 3: 3}
    assert cache.get(2) == -1  # Returns -1 (not found)

    # 3: Access an existing entry
    assert cache.get(3) == 3  # Returns 3; Cache is {1: 1, 3: 3}
    
    # 4: Add another entry
    cache.put(4, 4)  # Evicts key 1; Cache is {4: 4, 3: 3}
    assert cache.get(1) == -1  # Returns -1 (not found)
    assert cache.get(3) == 3  # Returns 3
    assert cache.get(4) == 4  # Returns 4

    print("All test cases passed!")

test_lru_cache()
