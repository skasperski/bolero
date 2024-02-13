from .environment import Environment, ContextualEnvironment
from .set_context import SetContext
from .objective_functions import ObjectiveFunctionBase, ObjectiveFunction
from .contextual_objective_functions import ContextualObjectiveFunction
from .optimum_trajectory import OptimumTrajectory, OptimumTrajectoryCurbingObstacles
from .catapult import Catapult


__all__ = [
    "Environment", "ContextualEnvironment", "SetContext", "ObjectiveFunction",
    "ContextualObjectiveFunction", "OptimumTrajectory", "Catapult"]

from .openaigym import OpenAiGym, gym_available
__all__.append("gym_available")
if gym_available:
    __all__.append("OpenAiGym")