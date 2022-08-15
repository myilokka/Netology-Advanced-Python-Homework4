from data import nested_list


class FlatIterator:

    def __init__(self, nested_list):
        self.flat_list = sum(nested_list, [])
        self.end = len(self.flat_list)
        self.start = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start != self.end-1:
            self.start += 1
            return self.flat_list[self.start]

        else:
            raise StopIteration


for i in FlatIterator(nested_list):
    print(i)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)



