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

	exe_file       = "/home/l2mcgrat/MMTK/bin/python FSimStart.py H2O_T"+str(T)+"t1.rho H2O_T"+str(T)+"t1.eng H2O_T"+str(T)+"t1.esq "+str(S)+" "+str(R)+" 1"

	job_string     = """#!/bin/bash
#SBATCH --job-name=%s
#SBATCH --output=%s.out
%s
""" % (job_name, job_name, exe_file)

	return job_string

# Main function

RList = [3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0, 16.0, 20.0, 25.0, 30.0]
TList = [15, 70, 95, 293]        #4                   #5                     #6                    #8                    #10                    #12                    #16                   #20                   #25                   #30
SList = [0.1, 0.15, 0.15, 0.15, 0.15, 0.2, 0.2, 0.18, 0.2, 0.25, 0.25, 0.2, 0.25, 0.3, 0.3, 0.25, 0.45, 0.35, 0.3, 0.22, 0.55, 0.35, 0.3, 0.22, 0.75, 0.4, 0.35, 0.22, 1.0, 0.4, 0.35, 0.18, 1.0, 0.4, 0.35, 0.18, 1.5, 0.4, 0.35, 0.18, 1.5, 0.4, 0.35, 0.18]

print(TList)
print(RList)
print(SList)

it = 0
for R in RList:
	for T in TList:
		S = SList[it]
		it += 1
		fname="job-T"+str(T)+"R"+str(R)+"S"+str(S)
		fileName = open(fname,'w')
		fileName.write(jobstring_sbatch(T,R,S))
		fileName.close()
		call(["sbatch", fname])
		call(["rm", fname])

