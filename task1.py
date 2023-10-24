def A():
    print("Hello!")

def B():
    print("Greetings!")
def C():
    print("Hi!")

q = 'Enter either "A", "B", or "C": '
a = input(q)

if a == "A":
    A()

if a == "B":
    B()
    
if a == "C":
    C()