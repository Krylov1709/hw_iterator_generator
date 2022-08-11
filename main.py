nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class MyIterator:
    def __init__(self, my_list):
        self.my_list = my_list
        self.x = 0
        self.y = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.y >= len(self.my_list[self.x]):
            if self.x >= len(self.my_list):
                raise StopIteration
            self.x += 1
            self.y = 0
        if self.x >= len(self.my_list):
            raise StopIteration
        self.cursor = self.my_list[self.x][self.y]
        self.y += 1
        return self.cursor


def my_generator(my_list, x=0, y=0):
    while x < len(my_list):
        while y < len(my_list[x]):
            yield my_list[x][y]
            y += 1
        x += 1
        y = 0


if __name__ == '__main__':

    for item in MyIterator(nested_list):
        print(item)
    print('-----------------------------')
    flat_list = [item for item in MyIterator(nested_list)]
    print(flat_list)
    print('-----------------------------')
    for item in my_generator(nested_list):
        print(item)
