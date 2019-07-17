import sys, os, glob

class FastQC:
	"""
	Use fastqc to assess read quality
	"""

	def __init__(self, fastqc_path, fastq, final_results_directory, threads, suffix):

		self.fastqc_path = fastqc_path
		self.fastq = fastq
		self.final_results_directory = final_results_directory
		self.threads = threads
		self.suffix = suffix

	def run_fastqc(self, fastqc_path, fastq, final_results_directory, threads, suffix):

		if not os.path.isdir(final_results_directory + "fastqc_" + suffix):
			os.mkdir(final_results_directory + "fastqc_" + suffix)
		for r in fastq:
			os.system(fastqc_path + " --threads " + threads + " --outdir " + final_results_directory + "fastqc_" + suffix + " " + r)
	
