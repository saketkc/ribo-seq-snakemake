GENOMES_DIR = '/home/cmb-panasas2/skchoudh/genomes'
OUT_DIR = '/staging/as/skchoudh/rna/September_2017_Shalgi_et_al_Cell_2013'
SRC_DIR = '/home/cmb-panasas2/skchoudh/github_projects/clip_seq_pipeline/scripts'
RAWDATA_DIR = '/home/cmb-06/as/skchoudh/dna/September_2017_Shalgi_et_al_Cell_2013/sra_single_end_mouse'
GENOME_BUILD = 'mm10'
GENOME_FASTA = GENOMES_DIR + '/' + GENOME_BUILD + '/fasta/'+ GENOME_BUILD+ '.fa'
STAR_INDEX = GENOMES_DIR + '/' + GENOME_BUILD + '/star_annotated'
GTF = GENOMES_DIR + '/' + GENOME_BUILD + '/annotation/' + 'gencode.vM11.annotation.without_rRNA_tRNA.gtf'
GENE_NAMES = GENOMES_DIR + '/' + GENOME_BUILD + '/annotation/' + GENOME_BUILD+'_gene_names_stripped.tsv'
GTF_UTR = GENOMES_DIR + '/' + GENOME_BUILD + '/annotation/' + 'gencode.vM11.gffutils.modifiedUTRs.gtf'
GENE_LENGTHS = GENOMES_DIR + '/' + GENOME_BUILD + '/annotation/' + 'gencode.vM11.coding_lengths.tsv'  #+ GENOME_BUILD+'_gene_lengths.tsv'
HTSEQ_STRANDED = 'yes'
FEATURECOUNTS_S = '-s 1'
GENE_BED = GENOMES_DIR + '/' + GENOME_BUILD + '/annotation/' + 'mm10.vM11.genes.fromUCSC.bed'  #+ GENOME_BUILD+'_gene_lengths.tsv'
START_CODON_BED = GENOMES_DIR + '/' + GENOME_BUILD + '/annotation/' + 'gencode.vM11.gffutils.start_codon.bed'  #+ GENOME_BUILD+'_gene_lengths.tsv'
STOP_CODON_BED = GENOMES_DIR + '/' + GENOME_BUILD + '/annotation/' + 'gencode.vM11.gffutils.stop_codon.bed'  #+ GENOME_BUILD+'_gene_lengths.tsv'
FEATURECOUNTS_T='CDS'
HTSEQ_MODE='intersection-strict'
