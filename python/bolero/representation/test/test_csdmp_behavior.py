import os
import numpy as np
try:
    from bolero.representation import CartesianDMPBehavior
except ImportError:
    from nose import SkipTest
    raise SkipTest("dmp is not installed")
from bolero.datasets import make_minimum_jerk
from nose.tools import assert_equal, assert_raises_regexp
from numpy.testing import assert_array_equal, assert_array_almost_equal


CURRENT_PATH = os.sep.join(__file__.split(os.sep)[:-1])
CSDMP_CONFIG_FILE = CURRENT_PATH + os.sep + "cs_dmp_model.yaml"
if not CURRENT_PATH:
    CSDMP_CONFIG_FILE = "dmp_model.yaml"

zeroq = np.array([0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0])


def eval_loop(beh, xva):
    beh.set_inputs(xva)
    beh.step()
    beh.get_outputs(xva)


def test_csdmp_dimensions_do_not_match():
    beh = CartesianDMPBehavior()
    assert_raises_regexp(ValueError, "Number of inputs must be 7",
                         beh.init, 6, 7)
    assert_raises_regexp(ValueError, "Number of outputs must be 7",
                         beh.init, 7, 6)


def test_csdmp_default_dmp():
    beh = CartesianDMPBehavior()
    beh.init(7, 7)

    x = np.copy(zeroq)
    beh.reset()
    t = 0
    while beh.can_step():
        eval_loop(beh, x)
        t += 1
    assert_equal(t, 101)
    assert_array_equal(x, np.array([0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]))


def test_csdmp_from_config():
    beh = CartesianDMPBehavior(configuration_file=CSDMP_CONFIG_FILE)
    beh.init(7, 7)

    x = np.copy(zeroq)
    beh.reset()
    t = 0
    while beh.can_step():
        eval_loop(beh, x)
        t += 1
    assert_equal(t, 301)


def test_csdmp_get_set_params():
    beh = CartesianDMPBehavior()
    beh.init(7, 7)

    assert_equal(beh.get_n_params(), 50 * 6)
    params = beh.get_params()
    assert_array_equal(params, np.zeros(50 * 6))

    random_state = np.random.RandomState(0)
    expected_params = random_state.randn(50 * 6)
    beh.set_params(expected_params)

    actual_params = beh.get_params()
    assert_array_equal(actual_params, expected_params)


def test_csdmp_constructor_args():
    beh = CartesianDMPBehavior(execution_time=2)
    beh.init(7, 7)

    x = np.copy(zeroq)
    beh.reset()
    t = 0
    while beh.can_step():
        eval_loop(beh, x)
        t += 1
    assert_equal(t, 201)


def test_csdmp_metaparameter_not_permitted():
    beh = CartesianDMPBehavior()
    beh.init(7, 7)
    assert_raises_regexp(ValueError, "Meta parameter .* is not allowed",
                         beh.set_meta_parameters, ["unknown"], [None])


def test_csdmp_change_goal():
    beh = CartesianDMPBehavior()
    beh.init(7, 7)

    g = np.hstack((np.ones(3), np.array([np.pi, 1.0, 0.0, 0.0])))
    g[3:] /= np.linalg.norm(g[3:])
    beh.set_meta_parameters(["g", "qg"], [g[:3], g[3:]])

    x = np.copy(zeroq)
    beh.reset()
    while beh.can_step():
        eval_loop(beh, x)

    assert_array_almost_equal(x, g, decimal=3)


def test_csdmp_change_goal_velocity():
    dt = 0.002
    beh = CartesianDMPBehavior(dt=dt)
    beh.init(7, 7)

    beh.set_meta_parameters(["gd"], [np.ones(3)])

    x = np.copy(zeroq)
    beh.reset()
    while beh.can_step():
        x_prev = np.copy(x)
        eval_loop(beh, x)

    v = (x[:3] - x_prev[:3]) / dt

    assert_array_almost_equal(v, np.ones(3), decimal=2)


def test_csdmp_change_execution_time():
    beh = CartesianDMPBehavior()
    beh.init(7, 7)

    X1 = beh.trajectory()
    beh.set_meta_parameters(["execution_time"], [2.0])
    X2 = beh.trajectory()
    assert_equal(X2.shape[0], 201)
    assert_array_almost_equal(X1, X2[::2])


