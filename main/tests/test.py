
class A:
    def __init__(self, name):
        self.namea= name
        print("in A : ", self.namea)


class B:
    def __init__(self, name):
        self.nameb = name
        print("in B : ", self.nameb)



class AB(B, A):
    def __init__(self, aaaaaa, nameb):
        print(aaaaaa)
        print("line ", 18)
        super(B, self).__init__(aaaaaa)
        print(nameb)
        super().__init__(nameb)


def main():
    a = [i for i in range(10)]
    print(a)
    print(*a)
    print(*[i for i in range(10)])


if __name__ == '__main__':
    main()
