import shesha.constants as conf
from shesha.sutra_wrap import Telescope as Telescope, carmaWrap_context as carmaWrap_context
from typing import Any

def target_init(ctxt: carmaWrap_context, telescope: Telescope, p_targets: list, p_atmos: conf.Param_atmos, p_tel: conf.Param_tel, p_geom: conf.Param_geom, dm: Any=..., brahma: Any=...) -> Any: ...
