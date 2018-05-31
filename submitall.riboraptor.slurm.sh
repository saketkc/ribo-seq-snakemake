#!/bin/bash
snakemake --snakefile Snakefile.riboraptor\
    --config config_path=configs/$1.py\
    --js $PWD/jobscript.slurm.sh\
    --printshellcmds\
    --cluster-config $PWD/cluster.riboraptor.slurm.yaml\
    --jobname "$1.{rulename}.{jobid}"\
    --keep-going\
    --stats $PWD/$1.riboraptor.stats\
    --timestamp\
    --rerun-incomplete\
    -j 4\
    --cluster 'sbatch --partition=cmb --ntasks={cluster.cores} --mem={cluster.vmem} --mem-per-cpu={cluster.mem} --time={cluster.time} -o {cluster.out} -e {cluster.err}'
# -A {cluster.account} -
