#def gen123():
#    yield 1
#    yield 2
#    yield 3
#for v in gen123():
#    print(v)

#def take(count, iterable):
#    counter = 0
#    for item in iterable:
#        if counter == count:
#            return
#        counter += 1
#        yield item


#def distinct(iterable):
#    seen = set()
#    for item in iterable:
#        if item in seen:
#            continue
#        yield item
#        seen.add(item)


#def run_pipeline():
#    items = [3, 6, 6, 2, 1, 1]
#    for item in take(3, distinct(items)):
#        print(item)


#run_pipeline()

#def lucas():
#    yield 2
#    a = 2
#    b = 1
#    while True:
#        yield b
#        a, b = b, a + b

#for x in lucas():
#    print(x)


#(expr(item) for item in iterable)