class Solution:
    def diffWaysToCompute(self, expression: str):
        res = []
        for i, v in enumerate(expression):
            if v == '*' or v == '+' or v == '-':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])

                for i in left:
                    for j in right:
                        if v == '*':
                            res.append(i * j)
                        elif v == '-':
                            res.append(i - j)
                        else:
                            res.append(i + j)

        return res or [int(expression)]
        print(res or [int(expression)])