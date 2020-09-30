# (generated with --quick)

import dqn
import memory
from typing import Any, TextIO, Tuple, Type

DQNAgent: Type[dqn.DQNAgent]
Episode: Type[memory.Episode]
EpisodeHistory: Type[memory.EpisodeHistory]
ExperienceMemory: Type[memory.ExperienceMemory]
GameHistory: Type[memory.GameHistory]
MatchResults: Type[memory.MatchResults]
cv2: Any
datetime: module
maximum_filter: Any
np: module
os: module
sys: module
tf: Any

class AgentTrainer(object):
    BATCH_SIZE: Any
    EXPLORE: Any
    FINAL_EPSILON: Any
    FRAME_PER_ACTION: Any
    GAMMA: Any
    INITIAL_EPSILON: Any
    LOG_PERIOD: Any
    OBSERVE: Any
    action_count: Any
    agent: dqn.DQNAgent
    episode_history: memory.EpisodeHistory
    epsilon: Any
    game_history: memory.GameHistory
    gamma_pow: Any
    increment_step: Any
    last_action_index: Any
    match_playtime: Any
    match_reward: Any
    memory: memory.ExperienceMemory
    s_t: Any
    saver: Any
    session: Any
    step: Any
    summary_output: TextIO
    summary_writer: Any
    t: Any
    def __init__(self, config) -> None: ...
    def act(self) -> Any: ...
    def compute_epsilon(self, t) -> Any: ...
    def init_training(self) -> None: ...
    def load_model(self, path) -> None: ...
    def make_train_step(self) -> Tuple[Any, Any]: ...
    def process_frame(self, screen, reward, terminal) -> None: ...
    def reset_state(self, initial_state) -> None: ...
    def save_model(self, path) -> None: ...

def transformImage(image) -> Any: ...
