#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

# Nucleotides and beginning of sequence saved in variables
nts = 'ATGC'
start_seq = 'AGGT'
end_seq = 'CGAA'

# Dictionary of TFs and their respective binding sites
tfbs = {"PDX1": "TCTAAT", "MAFA": "TGCA", "SP1": "CCGCCC"}

# Function to add transcription factors binding sites to sequence
def tf_addition(nwseq):
    no = random.randint(1, 6)  # Randomly generate between 1-6 TFs
    diffpos = random.sample(range(50, 400), no)  # Random positions for binding sites
    for pos in diffpos:
        tf_choice = random.choice(list(tfbs.values()))  # Randomly choose TF binding site
        nwseq = nwseq[:pos] + tf_choice + nwseq[pos + len(tf_choice):]
    return nwseq

# List to save 100 sequences
seqlist = []

# To create 100 sequences
for k in range(100):
    nwseq = start_seq  # Starting sequence 'AGGT'
    
    # Creating the random part of the sequence between 4th and 496th nucleotide
    for i in range(0, 492):
        randseq = random.choice(nts)
        nwseq += randseq
    
    # Adding end nucleotides to the sequence ('CGAA')
    nwseq += end_seq
    
    # Adding Inr motif at the 450th position
    pyr = 'CT'
    pur = 'AG'
    Y = random.choice(pyr)
    R = random.choice(pur)
    inr_motif = Y + R
    nwseq = nwseq[:449] + inr_motif + nwseq[451:]  # Replacing the sequence at position 450-451 with Inr
    
    # Random value between 24 and 31 to position the TATA-box upstream of the TSS (450th position)
    tatapos = random.randint(24, 31)
    tata_position = 450 - tatapos
    
    # Inserting the TATA-box at the randomly determined position
    nwseq = nwseq[:tata_position] + 'TATAA' + nwseq[tata_position + 5:]
    
    # Adding transcription factor binding sites to the sequence
    nwseq = tf_addition(nwseq)
    
    # Appending the created sequence to the list
    seqlist.append(nwseq)

# Converting the list to a string to save to a file
seqlist_str = '\n'.join(seqlist)

# Saving the sequences to a file named 'promoters.txt'
with open('promoters.txt', 'w') as file:
    file.write(seqlist_str)

