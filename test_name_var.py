# The __name__ variable is a special builtin
# variable that you can use to evaluate whether a
# program is being run in standalone
# mode or as an imported module; remember that a
# module is just a Python program used inside of another Python program.


if __name__ == "__main__":
    print("Nobody is calling me")
else:
    print("Soeome is calling me")
