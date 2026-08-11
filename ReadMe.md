# Multi-Read Variant Calling Pipeline

A Python-based bioinformatics pipeline that compares multiple sequencing reads against a reference DNA sequence, identifies nucleotide variants, and calculates read support for each variant.

## Overview

This project extends a basic variant-calling workflow to process multiple sequencing reads.

Instead of comparing one read against a reference, the pipeline:

1. Reads a reference sequence from a FASTA file.
2. Reads multiple sequencing reads from a FASTA file.
3. Compares each read against the reference.
4. Identifies nucleotide variants.
5. Combines variants found across all reads.
6. Calculates how many reads support each variant.
7. Writes the results to a VCF-style output file.

## Features

- FASTA file parsing
- Multi-read sequence processing
- Nucleotide variant detection
- Variant aggregation across reads
- Read-support calculation
- VCF-style output
- Modular Python functions
- Command-line execution

## Project Structure

```text
bioinformatics-multi-read-variant-calling-pipeline/
│
├── multi_read_variant_calling_pipeline.py
├── reference.fasta
├── reads.fasta
├── variants.vcf
└── README.md

## Author

Solomon Ketyebelu