
# This program checks if any of the sequence in a query fasta file is present in the 
# reference fasta file (checks for sub-string) or not. If they are present, it removes it.
# The updated database will have sequences unique to query fasta file.

def main():
    import sys
    from Bio import SeqIO
    
    ref_fastaFile = sys.argv[1].strip()
    query_fastaFile = sys.argv[2].strip()
    
    x = SeqIO.to_dict(SeqIO.parse(ref_fastaFile, "fasta"))
    y = x.values()
    b = []
    for a in y:
        b.append(str(a.seq))
    ref_fastaSeq = "#".join(b)
    
    outfh = open(sys.argv[3].strip(), "w")
    
    x = SeqIO.to_dict(SeqIO.parse(query_fastaFile, "fasta"))
    y = x.values()
    count = 0
    for a in x.keys():
        seq = str(x[a].seq)
        desc = str(x[a].description)
        if ref_fastaSeq.find(seq) < 0:
            outfh.write(">" + desc + "\n" + seq + "\n")
        else:
            count = count + 1
    print >> sys.stdout,"Total Number of Sequences Removed: %d" % count
    outfh.close()
    return None

if __name__ == "__main__":
    main()
    
    
    


