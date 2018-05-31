GENOMES_DIR='/home/cmb-panasas2/skchoudh/genomes'
OUT_DIR = '/staging/as/skchoudh/rna/HuR_results/human/ribo-seq-isoform'
SRC_DIR = '/home/cmb-panasas2/skchoudh/github_projects/ribo-seq-snakemake/scripts'
GENOME_BUILD = 'hg38'
GENOME_FASTA = GENOMES_DIR + '/' + GENOME_BUILD + '/fasta/'+ GENOME_BUILD+ '.fa'
STAR_INDEX = GENOMES_DIR + '/' + GENOME_BUILD + '/star_annotated'
#GTF = GENOMES_DIR + '/' + GENOME_BUILD + '/annotation/' + 'gencode.v25.annotation.without_rRNA_tRNA.gtf'
GTF = GENOMES_DIR + '/' + GENOME_BUILD + '/annotation/' + 'gencode.v25.annotation.gtf'
GENE_NAMES = GENOMES_DIR + '/' + GENOME_BUILD + '/annotation/' + GENOME_BUILD+'_gene_names_stripped.tsv'
GENE_LENGTHS = GENOMES_DIR + '/' + GENOME_BUILD + '/annotation/' + 'gencode.v25.coding_lengths.tsv'  #+ GENOME_BUILD+'_gene_lengths.tsv'
HTSEQ_STRANDED = 'yes'
FEATURECOUNTS_S = '-s 1'
GENE_BED = GENOMES_DIR + '/' + GENOME_BUILD + '/annotation/' + 'gencode.24.genes.bed'  #+ GENOME_BUILD+'_gene_lengths.tsv'
FEATURECOUNTS_T='cds'
HTSEQ_MODE='union'

cDNA_FASTA = GENOMES_DIR + '/' + GENOME_BUILD + '/cDNA/'+ 'gencode.v25.transcripts.fa'
pcDNA_FASTA = GENOMES_DIR + '/' + GENOME_BUILD + '/cDNA/'+ 'gencode.v25.pc_transcripts.fa'
protein_FASTA =  GENOMES_DIR + '/' + GENOME_BUILD + '/cDNA/'+ 'gencode.v25.pc_translations.fa'

tRNA_FASTA = GENOMES_DIR + '/tRNA_eukaryotic/eukaryotic-tRNAs.fa'
ncRNA_FASTA = GENOMES_DIR + '/' + GENOME_BUILD + '/cDNA/'+ 'gencode.v25.lncRNA_transcripts.fa'
STAR_INDEX_DIR = GENOMES_DIR + '/' + GENOME_BUILD + '/star_index'

RAWDATA_DIR_RIBO = '/staging/as/skchoudh/dna/Penalva_02222017/Penalva_L_01182017'
RAWDATA_DIR_RNA = '/staging/as/skchoudh/dna/lai_data/Penalva_L_01182017'

#CDS_RANGE_FILE =  GENOMES_DIR + '/' + GENOME_BUILD + '/cDNA/'+ 'gencode.v25.transcripts.fa_cds.txt'
CDS_RANGE_FILE =  GENOMES_DIR + '/' + GENOME_BUILD + '/cDNA/'+ 'gencode.v25.pc_transcripts_cds.txt'
pcDNA_FASTA_FILTERED = GENOMES_DIR + '/' + GENOME_BUILD + '/cDNA/'+ 'gencode.v25.pc_transcripts_filter.fa'
CDS_FASTA_FILTERED = GENOMES_DIR + '/' + GENOME_BUILD + '/cDNA/'+ 'gencode.v25.pc_transaltions_filter.fa'


CONTAMINANT_FASTA = STAR_INDEX_DIR+'/contaminant/fasta/contaminant.fa'
