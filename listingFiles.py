import pathlib
p = pathlib.path.home()
print(list(p.glob(".*")))