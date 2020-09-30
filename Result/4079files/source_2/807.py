import gym
import pytest
import numpy as np

from demeter.rl.env import GymEnv


@pytest.fixture
def env():
    gym_env = gym.make('CartPole-v0')
    return GymEnv(gym_env=gym_env, render_on_step=False)


def test_transition(env: GymEnv):
    transition1 = env.execute(env.action_space.sample())
    assert transition1.next_obs is not None
    assert transition1.terminated is False
    assert transition1.reward == 1.0
    assert env.terminated is False
    assert env.last_reward == 1.0

    transition2 = env.execute(env.action_space.sample())
    np.testing.assert_array_equal(transition2.obs, transition1.next_obs)
    assert transition2.next_obs is not None
    assert transition2.terminated is False
    assert transition2.reward == 1.0
    assert env.terminated is False
    assert env.last_reward == 1.0


def test_reset(env: GymEnv):
    env.reset()
    assert env.terminated is False
    assert env.last_reward is False
