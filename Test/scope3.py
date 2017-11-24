value3 = 1

def scope_test3():
    value3 = 100
    print("内部：",value3)

scope_test3()
print("外部：",value3)