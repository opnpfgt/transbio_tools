def gc_bound(seq: str) -> float:
    gc_content = (seq.count('g') + seq.count('c') + seq.count('G')
                  + seq.count('C')) / len(seq) * 100
    return gc_content


def avg_quality(quality: str) -> float:
    avg_qual = sum((ord(letter) - 33) for letter in quality) / len(quality)
    return avg_qual
