import os


def convert_multiline_fasta_to_oneline(
    input_fasta: str, output_fasta: str = "output_short"
):
    """
    Converts a multiline FASTA file to a single-line FASTA file.
    """
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
                    outfile.write(
                        f"{current_header}\
                        \n{''.join(current_sequence)}\n"
                    )
                current_header = line  # Update the current header
                current_sequence = []  # Reset the sequence list
            else:
                current_sequence.append(line)


def parse_blast_output(input_file: str, output_file: str):
    """
    Extracts the first protein name from the Description
    column in a BLAST results file
    and saves them to a new file.

    Parameters:
    ----------
    input_file
        The path to the input BLAST results file in TXT format.

    output_file
        The path to the output file where the protein names will be saved.
    """
    best_matches = set()  # Use a set to avoid duplicates

    with open(input_file, "r") as infile:
        for line in infile:
            line = line.strip()

            # Check for the start of a new query
            if line.startswith("Query="):
                continue

            # Look for the start of significant alignments section
            if "Sequences producing significant alignments:" in line:
                continue  # Skip this line

            # Process the lines containing significant alignments
            if line.startswith(">"):  # If it's a description line
                # The first part after '>' is the protein name
                description = line.split()[0][1:]
                # Get the protein ID, remove '>'
                best_matches.add(description)  # Add to the set of best matches

            # A blank line indicates the end of this query's results
            if line == "":
                continue

    # Write the unique results sorted to the output file
    with open(output_file, "w") as outfile:
        for match in sorted(best_matches):
            outfile.write(match + "\n")
