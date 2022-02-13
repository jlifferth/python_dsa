import pandas as pd
import time

t1_start = time.process_time()

# import csv from Google Drive
url = 'https://drive.google.com/uc?id=1UqwhclZtkAI3UDWaguzNj1VfFGpylDrF'
df = pd.read_csv(url)

# list of alleles that client wants
client_list = ['A*01:01', 'A*02:01', 'A*03:01', 'A*11:01', 'A*23:01', 'A*24:02', 'A*26:01', 'A*29:02', 'A*30:01',
               'A*30:02', 'A*31:01', 'A*32:01', 'A*33:03', 'A*68:01', 'A*68:02', 'B*35:01', 'B*07:02', 'B*40:01',
               'B*08:01', 'B*44:03', 'B*51:01', 'B*53:01', 'B*44:02', 'B*15:01', 'B*18:01', 'B*58:01', 'B*14:02',
               'B*27:05', 'B*15:03', 'B*48:01', 'B*52:01', 'B*42:01', 'B*49:01', 'B*57:01', 'B*13:02', 'B*39:01',
               'B*40:02', 'B*58:02', 'B*46:01', 'B*35:03', 'B*57:03', 'B*38:01', 'B*15:10', 'B*50:01', 'B*55:01',
               'B*15:02', 'B*37:01', 'B*54:01', 'B*38:02', 'B*45:01', 'B*81:01', 'B*07:05', 'B*14:01', 'B*35:02']

# split into separate allele lists
A_allele_list = []
B_allele_list = []

for haplotype in client_list:
    locus = haplotype[0]
    allele = haplotype[2:]
    if locus == 'A':
        A_allele_list.append(allele)
    elif locus == 'B':
        B_allele_list.append(allele)

# create dict with match count values for each cell line
samples = df.SampleID.unique()
match_counts = {}
for sample in samples:
    match_count = 0
    row = df[(df['SampleID'] == sample)].values[0]
    for A_allele in A_allele_list:
        if A_allele == row[3] or A_allele == row[4]:
            match_count += 1
    for B_allele in B_allele_list:
        if B_allele == row[5] or B_allele == row[6]:
            match_count += 1
    # print('match count: ', match_count)
    match_counts[sample] = match_count

# initialize client_list_matches with zeros values
client_list_matches = {}
for haplotype in client_list:
    client_list_matches[haplotype] = 0

# full search algorithm v2 - optimize to start by selecting cell lines with higher match counts
# this list contains cell lines that satisfy a client list requirement and should be ordered
cell_order_list = []

i = 4
while i > 0:
    for cell_line in match_counts:
        if match_counts[cell_line] == i:

            # we begin iteration with default assumption that sample does not satisfy requirement until proven otherwise
            order_sample = False
            row = df[(df['SampleID'] == cell_line)].values[0]
            A1 = 'A*' + row[3]
            A2 = 'A*' + row[4]
            B1 = 'B*' + row[5]
            B2 = 'B*' + row[6]
            row_alleles = [A1, A2, B1, B2]

            # determine if this cell line satisfies any client alleles that have not yet been matched
            for allele in row_alleles:
                if allele in client_list_matches:
                    if client_list_matches[allele] == 0:
                        order_sample = True

            if order_sample:
                # print('Order sample: ', cell_line)
                cell_order_list.append(cell_line)
                for allele in row_alleles:
                    if allele in client_list_matches:
                        client_list_matches[allele] += 1
            else:
                # print('Do not order sample: ', cell_line)
                continue
    i -= 1

print('Cell lines to order:', cell_order_list)
print('Length of cell order list:', len(cell_order_list))

# return process runtime
t1_stop = time.process_time()
elapsed_time = t1_stop - t1_start
print("Elapsed runtime:", elapsed_time)
