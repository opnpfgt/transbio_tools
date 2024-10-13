import os

def convert_multiline_fasta_to_oneline(input_fasta, output_fasta='output_short'):
    if os.path.exists(output_fasta):
        raise FileExistsError(f"File {output_fasta} already exists.\
 Please choose another name.")
    with open(os.path.join(input_fasta), 'r') as infile, open(os.path.join(output_fasta), 'a') as outfile:
        for lines in infile:
            header = infile.readline.strip()
            seq = []
            while not lines.readline().startswith('>').strip():
                seq.append(lines)
            seq = ",".join(seq)
            outfile.write(f"{header}\n{seq}\n")
