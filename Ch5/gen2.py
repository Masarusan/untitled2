def my_gen1(str):
    for c in str.upper():
        yield c

gen = my_gen1("Hello");
for c in gen:
      print(c)