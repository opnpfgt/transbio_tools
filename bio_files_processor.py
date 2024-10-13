import os


def convert_multiline_fasta_to_oneline(input_fasta, output_fasta="output_short"):
    if os.path.exists(output_fasta):
        raise FileExistsError(
            f"File {output_fasta} already exists.\
 Please choose another name."
        )
    with open(os.path.join(input_fasta), "r") as infile, open(
        os.path.join(output_fasta), "w"
    ) as outfile:
        current_header = None
        current_sequence = []
        for line in infile:
            line = line.strip()
            if line.startswith(">"):  # Header line
                if current_header:
                    # If there is a previous sequence, write it to the output
                    outfile.write(f"{current_header}\n{''.join(current_sequence)}\n")
                current_header = line  # Update the current header
                current_sequence = []  # Reset the sequence list
            else:
                current_sequence.append(line)
