import sys, os, glob

class MultiQC:
	"""
	Use multiqc to aggregate qc results for reads and/or assemblies
	"""

	def __init__(self, multiqc_path, directory):

		self.multiqc_path = multiqc_path
		self.directory = directory

	def run_multiqc(self, multiqc_path, directory):

		os.system(multiqc_path + " " + directory + " -o " + directory + "multiqc_results")

	def run_multiqc_ignore(self, multiqc_path, directory):

		os.system(multiqc_path + " --ignore " + directory +  "fastqc_raw/* -o " + directory + "multiqc_results " + directory)
