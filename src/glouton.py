# Exercice https://courses.21-learning.com/runestone/books/published/oci-2224-donc/classic-problems/01-knapsack-short.html#force-brute

from knapsack import KnapsackInstance, KnapsackSolver

class GloutonKnapsackSolver(KnapsackSolver):
    """
    >>> kp = KnapsackInstance(W=[13, 13, 13, 10, 24, 11], V=[2600, 2600, 2600, 500, 4500, 960], C=50)
    >>> bfs = BruteforceKnapsackSolver(kp)
    >>> Xopt = bfs.solve()
    >>> Xopt in [(0, 1, 1, 0, 1, 0), (1, 0, 1, 0, 1, 0), (1, 1, 0, 0, 1, 0)]
    True
    >>> bfs.value(Xopt)
    9700
    >>> bfs.weight(Xopt)
    50
    >>> bfs.weight(Xopt) <= bfs._inst.C
    True
KnapsackInstance(W=[13, 13, 13, 10, 24, 11], V=[2600, 2600, 2600, 500, 4500, 960], C=50)
    """
    
    def __init__(self, instance) -> None:
        # TODO: write the constructor by calling the parent class constructor
        ...

    
    def solve(self) -> tuple[int, ...]:
        # solve by glouton
        ratio = [(0, 0) * len(self.weight)]
        for i in range(len(self.weight)):
            ratio[i][0] = i
            ratio[i][1] = self.value[i] / self.weight[i]

        sorted_ratio = sorted(ratio, key = lambda x: x[1], reverse=True)
        bag = 0
        f = 0
        while bag < self.C:
            if bag + sorted_ratio[f][1] > self.C:
                break
            else:
                    

        return sol