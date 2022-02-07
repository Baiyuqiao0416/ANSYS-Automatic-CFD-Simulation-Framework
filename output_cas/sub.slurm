#!/bin/bash
#SBATCH -n 72
#SBATCH -N 1


srun hostname | sort -V > hosts
sed -i 's/$/-ens93/g' hosts
/usr/ansys_inc/v202/fluent/bin/fluent 3ddp -g -t$SLURM_NTASKS -cflush -i ./journal.jou -cnf=hosts