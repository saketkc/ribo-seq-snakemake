#!/bin/bash
snakemake --snakefile Snakefile.riboraptor\
    --config config_path=configs/$1.py\
    --js $PWD/jobscript.sh\
    --printshellcmds\
    --cluster-config $PWD/cluster.riboraptor.yaml\
    --jobname "$1.{jobid}.{rulename}"\
    --keep-going\
    --stats $PWD/$1.riboraptor.stats\
    --timestamp\
    --rerun-incomplete\
    -j 100\
    --cluster 'qsub -q cmb -S /bin/bash -V -l walltime={cluster.time} -l mem={cluster.mem} -l vmem={cluster.mem} -l pmem={cluster.mem} -l nodes=1:ppn={cluster.cores} -o {cluster.logdir} -e {cluster.logdir}'
