from importlib import import_module

def main():
    # create class path
    path = "test_package.test.test"
    className = "myTest"
    print(f"path: {path}")
    print(f"className: {className}")

    # import class
    mod = import_module(path)
    if mod is None:
        raise Exception("Unable to find package version")

    my_class = getattr(mod, className)
    if my_class is None:
        raise Exception("Unable to find class")
    
    # instantiate class
    # myClass = my_class()
    # OR call func
    my_class()  # Hello from myTest()
            
if __name__ == "__main__":
    main()