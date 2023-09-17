# Fasta_Finder
This file contains the code written for a group project for my 2022 Masters degree. The project called for us to create a python code that finds a given fasta sequence within a database.
I created two functions to fufill this brief. 
Fastafinder =     Searches for a Fasta sequence in a Fasta file by their ID Numbers
                  Produces a maximum of ten results for each sequence.
                  example use = python FastaFinder.py "NewYersinia1.faa" , "NY100009"

MultiFastaFinder =     Searches for multiple Fasta sequences in a Fasta file by their ID Numbers.
                        Produces a maximum of ten results for each sequence.
                        MultiFastaFinder currently only works as a funcition, not a stand-alone python file.
                        Import multi_fasta_find from MultiFastaFinder for use as multi_fasta_find(database, list_of_codes_to_find)
                        
