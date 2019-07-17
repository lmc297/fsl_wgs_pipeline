import sys, os, glob

class Quast:
	"""
	Assess the quality of an assembled genome using quast
	"""

	def __init__(self, final_results_directory, isolate_name, quast_path, quast_min_contig, threads, fastq, contigs):
		self.final_results_directory = final_results_directory
		self.isolate_name = isolate_name
		self.quast_path = quast_path
		self.quast_min_contig = quast_min_contig
		self.threads = threads
		self.fastq = fastq
		self.contigs = contigs

	def run_quast(self, final_results_directory, isolate_name, quast_path, quast_min_contig, threads, fastq, contigs):

		cmd = "{0} --min-contig {1} --threads {2} -o {3} {4}".format(quast_path, quast_min_contig, threads, final_results_directory + "quast_results/" + isolate_name + "_quast_out", contigs)

		os.system(cmd)

		return(final_results_directory + "quast_results/" + isolate_name + "_quast_out")
