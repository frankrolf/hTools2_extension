# [h] preview interpolation with another font

import hTools2.dialogs.glyph.interpolation_preview
import importlib
importlib.reload(hTools2.dialogs.glyph.interpolation_preview)

from hTools2.dialogs.glyph.interpolation_preview import interpolationPreviewDialog

interpolationPreviewDialog()
