class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.end:
            if self.current % 2 == 0:
                result = self.current
                self.current += 2
                return result
            else:
                self.current += 1
        raise StopIteration()


en = EvenNumbers(10, 25)
for i in en:
    print(i)



