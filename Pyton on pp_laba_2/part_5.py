import os

class Iterator:
    def __init__(self, name):
        self.counter = 0
        self.name = name
        self.data = os.listdir(os.path.join('dataset', self.name))
        self.limit = len(self.data)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < self.limit:
            next_path = os.path.join(self.name, self.data[self.counter])
            self.counter += 1
            return next_path
        else:
            raise StopIteration
    
    

if __name__ == "__main__":

    polarbear = Iterator('polarbear')
    brownbear = Iterator('brownbear')

    print(next(polarbear))
    print(next(polarbear))
    print(next(polarbear))
    print(next(polarbear))
    print(next(brownbear))
    print(next(brownbear))
    print(next(brownbear))