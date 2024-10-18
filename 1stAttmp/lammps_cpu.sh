#!/bin/bash
# 
#
# Julia job submission script
#
# TODO:
#   - Set name of the job below changing "BWA" value.
#   - Set the requested number of nodes (servers) with --nodes parameter.
#   - Set the requested number of tasks (cpu cores) with --ntasks parameter. (Total accross all nodes)
#   - Select the partition (queue) you want to run the job in:
#     - nodesloq : For cpu nodes
#   - Set the required time limit for the job with --time parameter.
#     - Acceptable time formats include "minutes", "minutes:seconds", "hours:minutes:seconds", "days-hours", "days-hours:minutes" and "days-hours:minutes:seconds"
#   - Put this script and all the input file under the same directory.
#   - Set the required parameters, input/output file names below.
#   - If you do not want mail please remove the line that has --mail-type and --mail-user. If you do want to get notification emails, set your email address.
#   - Put this script and all the input file under the same directory.
#   - Submit this file using:
#      sbatch lammps_submit.sh
#
# -= Resources =-
#
#SBATCH --job-name=lammps-droplet
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=80
#SBATCH --partition=nodesloq
#SBATCH --time=1-0
#SBATCH --output=../../output/01_systemcreation/slurm/%j-slurm.log
#SBATCH --mail-type=ALL
#SBATCH --mail-user=foo@toyota-europe.com


OUT_DIR=output/4Iλ13p5
HOST_DIR=$OUT_DIR/slurm/
INPUT="4Iλ13p5/input_4Iλ13p5.lammps"

################################################################################
##################### !!! DO NOT EDIT BELOW THIS LINE !!! ######################
################################################################################

## Load LAMMPS Parallel
echo "lammps/11Aug17 loading.."
#module load cuda12.3/toolkit/12.3.1
#module load openmpi3/gcc/64/3.1.6
#module load ffmpeg/4.4.2
#module load lammps/23jun2022_mpi_cpu

echo
echo "====== ENVIRONMENT VARIABLES ======"
env
echo "==================================="
echo

# Set stack size to unlimited
echo "Setting stack size to unlimited..."
echo "===================================="
ulimit -s unlimited
ulimit -l unlimited
ulimit -a
echo "===================================="
echo

################################################################################
##################### !!! DO NOT EDIT ABOVE THIS LINE !!! ######################
################################################################################


HOSTFILE=$HOST_DIR/hosts.$SLURM_JOB_ID
srun hostname -s > $HOSTFILE

export OMP_NUM_THREADS=$SLURM_NTASKS_PER_NODE
#export OMP_NUM_THREADS=1

PARALLEL=/cm/shared/apps/lammps/lammps-mpi-23Jun2022_cpu/bin/lmp 
MPI=/cm/shared/apps/openmpi3/gcc/64/3.1.6/bin/mpirun

echo "Running LAMMPS command..."
echo "==========================="
# PARALLEL
$MPI -n $SLURM_NTASKS_PER_NODE -machinefile $HOSTFILE $PARALLEL -in $INPUT -log $OUT_DIR/log.lammps
RET=$?
echo ""

echo "Remove Hostfile..."
rm $HOSTFILE

echo "RTC exited with return code: $RET"
echo "----------------------------------"
exit $RET
echo "----------------------------------"
