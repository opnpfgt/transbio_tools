from typing import Dict, Tuple, Union
from modules.module_for_dna_rna_tools import get_na_type, complement
from modules.module_for_dna_rna_tools import reverse, reverse_complement
from modules.module_for_dna_rna_tools import reverse_transcribe, transcribe
from modules.module_for_filter_fastq import avg_quality, gc_bound


def run_dna_rna_tools(*args: Union[Union[list, str], str]) -> Union[list, str]:
    '''Запускает указанные процедуры (транскрипция, комплементация и т.д.)\
для переданных последовательностей'''
    # Проверяем, что последним аргументом является имя процедуры
    if not args:
        raise ValueError("You forgot to add func or seq")

    procedure = args[-1]
    sequences = args[:-1]

    # Проверяем, что все последовательности являются корректными
    for seq in sequences:
        if get_na_type(seq) != 'dna' and get_na_type(seq) != 'rna':
            raise ValueError(f'''Проблемы \
                            c последовательностью: {get_na_type(seq)}''')

    # Выполняем нужную процедуру
    if procedure == 'transcribe':
        results = [transcribe(seq) for seq in sequences]
    elif procedure == 'reverse':
        results = [reverse(seq) for seq in sequences]
    elif procedure == 'complement':
        results = [complement(seq) for seq in sequences]
    elif procedure == 'reverse_complement':
        results = [reverse_complement(seq) for seq in sequences]
    elif procedure == 'reverse_transcribe':
        results = [reverse_transcribe(seq) for seq in sequences]
    else:
        raise ValueError(f"Can\'t perform: {procedure}")

    # Возвращаем результат в зависимости от количества последовательностей
    return results[0] if len(results) == 1 else results


# def check_type(gc_bounds, length_bounds):
#     if isinstance(gc_bounds, (int, float)):
#         gc_bounds = (0, gc_bounds)
#     if not isinstance(length_bounds, tuple):
#         length_bounds = (0, length_bounds)
#     return gc_bounds, length_bounds


def filter_fastq(seqs: Dict[str, Tuple[str, str]],
                 gc_bounds: Union[int, float, tuple] = (0, 100),
                 length_bounds: Union[int, float, tuple] = (0, 2**32),
                 quality_threshold:
                     Union[int, float] = 0) -> Dict[str, Tuple[str, str]]:

    if isinstance(gc_bounds, (int, float)):
        gc_bounds = (0, gc_bounds)
    if not isinstance(length_bounds, tuple):
        length_bounds = (0, length_bounds)
    if not seqs:
        raise ValueError('Ooops, you forgot to feed meeee')

    # check = check_type(gc_bounds, length_bounds)

    filtered_seqs = {}

    for name, (seq, quality) in seqs.items():
        gc = gc_bound(seq)
        length = len(seq)
        ave_q = avg_quality(quality)
        if ((gc_bounds[0] <= gc <= gc_bounds[1]) and
           (length_bounds[0] <= length <= length_bounds[1]) and
           (ave_q >= quality_threshold)):
            filtered_seqs[name] = (seq, quality)

    return filtered_seqs
