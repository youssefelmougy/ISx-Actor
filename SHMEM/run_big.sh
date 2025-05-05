#!/bin/bash
#SBATCH --job-name=convey_research
#SBATCH -N128
#SBATCH -n128
#SBATCH -C cpu
#SBATCH -t90
#SBATCH -qregular          
#SBATCH -oshmem_isx

echo "Started on `/bin/hostname`"   # prints name of compute node job was started on
cd $SLURM_SUBMIT_DIR                # changes into directory where script was submitted from

# source setup.sh
# cd shubh/ISx-Actor/SHMEM

for i in {1..3}; do
    srun -N 64 -n 8192 ./bin/isx.strong 134217728 output_strong_8192
    srun -N 128 -n 16384 ./bin/isx.strong 134217728 output_strong_16k

    srun -N 64 -n 8192 ./bin/isx.weak 134217728 output_weak_8192
    srun -N 128 -n 16384 ./bin/isx.weak 134217728 output_weak_16k
    
    srun -N 64 -n 8192 ./bin/isx.weak_iso 134217728 output_weak_iso_8192
    srun -N 128 -n 16384 ./bin/isx.weak_iso 134217728 output_weak_iso_16k
done