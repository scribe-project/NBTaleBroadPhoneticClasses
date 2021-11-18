sampa2htk = {
    # HTK safe symbols
    '{': 'ae',
    '{:': 'ae:',
    '2': 'oe',
    '2:': 'oe:',
    '}': 'ou',
    '}:': 'ou:',
    '{i': 'ei',
    'A}': 'oev',
    '2y': 'oei',
    't`': 'rt',
    'd`': 'rd',
    'n`': 'rn',
    'l`': 'rl',
    's`': 'rs',
    '@': 'eh',
}

broadClasses =  {
    # Vowels
    'U': '}',
    '3:': '2:',
    'V': '2:',
    'I': 'i',
    # Diphtongs
    'aU': 'A}',
    '@U': 'A}',
    '2}': 'A}',
    'eI': '{i',
    '}i': 'Oy',
    'ui': 'Oy',
    # Plosives
    'c': 'C',
    'J\\': 'd',
    # glottal stop
    '?': '',
    # fricatives and approximants
    'w': 'O',
    'z': 's',
    'Z': 'S',
    'c__C': 'C',
    't__S': 'tS',
    'd__Z': 'C',
    'T': 'f',
    'D': 'd',
    'x': 'h',
    # Nasals, laterals and trills
    '4': 'r',
    'R': 'r',
    'r\\': 'r',
    'J': 'n',
    'L': 'l',
    # retroflex
    'r`': 'l',
    # syllabic consonants
    'l_=': 'l',
    'l`_=': 'l`',
    'm_=': 'm',
    'n_=': 'n',
    'n`_=': 'n`',
    '4_=': 'r',
    'J_=': 'n',
    'L_=': 'l',
    'R_=': 'r',
    'N_=': 'N',
    'r\\_=': 'r',
    's_=': 's',
    't`_=': 't`',
    'v_=': 'v',
    # non verbal
    '<start>': 'sil',
    '<end>': 'sil',
    '<sil>': 'sil',
    '<exhale>': 'h',
    '<inhale>': 'h',
    '<nasal>': 'm',
    '<vowel>': 'eh',
    '<fp>': 'spk'
    }

def broadClass(phone, removeStress=True, htkSafe=False):
    """
    broadClass: converts the phonetic inventory used in NB Tale to broader phonetic classes

    phone: input phonetic symbol including stress markers
    removeStress: if True, the output symbol will not include stress markers
    HTKsafe: if True, return symbols that are compatible with HTK
    """
    # remove and set aside stress information
    if phone[:2] == '""':
        stress = '""'
        phone = phone[2:]
    if phone[:1] == '"':
        stress = '"'
        phone = phone[1:]
    if phone[:1] == '%':
        stress = '%'
        phone = phone[1:]
    if phone in broadClasses.keys():
        phone = broadClasses[phone]
    if htkSafe and phone in sampa2htk.keys():
        phone = sampa2htk[phone]
    if removeStress:
        return phone
    return stress+phone
        
NBTaleSymbols = [
    '""2',
    '""2:',
    '""2y',
    '""2}',
    '""A',
    '""A:',
    '""Ai',
    '""A}',
    '""O',
    '""O:',
    '""Oy',
    '""aU',
    '""e',
    '""e:',
    '""eI',
    '""i',
    '""i:',
    '""n`_=',
    '""u',
    '""u:',
    '""y',
    '""y:',
    '""{',
    '""{:',
    '""{i',
    '""}',
    '""}:',
    '""}i',
    '"2',
    '"2:',
    '"2y',
    '"2}',
    '"3:',
    '"@U',
    '"A',
    '"A:',
    '"Ai',
    '"A}',
    '"O',
    '"O:',
    '"Oy',
    '"U',
    '"U:',
    '"V',
    '"aU',
    '"e',
    '"e:',
    '"eI',
    '"i',
    '"i:',
    '"l_=',
    '"m_=',
    '"n_=',
    '"u',
    '"u:',
    '"y',
    '"y:',
    '"{',
    '"{:',
    '"{i',
    '"}',
    '"}:',
    '"}i',
    '%2',
    '%2:',
    '%2y',
    '%2}',
    '%3:',
    '%@U',
    '%A',
    '%A:',
    '%Ai',
    '%A}',
    '%O',
    '%O:',
    '%Oy',
    '%U:',
    '%V',
    '%aU',
    '%e',
    '%e:',
    '%eI',
    '%i',
    '%i:',
    '%n',
    '%u',
    '%u:',
    '%y',
    '%y:',
    '%{',
    '%{:',
    '%{i',
    '%}',
    '%}:',
    '%}i',
    '2',
    '2:',
    '2y',
    '2}',
    '4',
    '4_=',
    '<end>',
    '<exhale>',
    '<fp>',
    '<inhale>',
    '<nasal>',
    '<sil>',
    '<start>',
    '<vowel>',
    '?',
    '@',
    '@U',
    'A',
    'A:',
    'Ai',
    'A}',
    'C',
    'D',
    'J',
    'J\\',
    'J_=',
    'L',
    'L_=',
    'N',
    'N_=',
    'O',
    'O:',
    'Oy',
    'R',
    'R_=',
    'S',
    'T',
    'U',
    'U:',
    'V',
    'Z',
    'aU',
    'b',
    'c',
    'c__C',
    'd',
    'd__Z',
    'd`',
    'e',
    'e:',
    'eI',
    'f',
    'g',
    'h',
    'i',
    'i:',
    'j',
    'k',
    'l',
    'l_=',
    'l`',
    'l`_=',
    'm',
    'm_=',
    'n',
    'n_=',
    'n`',
    'n`_=',
    'p',
    'r\\',
    'r\\_=',
    'r`',
    's',
    's_=',
    't',
    't__S',
    't`',
    'u',
    'u:',
    'v',
    'v_=',
    'w',
    'x',
    'y',
    'y:',
    'z',
    '{',
    '{:',
    '{i',
    '}',
    '}:',
    '}i'
]
