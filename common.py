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
    u'\u04