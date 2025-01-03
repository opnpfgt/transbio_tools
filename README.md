# Transbio Tools

# Transbio Tools

**Transbio Tools** is a set of modules for working with biological DNA and RNA sequences and implementing processes of the central dogma of molecular biology. It supports handling the long_fasta format, processing BLAST results, and filtering data in FASTQ format.

## Project Structure

transbio_tools/

module_for_filter_fastq.py  # Module for filtering FASTQ data
module_for_dna_rna_tools.py # Module for working with DNA and RNA
fastq_filtrator.py  # Main module for running DNA and RNA processing tools


python

## Modules

### 1. `module_for_filter_fastq.py`

This module contains functions for calculating GC content and average quality of sequences.

- **Functions:**
  - `gc_bound(seq: str) -> float`: Calculates the percentage of G and C in a sequence.
  - `avg_quality(quality: str) -> float`: Calculates the average quality of a sequence.

### 2. `module_for_dna_rna_tools.py`

This module provides functions for working with DNA and RNA, including obtaining complementary sequences, transcription, and reverse transcription.

- **Functions:**
  - `get_na_type(seq: str) -> str`: Determines the type of nucleic acid (DNA or RNA) or reports an error.
  - `complement(seq: str) -> str`: Returns the complementary sequence.
  - `transcribe(dna_seq: str) -> str`: Transcribes DNA into RNA.
  - `reverse_transcribe(rna_seq: str) -> str`: Reverse transcribes RNA into DNA.
  - `reverse(seq: str) -> str`: Returns the reverse sequence.
  - `reverse_complement(seq: str) -> str`: Returns the reverse complementary sequence.

### 3. `transbio_tool.py`

This module combines functions from the previous modules and provides an interface for processing DNA and RNA sequences.

- **Functions:**
  - `run_dna_rna_tools(*args)`: Runs specified procedures (transcription, complementation, etc.) for the provided sequences.
  - `filter_fastq(input_fastq: str, output_fastq: str, gc_bounds: Union[int, float, tuple], length_bounds: Union[int, float, tuple], quality_threshold: Union[int, float]) -> str`: Filters FASTQ data based on specified criteria (GC content, length, quality) and writes the resulting data to the output FASTQ file.

## Installation

To use the modules, simply copy the `transbio_tools` folder into your project. Make sure all dependencies are installed (if any).

## Examples of Usage

### Filtering FASTQ

```python
from transbio_tools.fastq_filtrator import filter_fastq

seqs = {
    '@SRX079801': (
        'ACAGCAACATAAACATGATGGGATGGCGTAAGCCCCCGAGATATCAGTTTACCCAGGATAAGAGATTAAATTATGAGCAACATTATTAA',
        'FGGGFGGGFGGGFGDFGCEBB@CCDFDDFFFFBFFGFGEFDFFFF;D@DD>C@DDGGGDFGDGG?GFGFEGFGGEF@FDGGGFGFBGGD'
    )
}

filtered_sequences = filter_fastq(seqs, gc_bounds=(30, 60), length_bounds=(0, 100), quality_threshold=20)
print(filtered_sequences)'''

Working with DNA and RNA

'''python

from transbio_tools.modules.module_for_dna_rna_tools import transcribe, complement

dna_seq = "ATGC"
rna_seq = transcribe(dna_seq)
complement_seq = complement(dna_seq)

print(f"Transcribed sequence: {rna_seq}")
print(f"Complementary sequence: {complement_seq}")'''


# bio_files_processor

This package provides essential utilities for bioinformatics data processing, including converting multi-line FASTA files to single-line format and parsing BLAST output files to extract protein names. 

## Features

- **Convert Multi-line FASTA to Single Line**: Easily convert FASTA files formatted with multiple lines into a more compact single-line format.
- **Parse BLAST Output**: Extract the best matching protein names from BLAST results and save them to a text file.

## Requirements

- Python 3.x

## Functions

### `convert_multiline_fasta_to_oneline(input_fasta: str, output_fasta: str = "output_short")`

Converts a multi-line FASTA file to a single-line FASTA file.

#### Parameters:

- `input_fasta` (str): The path to the input multi-line FASTA file.
- `output_fasta` (str, optional): The path to the output single-line FASTA file. Default is `"output_short"`.

#### Example Usage:

'''python
convert_multiline_fasta_to_oneline('input.fasta', 'output.fasta')'''


#### Note:

If the output file already exists, the function raises a FileExistsError.


parse_blast_output(input_file: str, output_file: str)

Extracts the first protein name from the Description column in a BLAST results file and saves them to a new file.


Parameters:


input_file (str): The path to the input BLAST results file in TXT format.

output_file (str): The path to the output file where the protein names will be saved.


Example Usage:

'''python

parse_blast_output('example_blast_results.txt', 'best_matches.txt')
'''

License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgements


Any libraries or resources that were helpful.


Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.


Contact

For questions or feedback, please contact OSA.
