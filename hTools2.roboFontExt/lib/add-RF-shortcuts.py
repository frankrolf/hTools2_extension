# [h] create shortcuts

"""Create RoboFont keyboard shortcuts for scripts in hTools2."""

import os
from mojo.UI import setScriptingMenuNamingShortKeyForPath, createModifier

shortcuts = [
    (   '1',    'actions',          'selected-glyphs/actions/actions.py',            ),
    (   'c',    'paint select',     'selected-glyphs/color/paint-select.py',         ),
    (   'g',    'gridfit',          'selected-glyphs/transform/gridfit.py',          ),
    (   'h',    'set width',        'selected-glyphs/metrics/set-width.py',          ),
    (   'i',    'interpolate',      'selected-glyphs/interpol/interpolate.py',       ),
    (   'k',    'mask',             'selected-glyphs/layers/mask.py',                ),
    (   'l',    'copy to layer',    'selected-glyphs/layers/copy-to-layer.py',       ),
    (   'm',    'move',             'selected-glyphs/transform/move.py',             ),
    (   'o',    'copy to mask',     'selected-glyphs/layers/copy-to-mask.py',        ),
    (   'p',    'copy paste',       'selected-glyphs/actions/copy-paste.py',         ),
    (   'r',    'mirror',           'selected-glyphs/transform/mirror.py',           ),
    (   's',    'scale',            'selected-glyphs/transform/scale.py',            ),
    (   't',    'shift',            'selected-glyphs/transform/shift.py',            ),
    (   'v',    'adjust',           'current-font/vmetrics/adjust.py',               ),
    (   'w',    'skew',             'selected-glyphs/transform/skew.py',             ),
]

scripts_folder = os.path.join(os.getcwd(), 'Scripts')

for shortcut in shortcuts:
    short_key, name, script_file = shortcut
    script_path = os.path.join(scripts_folder, script_file)
    modifier = createModifier(command=True, shift=True)
    if os.path.exists(script_path):
        # print 'creating shortcut for', script_path
        setScriptingMenuNamingShortKeyForPath(script_path, name, short_key, modifier)
