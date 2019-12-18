# [h] dialogs.glyph

"""A collection of dialogs to do things to the current glyph."""

from . import align
import importlib
importlib.reload(align)

from . import nudge
importlib.reload(nudge)

from . import switch
importlib.reload(switch)

from . import interpolation_preview
importlib.reload(interpolation_preview)

# import

from .align import alignPointsDialog
from .nudge import nudgePointsDialog
from .switch import switchGlyphDialog
from .interpolation_preview import interpolationPreviewDialog

# export

__all__ = [
    'alignPointsDialog',
    'nudgePointsDialog',
    'switchGlyphDialog',
    'interpolationPreviewDialog',
]
