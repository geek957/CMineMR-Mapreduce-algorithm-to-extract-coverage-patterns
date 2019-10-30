#!/bin/bash
#SBATCH -A research
#SBATCH --qos=medium
#SBATCH -n 20 -wnode49
#SBATCH --mem-per-cpu=2048
#SBATCH --time=06:00:00
#SBATCH --mail-type=END
python run.py
