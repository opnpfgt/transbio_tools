def get_na_type(seq: str) -> str:
    dna_set = {'A', 'T', 'G', 'C', 'a', 't', 'g', 'c'}
    rna_set = {'A', 'U', 'G', 'C', 'a', 'u', 'g', 'c'}
    if 'U' in seq and 'T' in seq:
        return 'У вас таки примесь РНК в ДНК'
    # Содержит и U, и T, что недопустимо
    elif set(seq) <= dna_set:
        c = 'dna'
    elif set(seq) <= rna_set:
        c = 'rna'
    else:
        c = 'Sequence is wrong'
    return c


def complement(seq: str) -> str:
    """Return comlement sequence"""
    if get_na_type(seq) == 'dna':
        complement_str = str.maketrans('ATGCatgc', 'TACGtacg')
    elif get_na_type(seq) == 'rna':
        complement_str = str.maketrans('AUGCaugc', 'UACGuacg')
    return seq.translate(complement_str)


def transcribe(dna_seq: str) -> str:
    if get_na_type(dna_seq) == 'dna':
        transcribed = dna_seq.replace('U', 'T').replace('u', 't')
    else:
        raise ValueError('Can\'t transcribe this sequence')
    """Transcribe DNA to RNA"""
    return transcribed


def reverse_transcribe(rna_seq: str) -> str:
    if get_na_type(rna_seq) == 'rna':
        rev_transcribed = rna_seq.replace('U', 'T').replace('u', 't')
    else:
        raise ValueError('Can\'t rev transcribe this sequence')
    """Transcribe RNA to DNA"""
    return rev_transcribed


def reverse(seq: str) -> str:
    """Return reverse sequence"""
    return seq[::-1]


def reverse_complement(seq: str) -> str:
    """Return reversed complement sequence"""
    return complement(reverse(seq))
