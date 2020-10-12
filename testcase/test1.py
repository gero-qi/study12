class test1():

    def bb(self, *args):
        print(*args)
        print(type(args))
        return "ok"

    def hh(self, *args):
        print("aaa", args)
        print(self.bb(*args))


if __name__ == '__main__':
    test = test1()
    test.hh(1,2)
