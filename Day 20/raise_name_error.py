try:
    raise NameError("Name error raise")
except NameError:
    print("Name error handled")