import gzip
from mimetypes import guess_type
from functools import partial
from Bio import SeqIO


def count_nucleotides(sequence_in):
    sequence_in = sequence_in.upper()
    A = "A : " + str(sequence_in.count('A'))
    G = "G : " + str(sequence_in.count('G'))
    T = "T : " + str(sequence_in.count('T'))
    C = "C : " + str(sequence_in.count('C'))
    N = "N : " + str(sequence_in.count('N'))
    return A, G, T, C, N


input_file = '/Users/jonathanlifferth/data/bioinformatics/Divergene/question2/liver cDNA/1153-cDNA-8V8_S30_L001_R1_001.fastq.gz'

encoding = guess_type(input_file)[1]  # uses file extension
print(encoding)
_open = partial(gzip.open, mode='rt') if encoding == 'gzip' else open

with _open(input_file) as f:
    for record in SeqIO.parse(f, 'fastq'):

        print(type(record))
        print(record)
        print(record.seq)
        print(count_nucleotides(record.seq))
        # break
