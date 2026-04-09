class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for token in tokens:
            print(res)
            if token == "*":
                pop1 = res.pop()
                pop2 = res.pop()
                cur = pop1 * pop2
                res.append(cur)
            elif token == "+":
                pop1 = res.pop()
                pop2 = res.pop()
                cur = pop1 + pop2
                res.append(cur)
            elif token == "-":
                pop1 = res.pop()
                pop2 = res.pop()
                cur = pop2 - pop1
                res.append(cur)
            elif token == "/":
                pop1 = res.pop()
                pop2 = res.pop()
                cur = int(pop2 / pop1)
                res.append(cur)
            else:
                res.append(int(token))

            
        return res[0]
            
        