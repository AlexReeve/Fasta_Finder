from Bio import SeqIO

def fasta_find(database, target):
    """
    Searches for a Fasta sequence in a Fasta file by their ID Numbers
    Produces a maximum of ten results for each sequence.
    
    Args:    database = Fasta file
             target = ID Number
    Returns: Nothing.
    example:database = "NewYersinia1.faa"
             codes = "NY1000092"
             fasta_find(database, codes)
    
    """
    #what fasta file are we searching in
    fastas = list(SeqIO.parse(database, "fasta"))
    
    if len(target) <= 0:
        raise ValueError("No Fatsa ID present. Please enter a Fasta ID")
    # make a boolean - this will tell us if we have a match
   
    match_success = False 
    ##add a count 
    count = 0
    for record in fastas:
        if target in record.description:
            print(f"Match found for target {target}")
            print(f"ID: {record.description}")
            print(record.seq)
            print(f"Sequence length = {len(record.seq)}")
            # we have a match, so tell the boolean
            match_success = True
            #add one to a count for each search
            count += 1
            #set a maximum search return
            if count >= 11:
                raise ValueError(f"Too many results from your search {target}. Please make your search more specific")
                
     # tell me if there was no match for the sequence
    if match_success == False:
        print(f"No matches found for target {target}")
                




# Lets search - from command line :) 

import sys

fasta_find(sys.argv[1], sys.argv[2])
# example input = "NewYersinia1.faa.faa" , "NY100009"