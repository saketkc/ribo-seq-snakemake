#!/usr/bin/env Rscript

suppressMessages(library(docopt))
suppressMessages(library(readr))
suppressMessages(library(DESeq2))
suppressMessages(library('RColorBrewer'))
suppressMessages(library('gplots'))
suppressMessages(library('BiocParallel'))
register(MulticoreParam(4))

"Perform differetioan expressiona analysis
Usage:
  do_DE_analysis.R --basedir=<basedir> --design_file=<design_file> --gene_annotations=<gene_annotations> --outprefix=<outprefix> --inprefix=<inprefix>

  Options:
    --basedir=<basedir>                      Absolute path to base directory
    --design_file=<design_file>              Absolute path to design matrix file
    --inprefix=<inprefix>                    Prefix for counts file
    --outprefix=<outprefix>                  Outprefix
    --gene_annotations=<gene_annotations>    Annotation file

" -> doc

opts <- docopt(doc)

base_dir <- opts[['basedir']]
design_file <- opts[['design_file']]
outprefix <- opts[['outprefix']]
gene_annotations <- opts[['gene_annotations']]
gene_annotations <- read.table(gene_annotations, row.names = 1, col.names = c('id', 'name', 'type'))
inprefix <- opts[['inprefix']]

design.info <- read.csv(design_file, header = TRUE, stringsAsFactors=FALSE)
sample_id <- design.info$sample
files <- paste(sample_id, inprefix, 'tsv', sep='.')
names(files) <- sample_id
condition <- design.info$condition

sampleTable <- data.frame(sampleName=sample_id, fileName=files, condition = condition)
ddsHTSeq <- DESeqDataSetFromHTSeqCount(sampleTable=sampleTable, directory=base_dir, design=~condition)
## We dont need version numbers
rownames(ddsHTSeq) <- gsub('\\.[0-9]+', '', rownames(ddsHTSeq))
## Filter genes with atleast 2 count
ddsHTSeq <- ddsHTSeq[ rowSums(counts(ddsHTSeq)) > 1,  ]

colData(ddsHTSeq)$condition<-factor(colData(ddsHTSeq)$condition, levels=c('control', 'clone3', 'clone5'))

## Analyze with DESeq2
dds <- DESeq(ddsHTSeq)
res.clone3VScontrol <- results(dds, contrast=c('condition', 'clone3', 'control'))
resOrdered.clone3VScontrol <- res.clone3VScontrol[order(res.clone3VScontrol$padj),]
write.table(as.data.frame(resOrdered.clone3VScontrol), paste(outprefix, 'clone3_VS_control', 'all', 'tsv', sep='.'))
resSig.clone3VScontrol <- subset(resOrdered.clone3VScontrol, padj < 0.05)
write.table(as.data.frame(resSig.clone3VScontrol), paste(outprefix, 'clone3_VS_control', 'sig', 'tsv', sep='.'))
gene_name <- gene_annotations[row.names(resSig.clone3VScontrol),]$name
resSig.clone3VScontrol <- as.data.frame(resSig.clone3VScontrol)
resSig.clone3VScontrol$gene_name <- gene_name
write.table(as.data.frame(resSig.clone3VScontrol), paste(outprefix, 'clone3_VS_control', 'sig', 'names', 'tsv', sep='.'))

res.clone5VScontrol <- results(dds, contrast=c('condition', 'clone5', 'control'))
resOrdered.clone5VScontrol <- res.clone5VScontrol[order(res.clone5VScontrol$padj),]
write.table(as.data.frame(resOrdered.clone5VScontrol), paste(outprefix, 'clone5_VS_control', 'all', 'tsv', sep='.'))
resSig.clone5VScontrol <- subset(resOrdered.clone5VScontrol, padj < 0.05)
write.table(as.data.frame(resSig.clone5VScontrol), paste(outprefix, 'clone5_VS_control', 'sig', 'tsv', sep='.'))
#row.names(resSig.clone5VScontrol) <- gene_annotations[row.names(resSig.clone5VScontrol),]$name
gene_name <- gene_annotations[row.names(resSig.clone5VScontrol),]$name
resSig.clone5VScontrol <- as.data.frame(resSig.clone5VScontrol)
resSig.clone5VScontrol$gene_name <- gene_name
write.table(as.data.frame(resSig.clone5VScontrol), paste(outprefix, 'clone5_VS_control', 'sig', 'names', 'tsv', sep='.'))
