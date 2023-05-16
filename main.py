class Collection:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)


my_collection = Collection([1, 2, 3, 4, 5, 10])

for item in my_collection:
    print(item)

for item in my_collection:
    doubled_values = item * 2
    print(doubled_values)

print(f"The length of my collection is: {len(my_collection)}")