def test_csdmp_change_weights():
    beh = CartesianDMPBehavior()
    beh.init(7, 7)

    beh.set_params(np.ones(50 * 6))

    x = np.copy(zeroq)
    beh.reset()
    while beh.can_step():
        eval_loop(beh, x)

    assert_array_almost_equal(x, zeroq, decimal=3)


def test_csdmp_set_meta_params_before_init():
    beh = CartesianDMPBehavior()

    x0 = np.ones(3) * 0.43
    g = np.ones(3) * -0.21
    gd = np.ones(3) * 0.12

    beh.set_meta_parameters(["x0", "g", "gd"], [x0, g, gd])
    beh.init(7, 7)

    x = np.zeros(7)
    x[:3] = x0

    beh.reset()
    t = 0
    while beh.can_step():
        eval_loop(beh, x)
        t += 1

    assert_array_almost_equal(x[:3], g, decimal=3)


def test_csdmp_more_steps_than_allowed():
    beh = CartesianDMPBehavior()
    beh.init(7, 7)

    x = np.copy(zeroq)
    beh.reset()
    while beh.can_step():
        eval_loop(beh, x)

    last_x = x.copy()
    eval_loop(beh, x)

    assert_array_equal(x, last_x)


def test_csdmp_imitate():
    x0, g, execution_time, dt = np.zeros(3), np.ones(3), 1.0, 0.001

    beh = CartesianDMPBehavior(execution_time, dt, 20)
    beh.init(7, 7)
    beh.set_meta_parameters(["x0", "g"], [x0, g])

    X_demo = make_minimum_jerk(x0, g, execution_time, dt)[0]
    X_rot = np.tile(zeroq[3:], (X_demo.shape[1], 1)).T
    X_demo = np.vstack((X_demo[:, :, 0], X_rot))[:, :, np.newaxis][:, :, 0]

    # Without regularization
    beh.imitate(X_demo)
    X = beh.trajectory()
    assert_array_almost_equal(X_demo.T, X, decimal=2)

    # With alpha > 0
    beh.imitate(X.T, alpha=1.0)
    X = beh.trajectory()
    assert_array_almost_equal(X_demo.T, X, decimal=3)

    # Self-imitation
    beh.imitate(X.T)
    X2 = beh.trajectory()
    assert_array_almost_equal(X2, X, decimal=3)


def test_csdmp_save_and_load():
    beh_original = CartesianDMPBehavior(
        execution_time=0.853, dt=0.001, n_features=10)
    beh_original.init(7, 7)

    x0 = np.array([1.27, 3.41, 2.72])
    q0 = np.array([1.23, 2.33, 8.32, 9.29])
    q0 /= np.linalg.norm(q0)
    g = np.array([3.21, 9.34, 2.93])
    qg = np.array([2.19, 2.39, 2.94, 9.32])
    qg /= np.linalg.norm(qg)
    beh_original.set_meta_parameters(
        ["x0", "q0", "g", "qg"],
        [x0, q0, g, qg])

    x = np.hstack((x0, q0))
    beh_original.reset()
    t = 0
    while beh_original.can_step():
        eval_loop(beh_original, x)
        if t == 0:
            assert_array_almost_equal(x, np.hstack((x0, q0)))
        t += 1
    assert_array_almost_equal(x, np.hstack((g, qg)), decimal=2)
    assert_equal(t, 854)
    assert_equal(beh_original.get_n_params(), 6 * 10)

    try:
        beh_original.save("csdmp_tmp.yaml")
        beh_original.save_config("tmp_csdmp_config.yaml")

        beh_loaded = CartesianDMPBehavior(configuration_file="csdmp_tmp.yaml")
        beh_loaded.init(7, 7)
        beh_loaded.load_config("tmp_csdmp_config.yaml")
    finally:
        if os.path.exists("csdmp_tmp.yaml"):
            os.remove("csdmp_tmp.yaml")
        if os.path.exists("tmp_csdmp_config.yaml"):
            os.remove("tmp_csdmp_config.yaml")

    x = np.hstack((x0, q0))
    beh_loaded.reset()
    t = 0
    while beh_loaded.can_step():
        eval_loop(beh_loaded, x)
        if t == 0:
            assert_array_almost_equal(x, np.hstack((x0, q0)))
        t += 1
    assert_array_almost_equal(x, np.hstack((g, qg)), decimal=2)
    assert_equal(t, 854)
    assert_equal(beh_loaded.get_n_params(), 6 * 10)
