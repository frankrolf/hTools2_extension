# [h] transform all open fonts

import hTools2.dialogs.all_fonts.actions
import importlib
importlib.reload(hTools2.dialogs.all_fonts.actions)

hTools2.dialogs.all_fonts.actions.actionsDialog()
