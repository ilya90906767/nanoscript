from Bio import SeqIO
from minineedle import smith
from standart_primers import primers
import argparse 
import os


parser = argparse.ArgumentParser(description='Programm for trim')
parser.add_argument('-i','--InFasta', type=str, help="Input dir of fasta to process")
parser.add_argument('-o','--OutDir', type=str, help="Directory for results")
args = parser.parse_args()

absIn = str(os.path.abspath(args.InFasta)) 
absOut = os.path.abspath(args.OutDir) 

def FilterSW_new(file):
    record_list = list(SeqIO.parse(fr"{file}","fastq"))
    seq_list = [record_list[s].seq for s in range(len(record_list))]
    for no_seq in range(len(seq_list)):
        score = []
        for pr in range(1,21):
            aligment = smith.SmithWaterman((primers[f'primer{pr}']),seq_list[no_seq])
            score.append(aligment.get_score())
            max_score = max(score)
            max_index = score.index(max_score)
        if max_score >= 17:
            #matches[max_index].append(record_list[no_seq])
            with open(f"Result.fastq", "a") as output_handle:
                SeqIO.write(record_list[no_seq], output_handle, "fastq")           
    return 

FilterSW_new(absIn)
