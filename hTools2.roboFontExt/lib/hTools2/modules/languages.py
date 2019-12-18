#!/usr/bin/python
# -*- coding: utf-8 -*-

# imports

from . import encoding
import importlib
importlib.reload(encoding)

from .encoding import chars2psnames

# diacritics per language
# source: Diacritics Project
# http://diacritics.typo.cz/index.php?id=49

diacritics_chars = {
    'albanian' : [
        'ç ë',
        'Ç Ë',
    ],
    'bosnian' : [
        'č ć đ š ž',
        'Č Ć Đ Š Ž',
    ],
    'catalan' : [
        'à ç è é í ï ŀ ò ó ú ü',
        'À Ç È É Í Ï Ŀ Ò Ó Ú Ü',
    ],
    'croatian' : [
        'č ć đ š ž',
        'Č Ć Đ Š Ž',
    ],
    'czech' : [
        'á č ď é ě í ň ó ř š ť ú ů ý ž',
        'Á Č Ď É Ě Í Ň Ó Ř Š Ť Ú Ů Ý Ž',
    ],
    'danish' : [
        'å æ é ø á í ó ú ý',
        'Å Æ É Ø Á Í Ó Ú Ý',
    ],
    'dutch' : [
        'á é í ó ú à è ë ï ö ü ĳ',
        'Á É Í Ó Ú À È Ë Ï Ö Ü Ĳ',
    ],
    'estonian' : [
        'ä õ ö š ü ž',
        'Ä Õ Ö Š Ü Ž',
    ],
    'faroese' : [
        'á æ ð í ó ø ú ý',
        'Á Æ Ð Í Ó Ø Ú Ý',
    ],
    'finish' : [
        'å ä ö š ž',
        'Å Ä Ö Š Ž',
    ],
    'french' : [
        'à â æ ç è é ê ë î ï ô œ ù û ü ÿ',
        'À Â Æ Ç È É Ê Ë Î Ï Ô Œ Ù Û Ü Ÿ',
    ],
    'german' : [
        'ä ö ü ß',
        'Ä Ö Ü',
    ],
    'hungarian' : [
        'á é í ó ö ő ú ü ű',
        'Á É Í Ó Ö Ő Ú Ü Ű',
    ],
    'icelandic' : [
        'á æ ð é í ó ö þ ú ý',
        'Á Æ Ð É Í Ó Ö Þ Ú Ý',
    ],
    'irish' : [
        'á ḃ ċ ḋ é ḟ ġ ḣ í ṁ ó ṗ ṡ ṫ ú',
        'Á Ḃ Ċ Ḋ É Ḟ Ġ Ḣ Í Ṁ Ó Ṗ Ṡ Ṫ Ú',
    ],
    'latvian' : [
        'ā č ē ģ ī ķ ļ ņ š ū ž ō ŗ',
        'Ā Č Ē Ģ Ī Ķ Ļ Ņ Š Ū Ž Ō Ŗ',
    ],
    'lithuanian' : [
        'ą č ę ė į š ų ū ž',
        'Ą Č Ę Ė Į Š Ų Ū Ž',
    ],
    'maltese' : [
        'à ċ è ġ ħ ì î ò ù ż',
        'À Ċ È Ġ Ħ Ì Î Ò Ù Ż',
    ],
    'maori' : [
        'ā ē ī ō ū',
        'Ā Ē Ī Ō Ū',
    ],
    'norwegian' : [
        'æ ø å à é ê ó ò ô',
        'Æ Ø Å À É Ê Ó Ò Ô',
    ],
    'polish' : [
        'ą ć ę ł ń ó ś ż ź',
        'Ą Ć Ę Ł Ń Ó Ś Ż Ź',
    ],
    'portuguese' : [
        'à á â ã ç é ê í ó ô õ ú',
        'À Á Â Ã Ç É Ê Í Ó Ô Õ Ú ',
    ],
    'romanian' : [
        'â ă î ș ț',
        'Â Ă Î Ș Ț',
    ],
    'sanskrit' : [
        'ā ḍ ḥ ī ḷ ṁ ṅ ṇ ñ ṛ ṝ ś ṣ ṭ ū',
        'Ā Ḍ Ḥ Ī Ḷ Ṁ Ṅ Ṇ Ñ Ṛ Ṝ Ś Ṣ Ṭ Ū',
    ],
    'serbian' : [
        'č ć đ š ž',
        'Č Ć Đ Š Ž',
    ],
    'slovak' : [
        'á ä č ď é í ĺ ľ ň ó ô ŕ š ť ú ý ž',
        'Á Ä Č Ď É Í Ĺ Ľ Ň Ó Ô Ŕ Š Ť Ú Ý Ž',
    ],
    'slovenian' : [
        'č š ž',
        'Č Š Ž',
    ],
    'spanish' : [
        'á é í ó ú ü ñ',
        'Á É Í Ó Ú Ü Ñ',
    ],
    'swedish' : [
        'ä å é ö á à ë ü',
        'Ä Å É Ö Á À Ë Ü',
    ],
    'turkish' : [
        'â ç ğ î ı ö ş û ü',
        'Â Ç Ğ Î İ Ö Ş Û Ü',
    ],
    'welsh' : [
        'à â è é ê ë î ï ô ù û ü ÿ ẁ ẃ ẅ ỳ ý ŵ ŷ',
        'À Â È É Ê Ë Î Ï Ô Ù Û Ü Ÿ Ẁ Ẃ Ẅ Ỳ Ý Ŵ Ŷ',
    ],
}

# functions

def convert_chars_to_glyphnames(chars_dict):
    glyphnames = {}
    for lang in list(chars_dict.keys()):
        glyphnames[lang] = []
        # get lc/uc character strings
        lc, uc = chars_dict[lang]
        # get characters as lists
        lc_chars = lc.split()
        uc_chars = uc.split()
        # get glyph names from characters
        lc_glyph_names = chars2psnames(lc_chars)
        uc_glyph_names = chars2psnames(uc_chars)
        # append lists of glyph names to dict
        glyphnames[lang].append(lc_glyph_names)
        glyphnames[lang].append(uc_glyph_names)
    return glyphnames

def check_language_coverage(language, glyph_names):
    lc, uc = diacritics_glyphnames[language]
    lang_names = lc + uc
    # check matching glyphs
    not_in_font = []
    for lang_name in lang_names:
        if lang_name not in glyph_names:
            not_in_font.append(lang_name)
    # done
    return not_in_font

def check_languages_coverage(glyph_names, n=50):
    # check language support
    supported_langs = []
    not_supported_langs = {}
    for lang in list(diacritics_glyphnames.keys()):
        missing_glyphs = check_language_coverage(lang, glyph_names)
        if len(missing_glyphs) == 0:
            supported_langs.append(lang)
        else:
            not_supported_langs[lang] = missing_glyphs
    not_supported_ordered = list(not_supported_langs.keys())
    # print info
    print('fully supported languages:')
    print('-' * n)
    print('%s\n' % ' '.join(sorted(supported_langs)))
    print('not fully supported:')
    print('-' * n)
    print('%s\n' % ' '.join(sorted(not_supported_langs.keys())))
    print('missing glyphs for each language:')
    print('-' * n)
    for lang in sorted(not_supported_langs.keys()):
        print('%s (%s):' % (lang, len(not_supported_langs[lang])))
        print('%s\n' % ' '.join(not_supported_langs[lang]))

# constants

diacritics_glyphnames = convert_chars_to_glyphnames(diacritics_chars)
