from bolero.environment import OpenAiGym, gym_available
if not gym_available:
    from nose import SkipTest
    raise SkipTest("gym is not installed")
from bolero.behavior_search import MonteCarloRL
from bolero.controller import Controller
from nose.tools import assert_less, assert_equal
from nose import SkipTest


def test_mc_rl():
    env = OpenAiGym("FrozenLake-v0", render=False, seed=1)
    try:
        env.init()
    except ImportError:
        raise SkipTest("gym is not installed")
    bs = MonteCarloRL(env.get_discrete_action_space(), random_state=1)
    ctrl = Controller(environment=env, behavior_search=bs, n_episodes=10000,
                    finish_after_convergence=True)
    returns = ctrl.learn()
    assert_less(len(returns), 1000)
    beh = bs.get_best_behavior()
    rewards = ctrl.episode_with(beh)
    assert_equal(sum(rewards), 1.0)