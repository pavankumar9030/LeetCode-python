class MyHashSet:

    def __init__(self):
        self.set = []

    def add(self, key):
        if key not in self.set:
            self.set.append(key)

    def remove(self, key):
        if key in self.set:
            self.set.remove(key)

    def contains(self, key):
        return key in self.set