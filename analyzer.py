#!/usr/bin/python
import os
from os import system
from subprocess import call

def jobstring_sbatch(T,R,S):
	'''
	This function creats jobstring for #SBATCH script
	'''
	job_name       = "MyjobT"+str(T)+"R"+str(R)+"S"+str(S)
	walltime       = "40-00:00"
	omp_thread     = 1
#    logPath        = "/home/l2mcgrat/MBPolPaperN8/output_files/"+job_name

	exe_file       = "/home/l2mcgrat/MMTK/bin/python test-pimd-energy_analysis.py /work/l2mcgrat/trajectoryfiles/N8H20T"+str(T)+"P1R"+str(R)+"FilePVersion"+str(S)+"StepsDip.nc"

	job_string     = """#!/bin/bash
#SBATCH --job-name=%s
#SBATCH --output=%s.out
%s
""" % (job_name, job_name, exe_file)

	return job_string

# Main function

RList = [0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.6, 2.0, 2.5, 3.0]
TList = [15.0, 70.0, 95.0, 293.0]
SList = [100000, 1000000]

print(TList)
print(RList)
print(SList)

for S in SList:
    for R in RList:
        for T in TList:
            fname="job-T"+str(T)+"R"+str(R)+"S"+str(S)
            fileName = open(fname,'w')
            fileName.write(jobstring_sbatch(T,R,S))
            fileName.close()
            call(["sbatch", fname])
            call(["rm", fname])

