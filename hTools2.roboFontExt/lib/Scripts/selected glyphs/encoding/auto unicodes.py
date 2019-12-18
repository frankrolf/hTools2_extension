# [h] auto unicodes

"""Automatically set unicode values for selected glyphs."""

import hTools2.modules.encoding
import importlib
importlib.reload(hTools2.modules.encoding)

# imports

try:
    from mojo.roboFont import CurrentFont
except:
    from fontParts.world import CurrentFont

from hTools2.modules.encoding import auto_unicode
from hTools2.modules.fontutils import get_glyphs
from hTools2.modules.messages import no_font_open, no_glyph_selected

# run

f = CurrentFont()

if f is not None:
    glyph_names = get_glyphs(f)
    if len(glyph_names) > 0:
        print('setting unicode for selected glyphs...\n')
        print('\t', end=' ')
        for glyph_name in glyph_names:
            print(glyph_name, end=' ')
            auto_unicode(f[glyph_name])
        print()
        print('\n...done.\n')
    # no glyph selected
    else:
        print(no_glyph_selected)

# no font open
else:
    print(no_font_open)
