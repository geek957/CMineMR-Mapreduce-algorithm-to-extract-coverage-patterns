#!/bin/bash
#SBATCH -A research
#SBATCH --qos=medium
#SBATCH -n 10
#SBATCH --mem-per-cpu=2048
#SBATCH --time=4-00:00:00
#SBATCH --mail-type=END
python run.py
