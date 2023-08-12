from random_variables import DiscreteRandomVariable, ContinuousRandomVariable


if __name__ == '__main__':
    a = DiscreteRandomVariable([1, 2], [0.5, 0.5])
    print(a.count_expected_value())

    # F = lambda x: 0 if x < 0 else 1 if x > 2 else (3 * x * x + 1) / 10
    func = lambda x: (3 * x * x + 1) / 10 if 0 <= x <= 2 else 0

    b = ContinuousRandomVariable(probability_density_function=func)
    print(b.count_expected_value())

    b = ContinuousRandomVariable(probability_density_function=func, left=0, right=2)
    print(b.count_expected_value_v2())
