class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        super().__init__()      # Initialize parent Stack
        self.__counter = 0      # Initialize pop counter

    def get_counter(self):
        return self.__counter   # Return number of pops done

    def pop(self):
        val = super().pop()     # Call parent pop()
        self.__counter += 1     # Increment counter
        return val              # Return popped value


# --- Testing ---
stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()

print(stk.get_counter())
