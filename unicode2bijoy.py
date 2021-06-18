"""
A python script that takes a Unicode string and converts it into Bijoy

To use:
>>> from unicode2bijoy import to_bijoy
>>> to_bijoy("একা বসে তুমি")
GKv e‡m Zywg
>>> to_bijoy(\"\"\"একা বসে তুমি,
... দেখছো কি একই আকাশ?
... দিন শেষে তার তারাগুলো দিবে দেখা।\"\"\")
GKv e‡m Zywg,
‡`L‡Qv wK GKB AvKvk?
w`b ‡k‡l Zvi Zviv¸‡jv w`‡e ‡`Lv|
"""

def __is_bangla_pre_kar(ch_unicode: str) -> bool:
    return ch_unicode in ['ি', 'ৈ', 'ে']


def __is_bangla_banjonborno(ch_unicode: str) -> bool:
    return ch_unicode in ['ক', 'খ', 'গ', 'ঘ', 'ঙ', 'চ', 'ছ', 'জ', 'ঝ', 'ঞ', 'ট', 'ঠ', 'ড', 'ঢ', 'ণ', 'ত', 'থ', 'দ', 'ধ', 'ন', 'প', 'ফ', 'ব', 'ভ', 'ম', 'শ', 'ষ', 'স', 'হ', 'য', 'র', 'ল', 'য়', 'ং', 'ঃ', 'ঁ', 'ৎ']


def __is_bangla_halant(ch_unicode: str) -> bool:
    return ch_unicode == '্'


__uni2bijoy_string_conversion_map = {
    "।": "|",
    "‘": "Ô",
    "’": "Õ",
    "“": "Ò",
    "”": "Ó",
    "্র্য": "ª¨",
    "র‌্য": "i¨",
    "ক্ক": "°",
    "ক্ট": "±",
    "ক্ত": "³",
    "ক্ব": "K¡",
    "স্ক্র": "¯Œ",
    "ক্র": "µ",
    "ক্ল": "K¬",
    "ক্ষ": "¶",
    "ক্স": "·",
    "গু": "¸",
    "গ্ধ": "»",
    "গ্ন": "Mœ",
    "গ্ম": "M¥",
    "গ্ল": "M­",
    "গ্রু": "Mªy",
    "ঙ্ক": "¼",
    "ঙ্ক্ষ": "•¶",
    "ঙ্খ": "•L",
    "ঙ্গ": "½",
    "ঙ্ঘ": "•N",
    "চ্চ": "”P",
    "চ্ছ": "”Q",
    "চ্ছ্ব": "”Q¡",
    "চ্ঞ": "”T",
    "জ্জ্ব": "¾¡",
    "জ্জ": "¾",
    "জ্ঝ": "À",
    "জ্ঞ": "Á",
    "জ্ব": "R¡",
    "ঞ্চ": "Â",
    "ঞ্ছ": "Ã",
    "ঞ্জ": "Ä",
    "ঞ্ঝ": "Å",
    "ট্ট": "Æ",
    "ট্ব": "U¡",
    "ট্ম": "U¥",
    "ড্ড": "Ç",
    "ণ্ট": "È",
    "ণ্ঠ": "É",
    "ন্স": "Ý",
    "ণ্ড": "Ð",
    "ন্তু": "š‘",
    "ণ্ব": "Y^",
    "ত্ত": "Ë",
    "ত্ত্ব": "Ë¡",
    "ত্থ": "Ì",
    "ত্ন": "Zœ",
    "ত্ম": "Z¥",
    "ন্ত্ব": "š—¡",
    "ত্ব": "Z¡",
    "থ্ব": "_¡",
    "দ্গ": "˜M",
    "দ্ঘ": "˜N",
    "দ্দ": "Ï",
    "দ্ধ": "×",
    "দ্ব": "˜¡",
    "দ্ব": "Ø",
    "দ্ভ": "™¢",
    "দ্ম": "Ù",
    "দ্রু": "`ªæ",
    "ধ্ব": "aŸ",
    "ধ্ম": "a¥",
    "ন্ট": "›U",
    "ন্ঠ": "Ú",
    "ন্ড": "Û",
    "ন্ত্র": "š¿",
    "ন্ত": "šÍ",
    "স্ত্র": "¯¿",
    "ত্র": "Î",
    "ন্থ": "š’",
    "ন্দ": "›`",
    "ন্দ্ব": "›Ø",
    "ন্ধ": "Ü",
    "ন্ন": "bœ",
    "ন্ব": "š^",
    "ন্ম": "b¥",
    "প্ট": "Þ",
    "প্ত": "ß",
    "প্ন": "cœ",
    "প্প": "à",
    "প্ল": "cø",
    "প্স": "á",
    "ফ্ল": "d¬",
    "ব্জ": "â",
    "ব্দ": "ã",
    "ব্ধ": "ä",
    "ব্ব": "eŸ",
    "ব্ল": "eø",
    "ভ্র": "å",
    "ম্ন": "gœ",
    "ম্প": "¤ú",
    "ম্ফ": "ç",
    "ম্ব": "¤^",
    "ম্ভ": "¤¢",
    "ম্ভ্র": "¤£",
    "ম্ম": "¤§",
    "ম্ল": "¤­",
    "রু": "iæ",
    "রূ": "iƒ",
    "ল্ক": "é",
    "ল্গ": "ê",
    "ল্প": "í",
    "ল্ট": "ë",
    "ল্ড": "ì",
    "ল্ফ": "î",
    "ল্ব": "j¦",
    "ল্ম": "j¥",
    "ল্ল": "jø",
    "শু": "ï",
    "শ্চ": "ð",
    "শ্ন": "kœ",
    "শ্ব": "k¦",
    "শ্ম": "k¥",
    "শ্ল": "kø",
    "ষ্ক": "®‹",
    "ষ্ক্র": "®Œ",
    "ষ্ট": "ó",
    "ষ্ঠ": "ô",
    "ষ্ণ": "ò",
    "ষ্প": "®ú",
    "ষ্ফ": "õ",
    "ষ্ম": "®§",
    "স্ক": "¯‹",
    "স্ট": "÷",
    "স্খ": "ö",
    "স্ত": "¯Í",
    "স্তু": "¯‘",
    "স্থ": "¯’",
    "স্ন": "mœ",
    "স্প": "¯ú",
    "স্ফ": "ù",
    "স্ব": "¯^",
    "স্ম": "¯§",
    "স্ল": "¯­",
    "হু": "û",
    "হ্ণ": "nè",
    "হ্ন": "ý",
    "হ্ম": "þ",
    "হ্ল": "n¬",
    "হৃ": "ü",
    "র্": "©",
    "্র": "ª",
    "্য": "¨",
    "্": "&",
    "আ": "Av",
    "অ": "A",
    "ই": "B",
    "ঈ": "C",
    "উ": "D",
    "ঊ": "E",
    "ঋ": "F",
    "এ": "G",
    "ঐ": "H",
    "ও": "I",
    "ঔ": "J",
    "ক": "K",
    "খ": "L",
    "গ": "M",
    "ঘ": "N",
    "ঙ": "O",
    "চ": "P",
    "ছ": "Q",
    "জ": "R",
    "ঝ": "S",
    "ঞ": "T",
    "ট": "U",
    "ঠ": "V",
    "ড": "W",
    "ঢ": "X",
    "ণ": "Y",
    "ত": "Z",
    "থ": "_",
    "দ": "`",
    "ধ": "a",
    "ন": "b",
    "প": "c",
    "ফ": "d",
    "ব": "e",
    "ভ": "f",
    "ম": "g",
    "য": "h",
    "র": "i",
    "ল": "j",
    "শ": "k",
    "ষ": "l",
    "স": "m",
    "হ": "n",
    "ড়": "o",
    "ঢ়": "p",
    "য়": "q",
    "ৎ": "r",
    "০": "0",
    "১": "1",
    "২": "2",
    "৩": "3",
    "৪": "4",
    "৫": "5",
    "৬": "6",
    "৭": "7",
    "৮": "8",
    "৯": "9",
    "া": "v",
    "ি": "w",
    "ী": "x",
    "ু": "y",
    "ূ": "~",
    "ৃ": "…",
    "ে": "‡",
    "ৈ": "‰",
    "ৗ": "Š",
    "ং": "s",
    "ঃ": "t",
    "ঁ": "u",
}


