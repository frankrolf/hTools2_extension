# [h] import ufo into layer

import hTools2.dialogs.font.layer_import
import importlib
importlib.reload(hTools2.dialogs.font.layer_import)

from hTools2.dialogs.font.layer_import import importUFOIntoLayerDialog

importUFOIntoLayerDialog()
