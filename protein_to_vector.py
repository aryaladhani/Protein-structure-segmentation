import numpy as np

protein_set ={
    "A":0,
    "C":1,
    "D":2,
    "E":3,
    "F":4,
    "G":5,
    "H":6,
    "I":7,
    "K":8,
    "L":9,
    "M":10,
    "N":11,
    "P":12,
    "Q":13,
    "R":14,
    "S":15,
    "T":16,
    "V":17,
    "W":18,
    "Y":19
}

def hot_encode_protein(protein_sequence):
  encoded_sequence = np.zeros((len(protein_sequence),20))
  for i in range(len(protein_sequence)):
    j = protein_set[protein_sequence[i]]
    encoded_sequence[i][j]=1
  return encoded_sequence

# 