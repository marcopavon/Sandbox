
import os
#print(__name__)
os.environ["test"] = "test"

for x,y in os.environ.items():
    print(f"Key: {x}, --- Value: {y}")

env = os.environ.get("test")

def show(element):
    print(element)
    return 2

show(env)

print("ddone")