def __rearrange_unicode_str(text: str) -> str:
    barrier = 0
    i = 0
    while (i < len(text)):
        if i < len(text) and __is_bangla_pre_kar(text[i]):
            j = 1
            while (__is_bangla_banjonborno(text[i - j])):
                if (i - j < 0):
                    break
                if (i - j <= barrier):
                    break
                if (__is_bangla_halant(text[i - j - 1])):
                    j += 2
                else:
                    break
            temp = text[0: i - j]
            temp += text[i]
            temp += text[i - j: i]
            temp += text[i + 1: len(text)]
            text = temp
            barrier = i + 1
        if (
            i < (len(text) - 1) and
            __is_bangla_halant(text[i]) and
            text[i - 1] == 'র' and
            not __is_bangla_halant(text[i - 2])
        ):
            j = 1
            found_pre_kar = 0
            while True:
                if __is_bangla_banjonborno(text[i + j]) and __is_bangla_halant(text[i + j + 1]):
                    j += 2
                elif __is_bangla_banjonborno(text[i + j]) and __is_bangla_pre_kar(text[i + j + 1]):
                    found_pre_kar = 1
                    break
                else:
                    break
            temp = text[0: i - 1]
            temp += text[i + j + 1: i + j + found_pre_kar + 1]
            temp += text[i + 1: i + j + 1]
            temp += text[i - 1]
            temp += text[i]
            temp += text[i + j + found_pre_kar + 1: len(text)]
            text = temp
            i += j + found_pre_kar
            barrier = i + 1
        i+=1
    return text


def __to_bijoy_inner(line):
    conversion_map = __uni2bijoy_string_conversion_map
    line = line.replace("ো", "ো")
    line = line.replace("ৌ", "ৌ")
    line = __rearrange_unicode_str(line)
    for unic in conversion_map:
        line = line.replace(unic, conversion_map[unic])
    return line


def to_bijoy(unicode_str: str):
    """
    Args:
        unicode_str: a string in unicode

    Returns:
        A python script that takes Unicode string converts it into Bijoy

    To use:
    >>> to_bijoy("একা বসে তুমি")
    GKv e‡m Zywg
    >>> to_bijoy(\"\"\"একা বসে তুমি,
    ... দেখছো কি একই আকাশ?
    ... দিন শেষে তার তারাগুলো দিবে দেখা।\"\"\")
    GKv e‡m Zywg,
    ‡`L‡Qv wK GKB AvKvk?
    w`b ‡k‡l Zvi Zviv¸‡jv w`‡e ‡`Lv|
    """
    unicode_str = unicode_str.replace("য়", "য়").replace("\u200d", "\u200c")
    unicode_str_list = unicode_str.split('\n')
    result = ""
    for s in unicode_str_list:
        result += __to_bijoy_inner(s) + '\n'
    result = ''.join(char for char in result.strip() if ord(char) != 8204)
    return result
