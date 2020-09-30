from nbp.bodies import BodyState as BodyState
from nbp.helpers.physics import calculate_position as calculate_position, calculate_velocity as calculate_velocity
from nbp.modifiers import Modifier

class DeltaTimeModifier(Modifier):
    @staticmethod
    def get_cli_arguments() -> list: ...
    def modify(self, state: BodyState) -> BodyState: ...
