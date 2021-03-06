GENOMES_DIR = '/home/cmb-panasas2/skchoudh/genomes'
OUT_DIR = '/staging/as/skchoudh/rna/Feb_02_2017_Radiation_GBM_EBV_Sept2017_ribo'
SRC_DIR = '/home/cmb-panasas2/skchoudh/github_projects/clip_seq_pipeline/scripts'
RAWDATA_DIR = '/home/cmb-06/as/skchoudh/dna/Luiz_radiation_data/Penalva_08242016_Run160902/Penalva_08242016'
GENOME_BUILD = 'hg38'
GENOME_FASTA = GENOMES_DIR + '/' + GENOME_BUILD + '/fasta/'+ GENOME_BUILD+ '.fa'
STAR_INDEX = GENOMES_DIR + '/' + GENOME_BUILD + '/star_annotated'
GTF = GENOMES_DIR + '/' + GENOME_BUILD + '/annotation/' + 'gencode.v25.annotation.without_rRNA_tRNA.gtf'
GENE_NAMES = GENOMES_DIR + '/' + GENOME_BUILD + '/annotation/' + GENOME_BUILD+'_gene_names_stripped.tsv'
GTF_UTR = GENOMES_DIR + '/' + GENOME_BUILD + '/annotation/' + 'gencode.v25.gffutils.modifiedUTRs.gtf'
GENE_LENGTHS = GENOMES_DIR + '/' + GENOME_BUILD + '/annotation/' + 'gencode.v25.coding_lengths.tsv'  #+ GENOME_BUILD+'_gene_lengths.tsv'
DESIGN_FILE = RAWDATA_DIR + '/' + 'design.txt'
HTSEQ_STRANDED = 'yes'
FEATURECOUNTS_S = '-s 1'
GENE_BED = GENOMES_DIR + '/' + GENOME_BUILD + '/annotation/' + 'gencode.24.genes.bed'  #+ GENOME_BUILD+'_gene_lengths.tsv'
FEATURECOUNTS_T = 'CDS'
HTSEQ_MODE = 'intersection-strict'



UTR5_BED = GENOMES_DIR + '/' + GENOME_BUILD + '/annotation/' + 'gencode.v25.gffutils.UTR5.bed'
UTR3_BED = GENOMES_DIR + '/' + GENOME_BUILD + '/annotation/' + 'gencode.v25.gffutils.UTR3.bed'

START_CODON_BED = GENOMES_DIR + '/' + GENOME_BUILD + '/annotation/' + 'gencode.v25.gffutils.start_codon.bed'  #+ GENOME_BUILD+'_gene_lengths.tsv'
STOP_CODON_BED = GENOMES_DIR + '/' + GENOME_BUILD + '/annotation/' + 'gencode.v25.gffutils.stop_codon.bed'  #+ GENOME_BUILD+'_gene_lengths.tsv'
PYTHON2ENV = 'python2'


CDS_BED = '/home/cmb-panasas2/skchoudh/genomes/hg38/annotation/gencode.v25.gffutils.cds.bed'
CHROM_SIZES = '/home/cmb-panasas2/skchoudh/genomes/hg38/fasta/hg38.chrom.sizes'
