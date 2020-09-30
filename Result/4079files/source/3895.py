import tensorflow as tf

from demeter.rl.common import TensorBuffer, np_utils
from demeter.rl import TransitionAlgorithm, Policy, Transition

__all__ = ['Reinforce']


class Reinforce(TransitionAlgorithm):

    def __init__(self,
                 actor: Policy,
                 policy_obj_model: tf.keras.Model,
                 optimizer: tf.train.Optimizer,
                 discount: float,
                 step_batch_size: int = None,
                 episode_batch_size: int = None):
        assert (step_batch_size is None) ^ (episode_batch_size is None)

        self.actor = actor
        self.policy_obj_model = policy_obj_model
        self.optimizer = optimizer
        self.discount = discount
        self.step_batch_size = step_batch_size
        self.episode_batch_size = episode_batch_size

        if self.episode_batch_size is None:
            self.steps = 0
        else:
            self.episodes = 0
        self.buffer = TensorBuffer()
        self.step_counter = tf.train.get_or_create_global_step()

    def transition_update(self, transition: Transition, *args, **kwargs) -> None:
        self._add_to_buffer(transition, **kwargs)

        if self.episode_batch_size is not None:
            if transition.terminated:
                if self.episodes >= self.episode_batch_size:
                    self._update_batch()
                self.episodes += 1
        else:
            if self.steps >= self.step_batch_size:
                self._update_batch()
            self.steps += 1

    def _update_batch(self) -> None:
        c_return = tf.convert_to_tensor(np_utils.discount_cum_sum(self.buffer['reward'].numpy(), self.discount))
        self.buffer.add_buffer('c_return', c_return)

        with tf.GradientTape() as tape:
            # TODO: allow variable name action and obs to be passed in
            action, dist_params, lgdense = self.actor.eval(obs={'obs': self.buffer['obs']}, action={'action': self.buffer['action']},
                                                           featurize_inputs=False)
            policy_obj = self.policy_obj_model(inputs={'lgdense': lgdense, 'c_return': self.buffer['c_return']})
            policy_loss = -policy_obj
        grads = tape.gradient(policy_loss, self.actor.variables)
        self.optimizer.apply_gradients(zip(grads, self.actor.variables), global_step=self.step_counter)
        self.buffer.clear_buffers()

    def _add_to_buffer(self, transition: Transition, **kwargs) -> None:
        obs, action = self.actor.features(transition.obs, transition.action)
        if not isinstance(obs, dict):
            obs = {'obs': obs}
        if not isinstance(action, dict):
            action = {'action': action}

        data = {**obs, **action}
        data['reward'] = tf.convert_to_tensor([[transition.reward]])
        self.buffer.add(data)
