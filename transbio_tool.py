from typing import Union
from modules.module_for_dna_rna_tools import get_na_type, complement
from modules.module_for_dna_rna_tools import reverse, reverse_complement
from modules.module_for_dna_rna_tools import reverse_transcribe, transcribe
from modules.module_for_filter_fastq import avg_quality, gc_bound
import os

# path_to_file = os.path
# path_file = os.path.join()

# with open() as file:
#     input_fastq = file.read()
# output_fastq =


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


# def get_line(file):
#     header = file.readline().strip()
#     if header.startswith('@S'):
#         seq = file.readline().strip()
#         file.readline()  # Skip the string with "+"
#         quality = file.readline().strip()
#         return header, seq, quality

# def write_fastq(header: str, seq: str, quality: str, output_fastq: str):
#     with open(os.path.join(output_fastq), 'a') as file:
#         file.write((f'{header}\n{seq}\n+\n{quality}\n'))


def filter_fastq(input_fastq: str, output_fastq: str,
                 gc_bounds: Union[int, float, tuple] = (0, 100),
                 length_bounds: Union[int, float, tuple] = (0, 2**32),
                 quality_threshold: Union[int, float] = 0):
    '''
    Filters sequences from a FASTQ file based on GC content,
    sequence length, and average quality score.
    '''

    filtered_dir = 'filtered'
    if not os.path.exists(filtered_dir):
        os.makedirs(filtered_dir)

    output_path = os.path.join(filtered_dir, output_fastq)

    if os.path.exists(output_path):
        raise FileExistsError(f"File {output_fastq} already exists.\
 Please choose another name.")
    elif os.path.exists(output_fastq):
        raise FileExistsError(f"File {output_fastq} already exists.\
 Please choose another name.")

    # Construct the full output file path
    output_path = os.path.join(filtered_dir, output_fastq)
    with open(input_fastq, 'r') as infile, open(output_path, 'a') as outfile:
        for header in infile:  # Iterate over lines in the input file
            header = header.strip()
            if not header:
                break  # End of file reached
            seq = infile.readline().strip()
            infile.readline()  # Skip the line with "+"
            quality = infile.readline().strip()

            # Calculate values
            gc = gc_bound(seq)
            length = len(seq)
            ave_q = avg_quality(quality)

            # Filtering and writing results
            if ((gc_bounds[0] <= gc <= gc_bounds[1]) and
               (length_bounds[0] <= length <= length_bounds[1]) and
               (ave_q >= quality_threshold)):
                outfile.write(f"{header}\n{seq}\n+\n{quality}\n")

    return f"Processing completed. Filtered data saved to {output_path}"
