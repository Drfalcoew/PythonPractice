
class basic_calulator:


    operations = ['+', '-', '*', '/', '(', ')']

    def calculate(self, input):
        my_stack = []
        my_algo = input.replace(" ", "")
        i = 1
        l, r, op = int(my_algo[0]), None, None

        while i < len(my_algo):
            x = my_algo[i]

            if x in self.operations:
                op = x
                i += 1
                continue
            if not r:
                r = int(x)


            if l and r:
                if op == '+':
                    print("IN PLUS", l, r)
                    l += r
                elif op == '-':
                    l -= r
                elif op == '*':
                    l *= r
                elif op == '/':
                    l //=r
                elif op == '(':
                    stack.append(total, op)
                elif op == ')':
                    pass
                print(l, op, r)
                r, op = None, None

            i += 1

        return my_algo, "=", l

print(basic_calulator().calculate("2 + 3 - 1 + 6 / 2"))
