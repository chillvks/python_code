class stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def top(self):
        return self.items[len(self.items) - 1]


st1 = stack()

print(st1.isEmpty())

st1.push("first")

print(st1.isEmpty())
print(st1.top())

st1.push("second")
print(st1.size())
print(st1.top())