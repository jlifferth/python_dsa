import numpy as np
from datetime import datetime
import gzip
from mimetypes import guess_type
from functools import partial
from Bio import SeqIO


def map_nucs(seq):
    mapped_seq = []
    for nuc in seq:
        if nuc == 'A':
            mapped_seq.append(1)
        elif nuc == 'T':
            mapped_seq.append(2)
        elif nuc == 'G':
            mapped_seq.append(3)
        elif nuc == 'C':
            mapped_seq.append(4)
    return mapped_seq


def pad(x, _max_len):
    return x + [0] * (_max_len - len(x))


def unmap_nucs(seq):
    # unmap [int] to str
    unmapped_seq = ''
    for nuc in seq:
        if nuc == 1:
            unmapped_seq += 'A'
        elif nuc == 2:
            unmapped_seq += 'T'
        elif nuc == 3:
            unmapped_seq += 'G'
        elif nuc == 4:
            unmapped_seq += 'C'
        elif nuc == 0:
            pass
    return unmapped_seq


# combine steps into single function to obtain unique seq counts for a fastq file
def get_unique_seqs(filepath):
    start = datetime.now()

    encoding = guess_type(filepath)[1]  # uses file extension
    _open = partial(gzip.open, mode='rt') if encoding == 'gzip' else open

    Left_flank = 'taacttgcagcagcaaGGC'
    Right_flank = 'GCCaacacggctcctcaaa'

    Left_flank = Left_flank.upper()
    Right_flank = Right_flank.upper()

    # extract insert seqs from fastq file
    insert_seqs = []
    with _open(filepath) as f:
        for record in SeqIO.parse(f, 'fastq'):
            if Left_flank in record.seq and Right_flank in record.seq:
                seq_start = record.seq.find(Left_flank) + len(Left_flank)
                seq_end = record.seq.find(Right_flank)
                seq = record.seq[seq_start:seq_end]
                insert_seqs.append(str(seq))
    print('# of insert_seqs: ', len(insert_seqs))

    # map insert to ints for faster processing
    insert_seqs = [map_nucs(x) for x in insert_seqs]

    _max_len = len(max(insert_seqs, key=len))

    # pad mapped seq values for matrix
    padded_insert_seqs = [pad(x, _max_len) for x in insert_seqs]

    # convert padded seqs to np matrix
    insert_matrix = np.asarray(padded_insert_seqs)

    # isolate unique seqs and seq counts
    unique_seqs, counts = np.unique(insert_matrix, axis=0, return_counts=True)

    print('# of unique_seqs: ', len(unique_seqs))

    # unmap int values back to str
    unmapped_unique_seqs = [unmap_nucs(x) for x in unique_seqs]

    # create dict with unique seqs and counts
    unique_seqs_dict = {unmapped_unique_seqs[i]: counts[i] for i in range(len(unmapped_unique_seqs))}

    # sort dict by descending count values
    unique_seqs_sorted = sorted(unique_seqs_dict.items(), key=lambda x: x[1], reverse=True)

    end = datetime.now()
    elapsed = end - start
    print('elapsed time: ', elapsed)

    return unique_seqs_sorted
