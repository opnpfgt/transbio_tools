from typing import Dict, Tuple, Union
from modules.module_for_dna_rna_tools import get_na_type, complement
from modules.module_for_dna_rna_tools import reverse, reverse_complement
from modules.module_for_dna_rna_tools import reverse_transcribe, transcribe
from modules.module_for_filter_fastq import avg_quality, gc_bound


def run_dna_rna_tools(*args: Union[Union[list, str], str]) -> Union[list, str]:
    '''Run listed procedures (trnscribe, complement, etc.)\
for given sequences'''
    # Check for presence of all args
    if not args:
        raise ValueError("You forgot to add func or seq")

    procedure = args[-1]
    sequences = args[:-1]
    procedures = {'transcribe': transcribe,
                  'reverse': reverse,
                  'complement': complement,
                  'reverse_complement': reverse_complement,
                  'reverse_transcribe': reverse_transcribe}
    # Check our sequences
    for seq in sequences:
        if get_na_type(seq) != 'dna' and get_na_type(seq) != 'rna':
            raise ValueError(f'''Problems \
                            with your sequence: {get_na_type(seq)}''')

    # Perform the procedure
    if procedure in procedures:
        results = [procedures[procedure](seq) for seq in sequences]
    else:
        raise ValueError(f"Can\'t perform: {procedure}")

    # Return result depending on the number of sequences
    return results[0] if len(results) == 1 else results


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
