def read_fasta(filename):                      # Read a FASTA file and return a list of sequences
    file = open(filename, "r")
    line = file.readline().strip()
    sequences=[ ]
    while line:
        sequence = file.readline().strip()
        sequences.append(sequence)

        line = file.readline().strip()
    file.close()
    return sequences

def find_variants(reference, read):            # Find variants between reference and read sequences
    variants =[ ]
    for i in range(len(read)):
         if read[i] != reference [i]:
            variants.append({ "Position": i + 1,"Reference": reference[i],"Alternate": read[i] })
    return variants

def write_variants(filename, variants, variant_counts):  # Write the variants to a VCF-style file including the read support for each variant
    variants_file = open(filename, "w")
    variants_file.write("Position\tReference\tAlternate\tReadSupport\n")
    for variant in variants:
        key = (variant["Position"], variant["Reference"], variant["Alternate"])     # Create a key for the variant to look up its read support
        variants_file.write(str(variant["Position"]) + "\t" + variant["Reference"] + "\t" + variant["Alternate"] +  "\t" + str(variant_counts[key]) + "\n")
    variants_file.close()

def main():
    reference = read_fasta("reference.fasta")[0]       
    reads = read_fasta("reads.fasta")   
    all_variants = [ ]
    variant_counts = { }
    for read in reads:                                  
        variants = find_variants(reference, read)
        all_variants.extend(variants)                  
        for variant in variants:
            key = (variant["Position"], variant["Reference"], variant["Alternate"])
            if key in variant_counts:
                variant_counts[key] += 1
            else:
                variant_counts[key] = 1
    write_variants("variants.vcf", all_variants, variant_counts)
    print("Variant calling complete.")
    print("Variants found:", len(all_variants))
    print("Results written to variants.vcf")

if __name__ == "__main__":
    main()
    
