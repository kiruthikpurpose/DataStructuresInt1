class Term:
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent

    def __str__(self):
        return f"{self.coefficient}X^{self.exponent}"

class PolynomialADT:
    def __init__(self):
        self.terms = []

    def add_term(self, coefficient, exponent):
        self.terms.append(Term(coefficient, exponent))

    def __str__(self):
        return ' + '.join(str(term) for term in self.terms)


num_terms = int(input())
polynomial = PolynomialADT()

for _ in range(num_terms):
    coefficient, exponent = map(int, input().split())
    polynomial.add_term(coefficient, exponent)

print(polynomial)
