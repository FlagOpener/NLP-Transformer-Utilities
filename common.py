alphabet = {
    'A' : 'A',
    'B' : 'B',
    'C' : 'C',
    'D' : 'D',
    'E' : 'E',
    'F' : 'F',
    'G' : 'G',
    'H' : 'H',
    'I' : 'I',
    'J' : 'J',
    'K' : 'K',
    'L' : 'L',
    'M' : 'M',
    'N' : 'N',
    'O' : 'O',
    'P' : 'P',
    'Q' : 'Q',
    'R' : 'R',
    'S' : 'S',
    'T' : 'T',
    'U' : 'U',
    'V' : 'V',
    'W' : 'W',
    'X' : 'X',
    'Y' : 'Y',
    'Z' : 'Z',
    'Ä' : 'Ä',
    'Ö' : 'Ö',
    'Ü' : 'Ü',
    'ß' : 'ß',
    'a' : 'a',
    'b' : 'b',
    'c' : 'c',
    'd' : 'd',
    'e' : 'e',
    'f' : 'f',
    'g' : 'g',
    'h' : 'h',
    'i' : 'i',
    'j' : 'j',
    'k' : 'k',
    'l' : 'l',
    'm' : 'm',
    'n' : 'n',
    'o' : 'o',
    'p' : 'p',
    'q' : 'q',
    'r' : 'r',
    's' : 's',
    't' : 't',
    'u' : 'u',
    'v' : 'v',
    'w' : 'w',
    'x' : 'x',
    'y' : 'y',
    'z' : 'z',
    'ä' : 'ä',
    'ö' : 'ö',
    'ü' : 'ü',
    '0' : '0',
    '1' : '1',
    '2' : '2',
    '3' : '3',
    '4' : '4',
    '5' : '5',
    '6' : '6',
    '7' : '7',
    '8' : '8',
    '9' : '9',
    '"' : '"',
    ';' : ';',
    ' ' : ' ',
    ':' : ':',
    ',' : ',',
    '.' : '.',
    '!' : '!',
    '$' : '$',
    '%' : '%',
    '&' : '&',
    '*' : '*',
    '(' : '(',
    ')' : ')',
    '-' : '-',
    '+' : '+',
    '/' : '/',
    '=' : '=',
    '?' : '?',
    '[' : '[',
    ']' : ']',
    '|' : '|',
    "'" : "'",
    '\n': '\n',
    '#' : '#',
    '<' : '<',
    '>' : '>',
    '@' : '@',
    '^' : '^',
    '_' : '_',
    u'\xa0' : ' ', #  
    u'\xa7' : '§', # §
    u'\xa9' : '', # ©
    u'\xab' : '', # «
    u'\xad' : '', # ­
    u'\xb0' : '', # °
    u'\xb2' : '', # ²
    u'\xb3' : '', # ³
    u'\xb4' : "'", # ´
    u'\xb7' : '', # ·
    u'\xbb' : '', # »
    u'\xbd' : '', # ½
    u'\xc4' : 'Ä', # Ä
    u'\xd6' : 'Ö', # Ö
    u'\xdc' : 'Ü', # Ü
    u'\xdf' : 'ß', # ß
    u'\xe0' : '', # à
    u'\xe1' : '', # á
    u'\xe4' : 'ä', # ä
    u'\xe7' : '', # ç
    u'\xe9' : '', # é
    u'\xed' : '', # í
    u'\xf1' : '', # ñ
    u'\xf3' : '', # ó
    u'\xf6' : 'ö', # ö
    u'\xfc' : 'ü', # ü
    u'\u011b' : '', # ě
    u'\u011f' : '', # ğ
    u'\u0121' : '', # ġ
    u'\u0142' : '', # ł
    u'\u0151' : 'ö', # ő
    u'\u017c' : '', # ż
    u'\u0308' : '"', # ̈
    u'\u0336' : '_', # ̶
    u'\u200b' : '', # ​
    u'\u2013' : '_', # –
    u'\u2014' : '_', # —
    u'\u2018' : "'", # ‘
    u'\u2019' : "'", # ’
    u'\u201a' : ',', # ‚
    u'\u201c' : '"', # “
    u'\u201d' : '"', # ”
    u'\u201e' : '"', # „
    u'\u2026' : '...', # …
    u'\u2039' : '', # ‹
    u'\u203a' : '', # ›
    u'\u2082' : '', # ₂
    u'\u20ac' : '€', # €
    u'\u25b2' : '', # ▲
    u'\u25ba' : '', # ►
    u'\u25bc' : '', # ▼
    u'\u25c4' : '', # ◄
    u'\u2605' : '', # ★
    u'\u2661' : '', # ♡
    u'\u300b' : '', # 》
    u'\U0001d400' : 'A', # 𝐀
    u'\U0001d403' : 'D', # 𝐃
    u'\U0001d411' : 'R', # 𝐑
    u'\U0001d416' : 'W', # 𝐖
    u'\U0001d41a' : 'a', # 𝐚
    u'\U0001d41b' : 'b', # 𝐛
    u'\U0001d41c' : 'c', # 𝐜
    u'\U0001d41d' : 'd', # 𝐝
    u'\U0001d41e' : 'e', # 𝐞
    u'\U0001d41f' : 'f', # 𝐟
    u'\U0001d420' : 'g', # 𝐠
    u'\U0001d421' : 'h', # 𝐡
    u'\U0001d422' : 'i', # 𝐢
    u'\U0001d425' : 'l', # 𝐥
    u'\U0001d426' : 'm', # 𝐦
    u'\U0001d427' : 'n', # 𝐧
    u'\U0001d428' : 'o', # 𝐨
    u'\U0001d42b' : 'r', # 𝐫
    u'\U0001d42c' : 's', # 𝐬
    u'\U0001d42d' : 't', # 𝐭
    u'\U0001d42e' : 'u', # 𝐮
    u'\U0001d42f' : 'v', # 𝐯
    u'\U0001d46f' : 'H', # 𝑯
    u'\U0001d472' : 'K', # 𝑲
    u'\U0001d482' : 'a', # 𝒂
    u'\U0001d484' : 'c', # 𝒄
    u'\U0001d486' : 'e', # 𝒆
    u'\U0001d487' : 'f', # 𝒇
    u'\U0001d488' : 'g', # 𝒈
    u'\U0001d489' : 'h', # 𝒉
    u'\U0001d48d' : 'l', # 𝒍
    u'\U0001d48e' : 'm', # 𝒎
    u'\U0001d48f' : 'n', # 𝒏
    u'\U0001d490' : 'o', # 𝒐
    u'\U0001d494' : 'g', # 𝒔
    u'\U0001d495' : 't', # 𝒕
    u'\U0001d496' : 'u', # 𝒖
    u'\U0001d49b' : 'z', # 𝒛
    u'\U0001d4d8' : 'I', # 𝓘
    u'\U0001d4ed' : 'd', # 𝓭
    u'\U0001d4f0' : 'g', # 𝓰
    u'\U0001d4f2' : 'i', # 𝓲
    u'\U0001d4f7' : '', # 𝓷
    u'\U0001d4f8' : '', # 𝓸
    u'\U0001d53b' : '', # 𝔻
    u'\U0001d546' : '', # 𝕆
    u'\U0001d552' : '', # 𝕒
    u'\U0001d553' : '', # 𝕓
    u'\U0001d556' : '', # 𝕖
    u'\U0001d55c' : '', # 𝕜
    u'\U0001d55e' : 'm', # 𝕞
    u'\U0001d560' : '', # 𝕠
    u'\U0001d563' : 'r', # 𝕣
    u'\U0001d565' : 't', # 𝕥
    u'\U0001d56d' : '', # 𝕭
    u'\U0001d586' : 'a', # 𝖆
    u'\U0001d58a' : 'e', # 𝖊
    u'\U0001d58d' : 'h', # 𝖍
    u'\U0001d590' : '', # 𝖐
    u'\U0001d591' : '', # 𝖑
    u'\U0001d593' : 'u', # 𝖓
    u'\U0001d594' : 'o', # 𝖔
    u'\U0001d597' : 'r', # 𝖗
    u'\U0001d59a' : 'u', # 𝖚
    u'\U0001d645' : 'J', # 𝙅
    u'\U0001d656' : 'a', # 𝙖
    u'\U0001d659' : 'd', # 𝙙
    u'\U0001d65a' : 'e', # 𝙚
    u'\U0001d65d' : 'h', # 𝙝
    u'\U0001d65e' : 'l', # 𝙞
    u'\U0001d661' : 'l', # 𝙡
    u'\U0001d663' : 'n', # 𝙣
    u'\U0001d667' : 'r', # 𝙧
    u'\U0001d668' : 's', # 𝙨
    u'\U0001d66a' : 'u', # 𝙪
    u'\U0001d66b' : 'v', # 𝙫
    u'\U0001d66f' : 'z', # 𝙯
    u'\U0001d7d8' : '', # 𝟘
    u'\U0001d7d9' : '', # 𝟙
    u'\U0001d7de' : '', # 𝟞
    u'\U0001f44d' : '', # 👍
    u'\U000e0062' : '', # 󠁢
    u'\U000e0063' : '', # 󠁣
    u'\U000e0067' : '', # 󠁧
    u'\U000e0073' : '', # 󠁳
    u'\U000e0074' : '', # 󠁴
    u'`' : "'", # `
    u'~' : '~', # ~
    u'\\' : '\\', # \
    u'{' : '{', # {
    u'}' : '}', # }
    u'\x80' : '', # 
    u'\x84' : '', # 
    u'\x93' : '', # 
    u'\x94' : '', # 
    u'\x96' : '', # 
    u'\xa3' : '£', # £
    u'\xac' : '', # ¬
    u'\xaf' : '', # ¯
    u'\xb5' : 'µ', # µ
    u'\xb9' : '', # ¹
    u'\xbc' : '', # ¼
    u'\xbf' : '', # ¿
    u'\xc5' : '', # Å
    u'\xc7' : '', # Ç
    u'\xc8' : '', # È
    u'\xc9' : '', # É
    u'\xd3' : '', # Ó
    u'\xd7' : '', # ×
    u'\xd8' : '', # Ø
    u'\xe2' : '', # â
    u'\xe3' : '', # ã
    u'\xe5' : '', # å
    u'\xe8' : '', # è
    u'\xea' : '', # ê
    u'\xeb' : '', # ë
    u'\xec' : '', # ì
    u'\xef' : '', # ï
    u'\xf2' : '', # ò
    u'\xf4' : '', # ô
    u'\xf5' : '', # õ
    u'\xf8' : '', # ø
    u'\xf9' : '', # ù
    u'\xfa' : '', # ú
    u'\xfd' : '', # ý
    u'\u0105' : '', # ą
    u'\u0107' : '', # ć
    u'\u010d' : '', # č
    u'\u010f' : '', # ď
    u'\u0130' : '', # İ
    u'\u0131' : '', # ı
    u'\u0139' : '', # Ĺ
    u'\u0144' : '', # ń
    u'\u014d' : '', # ō
    u'\u0153' : '', # œ
    u'\u015b' : '', # ś
    u'\u015e' : '', # Ş
    u'\u015f' : '', # ş
    u'\u0160' : '', # Š
    u'\u0161' : '', # š
    u'\u016b' : '', # ū
    u'\u017d' : '', # Ž
    u'\u017e' : '', # ž
    u'\u0219' : '', # ș
    u'\u03bc' : '', # μ
    u'\u0410' : '', # А
    u'\u0413' : '', # Г
    u'\u041c' : '', # М
    u'\u041d' : '', # Н
    u'\u041e' : '', # О
    u'\u0420' : '', # Р
    u'\u0421' : '', # С
    u'\u0422' : '', # Т
    u'\u0424' : '', # Ф
    u'\u0425' : '', # Х
    u'\u0427' : '', # Ч
    u'\u042c' : '', # Ь
    u'\u0430' : '', # а
    u'\u0431' : '', # б
    u'\u0432' : '', # в
    u'\u0433' : '', # г
    u'\u0434' : '', # д
    u'\u0435' : '', # е
    u'\u0437' : '', # з
    u'\u0438' : '', # и
    u'\u0439' : '', # й
    u'\u043a' : '', # к
    u'\u043b' : '', # л
    u'\u043c' : '', # м
    u'\u043d' : '', # н
    u'\u043e' : '', # о
    u'\u043f' : '', # п
    u'\u0440' : '', # р
    u'\u0441' : '', # с
    u'\u0442' : '', # т
    u'\u0443' : '', # у
    u'\u0444' : '', # ф
    u'\u0445' : '', # х
    u'\u0446' : '', # ц
    u'\u0447' : '', # ч
    u'\u0448' : '', # ш
    u'\u0449' : '', # щ
    u'\u044b' : '', # ы
    u'\u044c' : '', # ь
    u'\u044e' : '', # ю
    u'\u044f' : '', # я
    u'\u0456' : '', # і
    u'\u061f' : '', # ؟
    u'\u0626' : '', # ئ
    u'\u0627' : '', # ا
    u'\u0628' : '', # ب
    u'\u0629' : '', # ة
    u'\u062a' : '', # ت
    u'\u062f' : '', # د
    u'\u0630' : '', # ذ
    u'\u0631' : '', # ر
    u'\u0632' : '', # ز
    u'\u0633' : '', # س
    u'\u0634' : '', # ش
    u'\u0635' : '', # ص
    u'\u0637' : '', # ط
    u'\u0639' : '', # ع
    u'\u063a' : '', # غ
    u'\u0641' : '', # ف
    u'\u0642' : '', # ق
    u'\u0644' : '', # ل
    u'\u0645' : '', # م
    u'\u0646' : '', # ن
    u'\u0647' : '', # ه
    u'\u0648' : '', # و
    u'\u064a' : '', # ي
    u'\u1e9e' : '', # ẞ
    u'\u2020' : '', # †
    u'\u2022' : '', # •
    u'\u2033' : '', # ″
    u'\u2122' : '', # ™
    u'\u2192' : '', # →
    u'\u21c5' : '', # ⇅
    u'\u2211' : '', # ∑
    u'\u2212' : '', # −
    u'\u2217' : '', # ∗
    u'\u2219' : '', # ∙
    u'\u221a' : '', # √
    u'\u221e' : '', # ∞
    u'\u2260' : '', # ≠
    u'\u2265' : '', # ≥
    u'\u226b' : '', # ≫
    u'\u2588' : '', # █
    u'\u2606' : '', # ☆
    u'\u263b' : '', # ☻
    u'\u2665' : '', # ♥
    u'\u2713' : '', # ✓
    u'\u27a4' : '', # ➤
    u'\u2800' : '', # ⠀
    u'\u30c4' : '', # ツ
    u'\u4e3a' : '', # 为
    u'\u4e5f' : '', # 也
    u'\u4e86' : '', # 了
    u'\u4eba' : '', # 人
    u'\u4ed6' : '', # 他
    u'\u4ee5' : '', # 以
    u'\u4eec' : '', # 们
    u'\u4fb5' : '', # 侵
    u'\u4fe1' : '', # 信
    u'\u5168' : '', # 全
    u'\u53ef' : '', # 可
    u'\u5b89' : '', # 安
    u'\u5b8c' : '', # 完
    u'\u5c01' : '', # 封
    u'\u5e9c' : '', # 府
    u'\u5f97' : '', # 得
    u'\u606f' : '', # 息
    u'\u653f' : '', # 政
    u'\u72af' : '', # 犯
    u'\u7684' : '', # 的
    u'\u79c1' : '', # 私
    u'\u9501' : '', # 锁
    u'\u9690' : '', # 隐
    u'\ufb00' : '', # ﬀ
    u'\ufb01' : '', # ﬁ
    u'\ufb02' : '', # ﬂ
    u'\ufeff' : '', # ﻿
    u'\uff0c' : '', # ，

    u'\U0001d401' : '', # 𝐁
    u'\U0001d424' : '', # 𝐤
    u'\U0001d429' : '', # 𝐩
    u'\U0001f592' : '', # 🖒
    u'\x7f' : '', # 
    u'\x90' : '', # 
    u'\x91' : '', # 
    u'\x92' : '', # 
    u'\x97' : '', # 
    u'\x9a' : '', # 
    u'\xa1' : '', # ¡
    u'\xa2' : '', # ¢
    u'\xa8' : '"', # ¨
    u'\xaa' : '', # ª
    u'\xae' : '(R)', # ®
    u'\xb1' : '+-', # ±
    u'\xb8' : '', # ¸
    u'\xba' : '', # º
    u'\xbe' : '', # ¾
    u'\xc0' : '', # À
    u'\xc1' : '', # Á
    u'\xc2' : '', # Â
    u'\xc3' : 'Ä', # Ã
    u'\xc6' : '', # Æ
    u'\xca' : '', # Ê
    u'\xcb' : '', # Ë
    u'\xcd' : '', # Í
    u'\xce' : '', # Î
    u'\xd1' : '', # Ñ
    u'\xd2' : '', # Ò
    u'\xd4' : '', # Ô
    u'\xd5' : 'Ö', # Õ
    u'\xda' : '', # Ú
    u'\xdb' : '', # Û
    u'\xde' : '', # Þ
    u'\xe6' : '', # æ
    u'\xee' : '', # î
    u'\xf0' : '', # ð
    u'\xf7' : '/', # ÷
    u'\xfb' : '', # û
    u'\xfe' : '', # þ
    u'\u0100' : '', # Ā
    u'\u0101' : '', # ā
    u'\u0103' : '', # ă
    u'\u0106' : '', # Ć
    u'\u010c' : '', # Č
    u'\u010e' : '', # Ď
    u'\u0110' : '', # Đ
    u'\u0111' : '', # đ
    u'\u0113' : '', # ē
    u'\u0115' : '', # ĕ
    u'\u0117' : '', # ė
    u'\u0118' : '', # Ę
    u'\u0119' : '', # ę
    u'\u011e' : '', # Ğ
    u'\u0123' : '', # ģ
    u'\u0126' : '', # Ħ
    u'\u0129' : '', # ĩ
    u'\u012b' : '', # ī
    u'\u0136' : '', # Ķ
    u'\u013a' : '', # ĺ
    u'\u013c' : '', # ļ
    u'\u0141' : '', # Ł
    u'\u0146' : '', # ņ
    u'\u0148' : '', # ň
    u'\u014c' : '', # Ō
    u'\u014f' : '', # ŏ
    u'\u0150' : 'Ö', # Ő
    u'\u0152' : '', # Œ
    u'\u0155' : '', # ŕ
    u'\u0159' : '', # ř
    u'\u015a' : '', # Ś
    u'\u0163' : '', # ţ
    u'\u0165' : '', # ť
    u'\u0169' : '', # ũ
    u'\u016f' : '', # ů
    u'\u0170' : 'Ü', # Ű
    u'\u0171' : 'ü', # ű
    u'\u017a' : '', # ź
    u'\u017b' : '', # Ż
    u'\u017f' : '', # ſ
    u'\u01a1' : '', # ơ
    u'\u01a2' : '', # Ƣ
    u'\u01b0' : '', # ư
    u'\u01bc' : '', # Ƽ
    u'\u01c4' : '', # Ǆ
    u'\u01eb' : '', # ǫ
    u'\u0201' : '', # ȁ
    u'\u0218' : '', # Ș
    u'\u021b' : '', # ț
    u'\u022c' : '', # Ȭ
    u'\u0250' : '', # ɐ
    u'\u0254' : '', # ɔ
    u'\u0259' : '', # ə
    u'\u025b' : '', # ɛ
    u'\u0280' : '', # ʀ
    u'\u0281' : '', # ʁ
    u'\u0283' : '', # ʃ
    u'\u028a' : '', # ʊ
    u'\u028c' : '', # ʌ
    u'\u0294' : '', # ʔ
    u'\u0296' : '', # ʖ
    u'\u0298' : '', # ʘ
    u'\u02a1' : '', # ʡ
    u'\u02a2' : '', # ʢ
    u'\u02a6' : '', # ʦ
    u'\u02ad' : '', # ʭ
    u'\u02bc' : "'", # ʼ
    u'\u02c8' : "'", # ˈ
    u'\u02ca' : "'", # ˊ
    u'\u02cb' : "'", # ˋ
    u'\u02cc' : ',', # ˌ
    u'\u02d0' : ':', # ː
    u'\u02d1' : '', # ˑ
    u'\u02d6' : '', # ˖
    u'\u0300' : "'", # ̀
    u'\u0301' : "'", # ́
    u'\u0302' : '^', # ̂
    u'\u0306' : '', # ̆
    u'\u032f' : '', # ̯
    u'\u035c' : '', # ͜
    u'\u0361' : '', # ͡
    u'\u0366' : '', # ͦ
    u'\u0391' : '', # Α
    u'\u0393' : '', # Γ
    u'\u0394' : '', # Δ
    u'\u039a' : '', # Κ
    u'\u039c' : '', # Μ
    u'\u039d' : '', # Ν
    u'\u039f' : '', # Ο
    u'\u03a0' : '', # Π
    u'\u03a2' : '', # ΢
    u'\u03a3' : '', # Σ
    u'\u03a4' : '', # Τ
    u'\u03a6' : '', # Φ
    u'\u03ac' : '', # ά
    u'\u03ad' : '', # έ
    u'\u03ae' : '', # ή
    u'\u03af' : '', # ί
    u'\u03b1' : '', # α
    u'\u03b2' : '', # β
    u'\u03b3' : '', # γ
    u'\u03b4' : '', # δ
    u'\u03b5' : '', # ε
    u'\u03b6' : '', # ζ
    u'\u03b7' : '', # η
    u'\u03b9' : '', # ι
    u'\u03ba' : '', # κ
    u'\u03bb' : '', # λ
    u'\u03bd' : '', # ν
    u'\u03bf' : '', # ο
    u'\u03c0' : '', # π
    u'\u03c1' : '', # ρ
    u'\u03c2' : '', # ς
    u'\u03c3' : '', # σ
    u'\u03c4' : '', # τ
    u'\u03c5' : '', # υ
    u'\u03c6' : '', # φ
    u'\u03c7' : '', # χ
    u'\u03c9' : '', # ω
    u'\u03cb' : '', # ϋ
    u'\u03cc' : '', # ό
    u'\u03cd' : '', # ύ
    u'\u03ce' : '', # ώ
    u'\u03df' : '', # ϟ
    u'\u0401' : '', # Ё
    u'\u0404' : '', # Є
    u'\u0406' : '', # І
    u'\u0411' : '', # Б
    u'\u0412' : '', # В
    u'\u0414' : '', # Д
    u'\u0415' : '', # Е
    u'\u0416' : '', # Ж
    u'\u0417' : '', # З
    u'\u0418' : '', # И
    u'\u0419' : '', # Й
    u'\u041a' : '', # К
    u'\u041b' : '', # Л
    u'\u041f' : '', # П
    u'\u0423' : '', # У
    u'\u0426' : '', # Ц
    u'\u0428' : '', # Ш
    u'\u0429' : '', # Щ
    u'\u042d' : '', # Э
    u'\u042e' : '', # Ю
    u'\u042f' : '', # Я
    u'\u0436' : '', # ж
    u'\u044d' : '', # э
    u'\u0451' : '', # ё
    u'\u0454' : '', # є
    u'\u0455' : '', # ѕ
    u'\u0457' : '', # ї
    u'\u0482' : '', # ҂
    u'\u0490' : '', # Ґ
    u'\u0491' : '', # ґ
    u'\u0498' : '', # Ҙ
    u'\u04ab' : '', # ҫ
    u'\u04af' : '', # ү
    u'\u04f4' : '', # Ӵ
    u'\u053c' : '', # Լ
    u'\u0541' : '', # Ձ
    u'\u0565' : '', # ե
    u'\u056e' : '', # ծ
    u'\u057d' : '', # ս
    u'\u0584' : '', # ք
    u'\u05b0' : '', # ְ
    u'\u05b4' : '', # ִ
    u'\u05b5' : '', # ֵ
    u'\u05b6' : '', # ֶ
    u'\u05b7' : '', # ַ
    u'\u05b8' : '', # ָ
    u'\u05b9' : '', # ֹ
    u'\u05bb' : '', # ֻ
    u'\u05bc' : '', # ּ
    u'\u05bf' : '', # ֿ
    u'\u05c1' : '', # ׁ
    u'\u05d0' : '', # א
    u'\u05d1' : '', # ב
    u'\u05d2' : '', # ג
    u'\u05d3' : '', # ד
    u'\u05d4' : '', # ה
    u'\u05d5' : '', # ו
    u'\u05d6' : '', # ז
    u'\u05d7' : '', # ח
    u'\u05d8' : '', # ט
    u'\u05d9' : '', # י
    u'\u05db' : '', # כ
    u'\u05dc' : '', # ל
    u'\u05dd' : '', # ם
    u'\u05de' : '', # מ
    u'\u05df' : '', # ן
    u'\u05e0' : '', # נ
    u'\u05e1' : '', # ס
    u'\u05e2' : '', # ע
    u'\u05e3' : '', # ף
    u'\u05e4' : '', # פ
    u'\u05e5' : '', # ץ
    u'\u05e6' : '', # צ
    u'\u05e7' : '', # ק
    u'\u05e8' : '', # ר
    u'\u05e9' : '', # ש
    u'\u05ea' : '', # ת
    u'\u05eb' : '', # ׫
    u'\u060c' : '', # ،
    u'\u0622' : '', # آ
    u'\u0623' : '', # أ
    u'\u0625' : '', # إ
    u'\u062b' : '', # ث
    u'\u062c' : '', # ج
    u'\u062d' : '', # ح
    u'\u062e' : '', # خ
    u'\u0636' : '', # ض
    u'\u0643' : '', # ك
    u'\u0649' : '', # ى
    u'\u0661' : '', # ١
    u'\u0665' : '', # ٥
    u'\u067e' : '', # پ
    u'\u0686' : '', # چ
    u'\u068a' : '', # ڊ
    u'\u06a9' : '', # ک
    u'\u06aa' : '', # ڪ
    u'\u06ab' : '', # ګ
    u'\u06af' : '', # گ
    u'\u06bf' : '', # ڿ
    u'\u06cc' : '', # ی
    u'\u06e9' : '', # ۩
    u'\u06ea' : '', # ۪
    u'\u06eb' : '', # ۫
    u'\u06ee' : '', # ۮ
    u'\u06f0' : '', # ۰
    u'\u07fc' : '', # ߼
    u'\u0907' : '', # इ
    u'\u0924' : '', # त
    u'\u0928' : '', # न
    u'\u092f' : '', # य
    u'\u0932' : '', # ल
    u'\u093e' : '', # ा
    u'\u1114' : '', # ᄔ
    u'\u1d25' : '', # ᴥ
    u'\u1d6b' : '', # ᵫ
    u'\u1e25' : '', # ḥ
    u'\u1e35' : '', # ḵ
    u'\u1e6d' : '', # ṭ
    u'\u1e6f' : '', # ṯ
    u'\u1e93' : '', # ẓ
    u'\u1ea1' : '', # ạ
    u'\u1ea3' : '', # ả
    u'\u1ea5' : '', # ấ
    u'\u1eaf' : '', # ắ
    u'\u1eb9' : '', # ẹ
    u'\u1ebd' : '', # ẽ
    u'\u1ebf' : '', # ế
    u'\u1ec1' : '', # ề
    u'\u1ec3' : '', # ể
    u'\u1ec5' : '', # ễ
    u'\u1ec7' : '', # ệ
    u'\u1ecf' : '', # ỏ
    u'\u1ed1' : '', # ố
    u'\u1ed3' : '', # ồ
    u'\u1ed7' : '', # ỗ
    u'\u1ed9' : '', # ộ
    u'\u1edd' : '', # ờ
    u'\u1edf' : '', # ở
    u'\u1ee3' : '', # ợ
    u'\u1eef' : '', # ữ
    u'\u1fd6' : '', # ῖ
    u'\u1fe5' : '', # ῥ
    u'\u2002' : '', #  
    u'\u2006' : '', #  
    u'\u2009' : '', #  
    u'\u200d' : '', # ‍
    u'\u200e' : '', # ‎
    u'\u200f' : '', # ‏
    u'\u2010' : '', # ‐
    u'\u2011' : '', # ‑
    u'\u2012' : '', # ‒
    u'\u2015' : '', # ―
    u'\u2023' : '', # ‣
    u'\u2027' : '', # ‧
    u'\u202a' : '', # ‪
    u'\u202c' : '', # ‬
    u'\u202f' : '', #  
    u'\u2030' : '', # ‰
    u'\u203b' : '', # ※
    u'\u203d' : '?', # ‽
    u'\u203e' : '', # ‾
    u'\u2060' : '', # ⁠
    u'\u2063' : '', # ⁣
    u'\u2066' : '', # ⁦
    u'\u2069' : '', # ⁩
    u'\u2078' : '', # ⁸
    u'\u2103' : '', # ℃
    u'\u2105' : '', # ℅
    u'\u2117' : '', # ℗
    u'\u2120' : '', # ℠
    u'\u2153' : '', # ⅓
    u'\u2190' : '', # ←
    u'\u2248' : '', # ≈
    u'\u2264' : '', # ≤
    u'\u226a' : '', # ≪
    u'\u2501' : '', # ━
    u'\u253b' : '', # ┻
    u'\u2551' : '', # ║
    u'\u256f' : '', # ╯
    u'\u25a1' : '', # □
    u'\u25aa' : '', # ▪
    u'\u25b6' : '', # ▶
    u'\u25c7' : '', # ◇
    u'\u25c9' : '', # ◉
    u'\u25cb' : '', # ○
    u'\u25cf' : '', # ●
    u'\u2600' : '', # ☀
    u'\u2612' : '', # ☒
    u'\u261b' : '', # ☛
    u'\u261d' : '', # ☝
    u'\u261e' : '', # ☞
    u'\u262d' : '', # ☭
    u'\u2640' : '', # ♀
    u'\u2664' : '', # ♤
    u'\u2666' : '', # ♦
    u'\u266a' : '', # ♪
    u'\u266b' : '', # ♫
    u'\u266c' : '', # ♬
    u'\u2686' : '', # ⚆
    u'\u2698' : '', # ⚘
    u'\u26a0' : '', # ⚠
    u'\u26a1' : '', # ⚡
    u'\u26df' : '', # ⛟
    u'\u2705' : '', # ✅
    u'\u270a' : '', # ✊
    u'\u2726' : '', # ✦
    u'\u2728' : '', # ✨
    u'\u273f' : '', # ✿
    u'\u2755' : '', # ❕
    u'\u2764' : '', # ❤
    u'\u279d' : '', # ➝
    u'\u27a1' : '', # ➡
    u'\u2b07' : '', # ⬇
    u'\u2e2e' : '', # ⸮
    u'\u3001' : '', # 、
    u'\u3002' : '', # 。
    u'\u3005' : '', # 々
    u'\u300a' : '', # 《
    u'\u3042' : '', # あ
    u'\u3044' : '', # い
    u'\u3046' : '', # う
    u'\u3048' : '', # え
    u'\u304a' : '', # お
    u'\u304b' : '', # か
    u'\u304c' : '', # が
    u'\u304d' : '', # き
    u'\u304f' : '', # く
    u'\u3050' : '', # ぐ
    u'\u3051' : '', # け
    u'\u3053' : '', # こ
    u'\u3054' : '', # ご
    u'\u3055' : '', # さ
    u'\u3057' : '', # し
    u'\u3058' : '', # じ
    u'\u3059' : '', # す
    u'\u305b' : '', # せ
    u'\u305d' : '', # そ
    u'\u305f' : '', # た
    u'\u3060' : '', # だ
    u'\u3061' : '', # ち
    u'\u3063' : '', # っ
    u'\u3064' : '', # つ
    u'\u3066' : '', # て
    u'\u3067' : '', # で
    u'\u3068' : '', # と
    u'\u3069' : '', # ど
    u'\u306a' : '', # な
    u'\u306b' : '', # に
    u'\u306d' : '', # ね
    u'\u306e' : '', # の
    u'\u306f' : '', # は
    u'\u3070' : '', # ば
    u'\u307e' : '', # ま
    u'\u307f' : '', # み
    u'\u3081' : '', # め
    u'\u3082' : '', # も
    u'\u3083' : '', # ゃ
    u'\u3084' : '', # や
    u'\u3087' : '', # ょ
    u'\u3088' : '', # よ
    u'\u3089' : '', # ら
    u'\u308a' : '', # り
    u'\u308b' : '', # る
    u'\u308c' : '', # れ
    u'\u308d' : '', # ろ
    u'\u308f' : '', # わ
    u'\u3092' : '', # を
    u'\u3093' : '', # ん
    u'\u30a2' : '', # ア
    u'\u30a3' : '', # ィ
    u'\u30a4' : '', # イ
    u'\u30a7' : '', # ェ
    u'\u30a8' : '', # エ
    u'\u30aa' : '', # オ
    u'\u30ab' : '', # カ
    u'\u30ad' : '', # キ
    u'\u30af' : '', # ク
    u'\u30b0' : '', # グ
    u'\u30b1' : '', # ケ
    u'\u30b9' : '', # ス
    u'\u30ba' : '', # ズ
    u'\u30bf' : '', # タ
    u'\u30c0' : '', # ダ
    u'\u30c1' : '', # チ
    u'\u30c3' : '', # ッ
    u'\u30c6' : '', # テ
    u'\u30c9' : '', # ド
    u'\u30ca' : '', # ナ
    u'\u30ce' : '', # ノ
    u'\u30cf' : '', # ハ
    u'\u30d5' : '', # フ
    u'\u30d6' : '', # ブ
    u'\u30d7' : '', # プ
    u'\u30de' : '', # マ
    u'\u30e1' : '', # メ
    u'\u30e2' : '', # モ
    u'\u30e4' : '', # ヤ
    u'\u30e6' : '', # ユ
    u'\u30e9' : '', # ラ
    u'\u30ea' : '', # リ
    u'\u30eb' : '', # ル
    u'\u30ec' : '', # レ
    u'\u30f3' : '', # ン
    u'\u30fb' : '', # ・
    u'\u30fc' : '', # ー
    u'\u3381' : '', # ㎁
    u'\u3383' : '', # ㎃
    u'\u4e00' : '', # 一
    u'\u4e0a' : '', # 上
    u'\u4e0d' : '', # 不
    u'\u4e2d' : '', # 中
    u'\u4e3b' : '', # 主
    u'\u4e3e' : '', # 举
    u'\u4e48' : '', # 么
    u'\u4e8b' : '', # 事
    u'\u4e9a' : '', # 亚
    u'\u4ec0' : '', # 什
    u'\u4efb' : '', # 任
    u'\u4f1a' : '', # 会
    u'\u4f53' : '', # 体
    u'\u4f5c' : '', # 作
    u'\u4ffa' : '', # 俺
    u'\u500b' : '', # 個
    u'\u5074' : '', # 側
    u'\u518d' : '', # 再
    u'\u5197' : '', # 冗
    u'\u51e0' : '', # 几
    u'\u51f6' : '', # 凶
    u'\u51fa' : '', # 出
    u'\u51fb' : '', # 击
    u'\u5206' : '', # 分
    u'\u5207' : '', # 切
    u'\u5224' : '', # 判
    u'\u5225' : '', # 別
    u'\u523a' : '', # 刺
    u'\u529b' : '', # 力
    u'\u529e' : '', # 办
    u'\u52a0' : '', # 加
    u'\u52a9' : '', # 助
    u'\u52d5' : '', # 動
    u'\u52d9' : '', # 務
    u'\u5316' : '', # 化
    u'\u5358' : '', # 単
    u'\u535a' : '', # 博
    u'\u5371' : '', # 危
    u'\u53ad' : '', # 厭
    u'\u53f2' : '', # 史
    u'\u540c' : '', # 同
    u'\u540e' : '', # 后
    u'\u5426' : '', # 否
    u'\u542b' : '', # 含
    u'\u548c' : '', # 和
    u'\u54c8' : '', # 哈
    u'\u554f' : '', # 問
    u'\u55b6' : '', # 営
    u'\u56db' : '', # 四
    u'\u56e3' : '', # 団
    u'\u56fd' : '', # 国
    u'\u5728' : '', # 在
    u'\u5730' : '', # 地
    u'\u5831' : '', # 報
    u'\u5834' : '', # 場
    u'\u5916' : '', # 外
    u'\u5927' : '', # 大
    u'\u5973' : '', # 女
    u'\u5974' : '', # 奴
    u'\u5a4a' : '', # 婊
    u'\u5acc' : '', # 嫌
    u'\u5b50' : '', # 子
    u'\u5b58' : '', # 存
    u'\u5b9a' : '', # 定
    u'\u5b9f' : '', # 実
    u'\u5ba2' : '', # 客
    u'\u5bb3' : '', # 害
    u'\u5bdf' : '', # 察
    u'\u5bfe' : '', # 対
    u'\u5c0f' : '', # 小
    u'\u5c31' : '', # 就
    u'\u5c55' : '', # 展
    u'\u5c71' : '', # 山
    u'\u5d07' : '', # 崇
    u'\u5ddd' : '', # 川
    u'\u5dee' : '', # 差
    u'\u5e33' : '', # 帳
    u'\u5e38' : '', # 常
    u'\u5e74' : '', # 年
    u'\u5f15' : '', # 引
    u'\u5f3e' : '', # 弾
    u'\u5f53' : '', # 当
    u'\u5fa9' : '', # 復
    u'\u5fb7' : '', # 德
    u'\u5fc3' : '', # 心
    u'\u5ff5' : '', # 念
    u'\u6012' : '', # 怒
    u'\u6016' : '', # 怖
    u'\u601d' : '', # 思
    u'\u6027' : '', # 性
    u'\u6050' : '', # 恐
    u'\u60aa' : '', # 悪
    u'\u60c5' : '', # 情
    u'\u6211' : '', # 我
    u'\u6297' : '', # 抗
    u'\u62db' : '', # 招
    u'\u62dd' : '', # 拝
    u'\u6319' : '', # 挙
    u'\u6458' : '', # 摘
    u'\u64ae' : '', # 撮
    u'\u653e' : '', # 放
    u'\u6557' : '', # 敗
    u'\u65ad' : '', # 断
    u'\u65b0' : '', # 新
    u'\u65b9' : '', # 方
    u'\u65e5' : '', # 日
    u'\u65e7' : '', # 旧
    u'\u65e9' : '', # 早
    u'\u660e' : '', # 明
    u'\u662f' : '', # 是
    u'\u666f' : '', # 景
    u'\u66b4' : '', # 暴
    u'\u66f8' : '', # 書
    u'\u6700' : '', # 最
    u'\u6708' : '', # 月
    u'\u672a' : '', # 未
    u'\u672c' : '', # 本
    u'\u6765' : '', # 来
    u'\u68c0' : '', # 检
    u'\u696d' : '', # 業
    u'\u69d8' : '', # 様
    u'\u6a29' : '', # 権
    u'\u6b63' : '', # 正
    u'\u6b74' : '', # 歴
    u'\u6b8b' : '', # 残
    u'\u6bba' : '', # 殺
    u'\u6bce' : '', # 毎
    u'\u6c17' : '', # 気
    u'\u6c37' : '', # 氷
    u'\u6c42' : '', # 求
    u'\u6cb9' : '', # 油
    u'\u6cbb' : '', # 治
    u'\u6cd5' : '', # 法
    u'\u6cdb' : '', # 泛
    u'\u6d0b' : '', # 洋
    u'\u6d77' : '', # 海
    u'\u6e2f' : '', # 港
    u'\u6e80' : '', # 満
    u'\u6f2b' : '', # 漫
    u'\u6fc0' : '', # 激
    u'\u70ba' : '', # 為
    u'\u7269' : '', # 物
    u'\u7279' : '', # 特
    u'\u72ec' : '', # 独
    u'\u7387' : '', # 率
    u'\u751f' : '', # 生
    u'\u753b' : '', # 画
    u'\u767a' : '', # 発
    u'\u76df' : '', # 盟
    u'\u76e3' : '', # 監
    u'\u76ee' : '', # 目
    u'\u76f4' : '', # 直
    u'\u76f8' : '', # 相
    u'\u7701' : '', # 省
    u'\u77e5' : '', # 知
    u'\u78ba' : '', # 確
    u'\u7948' : '', # 祈
    u'\u79f0' : '', # 称
    u'\u7a2e' : '', # 種
    u'\u7a7a' : '', # 空
    u'\u7b11' : '', # 笑
    u'\u7cfe' : '', # 糾
    u'\u7d42' : '', # 終
    u'\u7db2' : '', # 網
    u'\u7e2e' : '', # 縮
    u'\u7f6e' : '', # 置
    u'\u7fa9' : '', # 義
    u'\u8003' : '', # 考
    u'\u8005' : '', # 者
    u'\u805e' : '', # 聞
    u'\u80cc' : '', # 背
    u'\u8150' : '', # 腐
    u'\u81ea' : '', # 自
    u'\u827e' : '', # 艾
    u'\u82e6' : '', # 苦
    u'\u83ab' : '', # 莫
    u'\u843d' : '', # 落
    u'\u8650' : '', # 虐
    u'\u8651' : '', # 虑
    u'\u86ee' : '', # 蛮
    u'\u884c' : '', # 行
    u'\u88ab' : '', # 被
    u'\u88ad' : '', # 袭
    u'\u88c1' : '', # 裁
    u'\u88dc' : '', # 補
    u'\u897f' : '', # 西
    u'\u898b' : '', # 見
    u'\u8996' : '', # 視
    u'\u89d2' : '', # 角
    u'\u89e3' : '', # 解
    u'\u8a00' : '', # 言
    u'\u8a0e' : '', # 討
    u'\u8a55' : '', # 評
    u'\u8a8d' : '', # 認
    u'\u8a9e' : '', # 語
    u'\u8ac7' : '', # 談
    u'\u8b70' : '', # 議
    u'\u8ba4' : '', # 认
    u'\u8bb2' : '', # 讲
    u'\u8bbd' : '', # 讽
    u'\u8bc9' : '', # 诉
    u'\u8be5' : '', # 该
    u'\u8c03' : '', # 调
    u'\u8db3' : '', # 足
    u'\u8f9e' : '', # 辞
    u'\u8fd1' : '', # 近
    u'\u8fd4' : '', # 返
    u'\u9012' : '', # 递
    u'\u9019' : '', # 這
    u'\u901a' : '', # 通
    u'\u9023' : '', # 連
    u'\u904e' : '', # 過
    u'\u9053' : '', # 道
    u'\u9054' : '', # 達
    u'\u9078' : '', # 選
    u'\u90e8' : '', # 部
    u'\u90fd' : '', # 都
    u'\u91ce' : '', # 野
    u'\u91d1' : '', # 金
    u'\u93e1' : '', # 鏡
    u'\u955c' : '', # 镜
    u'\u9577' : '', # 長
    u'\u958b' : '', # 開
    u'\u9662' : '', # 院
    u'\u967a' : '', # 険
    u'\u969b' : '', # 際
    u'\u969c' : '', # 障
    u'\u96c6' : '', # 集
    u'\u9707' : '', # 震
    u'\u9752' : '', # 青
    u'\u9762' : '', # 面
    u'\u982d' : '', # 頭
    u'\u984c' : '', # 題
    u'\u9986' : '', # 馆
    u'\u9996' : '', # 首
    u'\u9a13' : '', # 験
    u'\u9ad8' : '', # 高
    u'\u9ed2' : '', # 黒
    u'\u9ed8' : '', # 默
    u'\u9ede' : '', # 點
    u'\ue025' : '', # 
    u'\ue901' : '', # 
    u'\uf8ff' : '', # 
    u'\ufb06' : '', # ﬆ
    u'\ufe0e' : '', # ︎
    u'\ufe0f' : '', # ️
    u'\ufe35' : '', # ︵
    u'\uff01' : '', # ！
    u'\uff08' : '', # （
    u'\uff09' : '', # ）
    u'\uff11' : '', # １
    u'\uff1a' : '', # ：
    u'\uff1b' : '', # ；
    u'\uff1d' : '', # ＝
    u'\uff