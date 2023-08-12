from numpy import array, dot, inf
from scipy.integrate import quad as integration


class DiscreteRandomVariable:
    def __init__(self, variables: list, probabilities: list) -> None:
        """Be sure to put lists with accurate format"""
        if len(variables) != len(probabilities):
            raise Exception("List of Variables and Probabilities do not have same size")

        if sum(probabilities) != 1 or not all(x > 0 for x in probabilities):
            raise Exception("Probabilities' format is incorrect")

        if len(set(variables)) != len(variables):
            raise Exception("Variables are not all uniq")

        self.variables = array(variables)
        self.probabilities = array(probabilities)
        self.size = len(variables)

    def count_expected_value(self) -> float:
        """Counting expected value for Discrete Random Variable"""
        return float(dot(self.variables, self.probabilities))

    def count_expected_value_v2(self) -> float:
        result = 0
        for i in range(self.size):
            result += self.variables[i] * self.probabilities[i]
        return result


class ContinuousRandomVariable:
    def __init__(self, probability_density_function, left=0, right=1):
        """Put here Probability density function"""
        self.pdf = probability_density_function
        self.left = left  # needed only when you use count_expected_value_v2
        self.right = right  # needed only when you use count_expected_value_v2

    def count_expected_value(self):
        """Counting expected value for Continuous Random Variable"""
        xpdf = lambda x: x * self.pdf(x)
        return integration(xpdf, -inf, +inf)[0]

    '''Solving integration using Riemann method'''
    def count_expected_value_v2(self):
        number_of_dots = 1_000_000
        x_s = [i / number_of_dots * (self.right - self.left) for i in range(number_of_dots)]
        y_s = [self.pdf(x) for x in x_s]
        return (x_s[1] - x_s[0]) * dot(x_s, y_s)
