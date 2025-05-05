#!/bin/bash
#SBATCH --job-name=convey_research
#SBATCH -N128
#SBATCH -n128
#SBATCH -C cpu
#SBATCH -t30
#SBATCH -qregular          
#SBATCH -ompi_isx_31_b

echo "Started on `/bin/hostname`"   # prints name of compute node job was started on
cd $SLURM_SUBMIT_DIR                # changes into directory where script was submitted from

# source setup.sh
# cd shubh/ISx-Actor/SHMEM
for i in {1..2}; do
    # srun -N 1 -n 128 ./bin/isx.strong 2147483648 output_strong_128
    # srun -N 2 -n 256 ./bin/isx.strong 2147483648 output_strong_256
    # srun -N 4 -n 512 ./bin/isx.strong 2147483648 output_strong_512
    # srun -N 8 -n 1024 ./bin/isx.strong 2147483648 output_strong_1024
    # srun -N 16 -n 2048 ./bin/isx.strong 2147483648 output_strong_2048
    # srun -N 32 -n 4096 ./bin/isx.strong 2147483648 output_strong_4096
    #srun -N 64 -n 8192 ./bin/isx.strong 2147483648 output_strong_8192
    srun -N 128 -n 16384 ./bin/isx.strong 2147483648 output_strong_16384

    # srun -N 1 -n 128 ./bin/isx.weak 2147483648 output_weak_128
    # srun -N 2 -n 256 ./bin/isx.weak 2147483648 output_weak_256
    # srun -N 4 -n 512 ./bin/isx.weak 2147483648 output_weak_512
    # srun -N 8 -n 1024 ./bin/isx.weak 2147483648 output_weak_1024
    # srun -N 16 -n 2048 ./bin/isx.weak 2147483648 output_weak_2048
    # srun -N 32 -n 4096 ./bin/isx.weak 2147483648 output_weak_4096
    # srun -N 64 -n 8192 ./bin/isx.weak 2147483648 output_weak_4096

    # srun -N 1 -n 128 ./bin/isx.weak_iso 2147483648 output_weak_iso_128
    # srun -N 2 -n 256 ./bin/isx.weak_iso 2147483648 output_weak_iso_256
    # srun -N 4 -n 512 ./bin/isx.weak_iso 2147483648 output_weak_iso_512
    # srun -N 8 -n 1024 ./bin/isx.weak_iso 2147483648 output_weak_iso_1024
    # srun -N 16 -n 2048 ./bin/isx.weak_iso 2147483648 output_weak_iso_2048
    # srun -N 32 -n 4096 ./bin/isx.weak_iso 2147483648 output_weak_iso_4096
    # srun -N 64 -n 8192 ./bin/isx.weak_iso 2147483648 output_weak_iso_4096
done