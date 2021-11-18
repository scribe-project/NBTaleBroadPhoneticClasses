# broadClasses converts the original phonetic inventory used in NB Tale transcription to a set of broader phonetic classes that can be used for phonetic classification

broadClasses =  {
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
    # reductions (Vowels)
    'U': 'ou',
    '3:': 'oe:',
    'V': 'oe:',
    'I': 'i',
    '@': 'eh',
    # reductions (Diphtongs)
    'aU': 'oev',
    '@U': 'oev',
    '2}': 'oev',
    'eI': 'ei',
    '}i': 'Oy',
    'ui': 'Oy',
    # reductions (Plosives)
    'c': 'C',
    'J\\': 'd',
    # reductions (glottal stop)
    '?': '',
    # reductions (fricatives and approximants)
    'w': 'O',
    'z': 's',
    'Z': 'S',
    'c__C': 'C',
    't__S': 'tS',
    'd__Z': 'C',
    'T': 'f',
    'D': 'd',
    'x': 'h',
    # reductions (Nasals, laterals and trills)
    '4': 'r',
    'R': 'r',
    'r\\': 'r',
    'J': 'n',
    'L': 'l',
    # reductions (retroflex)
    'r`': 'l',
    # reductions (syllabic consonants)
    'l_=': 'l',
    'l`_=': 'rl',
    'm_=': 'm',
    'n_=': 'n',
    'n`_=': 'rn',
    '4_=': 'r',
    'J_=': 'n',
    'L_=': 'l',
    'R_=': 'r',
    'N_=': 'N',
    'r\\_=': 'r',
    's_=': 's',
    't`_=': 'rt',
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

def broadClass(phone, removeStress=True):
    """
    broadClass: converts the phonetic inventory used in NB Tale to broader phonetic classes

    phone: input phonetic symbol including stress markers
    removeStress: if True, the output symbol will not include stress markers
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
