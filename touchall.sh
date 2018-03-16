#!/bin/bash
snakemake --snakefile Snakefile\
    --touch\
    --config config_path=configs/$1.py
