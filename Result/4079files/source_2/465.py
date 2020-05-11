from typing import Any, Callable, Dict, List, Tuple, Union

import tensorflow as tf

from demeter.rl.common import take_any
from demeter.rl import Policy


class DiscreteActor(Policy):

    def __init__(self,
                 dist_model: tf.keras.Model,
                 obs_features: Callable[[Any], Dict[str, tf.Tensor]] = None,
                 action_features: Callable[[Any], Dict[str, tf.Tensor]] = None):
        self.dist_model = dist_model
        self.obs_features = obs_features
        self.action_features = action_features

    def sample(self, obs: Any, featurize_inputs: bool = True) -> Any:
        """Sample an action for the given observation."""
        ofeat = self.features(obs=obs, featurize_inputs=featurize_inputs)
        dist_params = self.dist_model(inputs=take_any(ofeat))
        return self.sample_action(dist=dist_params)

    @staticmethod
    def sample_action(dist: Union[tf.Tensor, Dict[str, tf.Tensor]]) -> Any:
        cat_dist = tf.distributions.Categorical(probs=take_any(dist))
        return cat_dist.sample(1).numpy()[0][0]

    def log_pdf(self, action: Union[tf.Tensor, Dict[str, tf.Tensor]], dist: Union[str, Dict[str, tf.Tensor]]
                ) -> tf.Tensor:
        cat_dist = tf.distributions.Categorical(probs=take_any(dist))
        return tf.expand_dims(cat_dist.log_prob(take_any(action)), axis=1)

    def sample_eval(self, obs: Any, **kwargs) -> Dict[str, tf.Tensor]:
        pass

    def eval(self, obs: Any, action: Any, featurize_inputs: bool = True
             ) -> Tuple[Union[tf.Tensor, Dict[str, tf.Tensor]], Union[tf.Tensor, Dict[str, tf.Tensor]], tf.Tensor]:
        ofeat, afeat = self.features(obs=obs, action=action, featurize_inputs=featurize_inputs)
        dist_params = self.dist_model(inputs=take_any(ofeat))
        lgdense = self.log_pdf(action=take_any(afeat), dist=dist_params)
        return action, dist_params, lgdense

    def features(self, obs: Any = None, action: Any = None, featurize_inputs: bool = True) -> Any:
        ofeat = {}
        if obs is not None:
            if not featurize_inputs or self.obs_features is None:
                ofeat = obs
            else:
                ofeat = self.obs_features(obs)
            if action is None:
                return ofeat
        afeat = {}
        if action is not None:
            if not featurize_inputs or self.action_features is None:
                afeat = action
            else:
                afeat = self.action_features(action)
            if obs is None:
                return afeat
        return ofeat, afeat

    @property
    def variables(self) -> List[tf.Variable]:
        return self.dist_model.variables
