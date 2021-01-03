def books(old, new):
    print(f"I have {old} old and {new} new books.")
    return old + new

shelf = books(50,25)

def is_true(a):

    # returning boolean of a
    return bool(a)
    print(a)

res = add(2, 3)
print("Result of add function is {}".format(res))

res = is_true(2<5)
print("\nResult of is_true function is {}".format(res)) 
