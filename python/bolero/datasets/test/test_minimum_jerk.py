import numpy as np
from bolero.datasets import make_minimum_jerk
from numpy.testing import assert_array_almost_equal
from nose.tools import (assert_raises_regexp, assert_greater_equal,
                        assert_less_equal)


def test_minimum_jerk_boundaries():
    random_state = np.random.RandomState(1)
    x0 = random_state.randn(2)
    g = x0 + random_state.rand(2)

    X, Xd, Xdd = make_minimum_jerk(x0, g)
    assert_array_almost_equal(X[:, 0, 0], x0)
    assert_array_almost_equal(Xd[:, 0, 0], np.zeros(2))
    assert_array_almost_equal(Xdd[:, 0, 0], np.zeros(2))
    assert_array_almost_equal(X[:, -1, 0], g)
    assert_array_almost_equal(Xd[:, -1, 0], np.zeros(2))
    assert_array_almost_equal(Xdd[:, -1, 0], np.zeros(2))

    for d in range(X.shape[0]):
        for t in range(X.shape[1]):
            assert_greater_equal(X[d, t, 0], x0[d])
            assert_less_equal(X[d, t, 0], g[d])

    assert_raises_regexp(ValueError, "Shape .* must be equal",
                         make_minimum_jerk, x0, np.zeros(1))
