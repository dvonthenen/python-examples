from dog import Dog

def base_func():
    return "simple"
            
def call_func(func):
    print(func())

call_func(base_func)

dog = Dog(name="Zoe")
dog()
