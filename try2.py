from other import decorators

@decorators.slow_down(0.2)
def hello():
    print("hello")

for _ in range(5):
    hello()
