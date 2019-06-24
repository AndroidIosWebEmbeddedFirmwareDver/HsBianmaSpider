import json

class Foo(object):
    def __init__(self):
        self.x = 1
        self.y = 2




if __name__ == '__main__':

    foo = Foo()
    # s = json.dumps(foo) # raises TypeError with "is not JSON serializable"
    s = json.dumps(foo.__dict__) # s set to: {"x":1, "y":2}
    print(s)