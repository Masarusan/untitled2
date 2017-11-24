def my_gen1(str):
    for c in str.upper():
        yield  c

gen = my_gen1("Hello")
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))