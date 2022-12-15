def sequence_extraction(data_dir,protein_category):
    f = open(data_dir)
    lines = f.read() 
    lines = lines.split('>')
    out = [[0 for x in range(3)] for y in range(len(lines))]
    for i in range(len(lines)):
        lines[i] = lines[i].split(' ')
        out[i][0]= lines[i][0]
        out [i][1] = lines[i][-1]
        out[i][1] = out[i][1].split('\n')
        protein_sequence = ""
        for j in range(len(out[i][1])):
            protein_sequence+= out[i][1][j]
        out[i][1]=protein_sequence
        if (protein_category=='positive'):
            out[i][2]=1
        else :
            out[i][2]=0
    return out[1:]
