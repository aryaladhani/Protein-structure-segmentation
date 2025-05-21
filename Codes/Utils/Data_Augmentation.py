
def average_sequence_length(data):
    sum =0
    for i in range(len(data)):
        sum += len(data[i][1])
    print("Arya")
    return (sum//len(data))

def add_amino_acids(protein, avg):
    n = len(protein)
    x = avg - n
    protein2 = protein + x*str('A')
    return protein2

def remove_amino_acids(protein,avg):
    n = len(protein)
    x = n - avg
    protein2 = protein[x//2:x//2+avg]
    return protein2

def augment_protein_sequence(data):
    avg = average_sequence_length(data)
    for i in range (len(data)):
        if (len(data[i][1])>avg):
            data[i][1] = remove_amino_acids(data[i][1],avg)
        else:
            data[i][1] = add_amino_acids(data[i][1],avg)
    return data 
    



