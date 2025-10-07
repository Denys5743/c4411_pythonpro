class MyIterable:
    def __iter__(self):
        yield from range(5)

obj = MyIterable()

for item in obj:
    print(item)
