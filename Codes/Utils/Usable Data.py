import numpy as np

protein_set ={
    'A':0,
    'C':1,
    'D':2,
    'E':3,
    'F':4,
    'G':5,
    'H':6,
    'I':7,
    'K':8,
    'L':9,
    'M':10,
    'N':11,
    'P':12,
    'Q':13,
    'R':14,
    'S':15,
    'T':16,
    'V':17,
    'W':18,
    'Y':19
}
def get_process_data(protein_data):
  random_sequence = protein_data[0][1]
  protein_size = len(random_sequence)
  data_size = len(protein_data)
  inputs = np.zeros((data_size,protein_size,20))
  labels = np.zeros((data_size,1))
  for i in range(data_size):
    protein_sequence = protein_data[i][1]
    for j in range (len(protein_sequence)):
      amino_acid = protein_sequence[j]
      if (amino_acid=='B' or amino_acid=='J' or  amino_acid=='O' or amino_acid=='U' or amino_acid=='X' or amino_acid=='Z'  ):
        amino_acid ='A'
      # print(amino_acid.type())
      k = protein_set[amino_acid]
      inputs[i][j][k] = 1
    labels[i][0]=protein_data[i][2]
  
  return inputs, labels 
