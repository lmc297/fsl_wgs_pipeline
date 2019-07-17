import sys, os, glob

class Assembler:
	"""
	Assemble genomes from reads
	"""

	def __init__(self, final_results_directory, isolate_name, spades_path, fastq, threads, spades_m):
		self.final_results_directory = final_results_directory
		self.isolate_name = isolate_name
		self.spades_path = spades_path
		self.fastq = fastq
		self.threads = threads
		self.spades_m = spades_m

	def spades_pe(self, final_results_directory, isolate_name, spades_path, fastq, threads, spades_m):

		if not os.path.isdir(final_results_directory + "contigs"):
			os.mkdir(final_results_directory + "contigs")

		if not os.path.isdir(final_results_directory + "spades_output"):
			os.mkdir(final_results_directory + "spades_output")

		cmd = "{0} --careful -1 {1} -2 {2} -o {3} -t {4} -m {5}".format(spades_path, fastq[0], fastq[1], final_results_directory + "spades_output/" + isolate_name, threads, spades_m)

		os.system(cmd)

		os.system("cp " + final_results_directory + "spades_output/" + isolate_name + "/contigs.fasta " + final_results_directory + "contigs/" + isolate_name + ".fasta") 

		return(final_results_directory + "contigs/" + isolate_name + ".fasta")

		

	def spades_se(self, final_results_directory, isolate_name, spades_path, fastq, threads, spades_m):

		if not os.path.isdir(final_results_directory + "contigs"):
			os.mkdir(final_results_directory + "contigs")

		if not os.path.isdir(final_results_directory + "spades_output"):
			os.mkdir(final_results_directory + "spades_output")

		cmd = "{0} --careful -s {1} -o {2} -t {3} -m {4}".format(spades_path, fastq[0], final_results_directory + "spades_output/" + isolate_name, threads, spades_m)

		os.system(cmd)

		os.system("cp " + final_results_directory + "spades_output/" + isolate_name + "/contigs.fasta " + final_results_directory + "contigs/" + isolate_name + ".fasta")

		return(final_results_directory + "contigs/" + isolate_name + ".fasta") 
