import argparse
from pdb import set_trace as stop

def build_check_query(length, index, query_list, reference_list):

    if length < 12:
        return []

    duplicate_matches = []

    for i in range(12, length):
        built_strand = query_list[index:index+i]

        if built_strand in reference_list:
            duplicate_matches.append(built_strand)
        
    if duplicate_matches:
        return duplicate_matches[-1]
    else:
        return []
    
parser = argparse.ArgumentParser()

parser.add_argument('-f', '--filename')

args = parser.parse_args()

query = ""
reference = ""

with open(args.filename, 'r') as f:
    for line in f:
        #pdb.set_trace()
        if not query:
            query = line
        else:
            reference = line

mismatch = 0;
            
for i in range(len(query)):
    if (list(query)[i] != list(reference)[i]) and (list(query)[i] != '-'):
        mismatch += 1


#pdb.set_trace()
percent_match = (len(query) - mismatch) / float(len(reference)) * 100
print("{0:.2f}% match".format(percent_match))

if percent_match < 70:
    print("Match needs to be at least 70%")
    exit(1)

i = 0
while i < (len(reference)):
    if list(reference)[i] == '-':
        for j in range(i, len(reference)):
            if list(reference)[j] != '-':
                length_of_mystery = j - (i - 1)
                #stop()
                built_strand =  build_check_query(length_of_mystery, i, query, reference)
                if any(built_strand):
                    print(built_strand)
    
                i += j + 1
                break
    i += 1
