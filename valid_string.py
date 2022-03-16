def minRemoveToMakeValid(s: str) -> str:
        stack = []
        n = len(s)
        l = list(s)

        for i in range(n):
            if l[i] == '(':
                stack.append(i)
            elif l[i] == ')':
                if stack:
                    stack.pop()
                else:
                    l[i] = ""

        if stack:
            for i in stack:
                l[i] = ""
        return "".join(l)


my_sol = minRemoveToMakeValid("))((")
print(my_sol)
