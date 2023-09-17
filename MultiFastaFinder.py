from Bio import SeqIO

def multi_fasta_find(fastas, targets):
    """
    Searches for multiple Fasta sequences in a Fasta file by their ID Numbers.
    Produces a maximum of ten results for each sequence.
    
    Args:    fastas = Fasta file. Must be saved in the same location as MultiFasterFinder.
             target = ID Numbers as a list, even if searching for only one ID.
    Returns: Nothing.
    example:database = "NewYersinia1.faa"
             codes = ["NY1000092", "NY1000093"]
             fasta_find(database, codes)
    
    """
    # load in database
    database = list(SeqIO.parse(fastas, "fasta"))
    if len(targets) <= 0:
        raise ValueError("No Fatsa ID present. Please enter a Fasta ID")
    # make a boolean - this will tell us if we have a match
    for item in targets:
        match_success = False 
        ##add a count 
        count = 0
        for record in database:
            if item in record.description:
                print(f"Match found for target {item}")
                print(f"ID: {record.description}")
                print(record.seq)
                print(f"Sequence length = {len(record.seq)}")
                # we have a match, so tell the boolean
                match_success = True
                #add one to a count for each search
                count += 1
                #set a maximum search return
                if count >= 11:
                    raise ValueError(f"Too many results from your search {item}. Please make your search more specific")
                
         # tell me if there was no match for the sequence
        if match_success == False:
            print(f"No matches found for target {item}")
                


# what fasta file are we searching in
#database = "NewYersinia1.faa.faa"

# what fasta code/codes are we looking for (must be in a list, even with only one id)
#codes = ["NY100009", "NY1000093_NewYersinia1"]

# Lets search :) 
#multi_fasta_find(database, codes)
