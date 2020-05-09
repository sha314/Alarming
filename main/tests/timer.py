import threading

def test3():
    threads = []
    for i in range(5):
        t = threading.Thread(target=lambda x: print("executing ", t.ident), args=(1,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

def test2():

    run = int(input("sec > "))

    def timeout(foo, bar=None):
        print("Thread id ", threading.currentThread().ident)
        print('The arguments were: foo: {}, bar: {}'.format(foo, bar))

    # duration is in seconds
    t = threading.Timer(run, timeout, args=['something'], kwargs={'bar': 'else'})
    print("Thread id ", threading.currentThread().ident)
    t.start()

    print("Thread id ", threading.currentThread().ident)
    # t.join()

if __name__ == '__main__':
    print("Thread id ", threading.currentThread().ident)
    # test2()
    test3()