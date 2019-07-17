import sys, os, glob

class Trimmer:
	"""
	Trim raw reads and/or remove adapters
	"""

	def __init__(self, final_results_directory, isolate_name, fastq, trimmomatic_jar, threads, trimmomatic_adapters, trimmomatic_phred, trimmomatic_illuminaclip, trimmomatic_slidingwindow, trimmomatic_leading, trimmomatic_trailing, trimmomatic_minlen):
		self.final_results_directory = final_results_directory
		self.isolate_name = isolate_name
		self.fastq = fastq
		self.trimmomatic_jar = trimmomatic_jar
		self.threads = threads
		self.trimmomatic_adapters = trimmomatic_adapters
		self.trimmomatic_phred = trimmomatic_phred
		self.trimmomatic_illuminaclip = trimmomatic_illuminaclip
		self.trimmomatic_slidingwindow = trimmomatic_slidingwindow
		self.trimmomatic_leading = trimmomatic_leading
		self.trimmomatic_trailing = trimmomatic_trailing
		self.trimmomatic_minlen = trimmomatic_minlen

	
	def trimmomatic_pe(self, final_results_directory, isolate_name, fastq, trimmomatic_jar, threads, trimmomatic_adapters, trimmomatic_phred, trimmomatic_illuminaclip, trimmomatic_slidingwindow, trimmomatic_leading, trimmomatic_trailing, trimmomatic_minlen):

		if not os.path.isdir(final_results_directory + "trimmomatic_trimmedP"):
			os.mkdir(final_results_directory + "trimmomatic_trimmedP")

		if not os.path.isdir(final_results_directory + "trimmomatic_trimmedS"):
			os.mkdir(final_results_directory + "trimmomatic_trimmedS")

		if not os.path.isdir(final_results_directory + "trimmomatic_logs"):
			os.mkdir(final_results_directory + "trimmomatic_logs")

		trimmedP1 = final_results_directory + "trimmomatic_trimmedP/" + isolate_name + "_trimmedP_1.fastq.gz"
		trimmedP2 = final_results_directory + "trimmomatic_trimmedP/" + isolate_name + "_trimmedP_2.fastq.gz"
		trimmedS1 = final_results_directory + "trimmomatic_trimmedS/" + isolate_name + "_trimmedS_1.fastq.gz"
		trimmedS2 = final_results_directory + "trimmomatic_trimmedS/" + isolate_name + "_trimmedS_2.fastq.gz"
		logfile = final_results_directory + "trimmomatic_logs/" + isolate_name + "_trimmomatic.log"

		cmd = "java -jar {0} PE -threads {1} -{2} -trimlog {3} {4} {5} {6} {7} {8} {9} ILLUMINACLIP:{10}:{11} LEADING:{12} TRAILING:{13} SLIDINGWINDOW:{14} MINLEN:{15}".format(trimmomatic_jar, threads, trimmomatic_phred, logfile, fastq[0], fastq[1], trimmedP1, trimmedS1, trimmedP2, trimmedS2, trimmomatic_adapters, trimmomatic_illuminaclip, trimmomatic_leading, trimmomatic_trailing, trimmomatic_slidingwindow, trimmomatic_minlen)

		os.system(cmd) 

		return([trimmedP1, trimmedP2])

	def trimmomatic_se(self, final_results_directory, isolate_name, fastq, trimmomatic_jar, threads, trimmomatic_adapters, trimmomatic_phred, trimmomatic_illuminaclip, trimmomatic_slidingwindow, trimmomatic_leading, trimmomatic_trailing, trimmomatic_minlen):

		if not os.path.isdir(final_results_directory + "trimmomatic_trimmed"):
			os.mkdir(final_results_directory + "trimmomatic_trimmed")

		if not os.path.isdir(final_results_directory + "trimmomatic_logs"):
			os.mkdir(final_results_directory + "trimmomatic_logs")

		trimmedP = final_results_directory + "trimmomatic_trimmed/" + isolate_name + "_trimmed.fastq.gz"
		logfile = final_results_directory + "trimmomatic_logs/" + isolate_name + "_trimmomatic.log"

		cmd = "java -jar {0} SE -threads {1} -{2} -trimlog {3} {4} {5} ILLUMINACLIP:{6}:{7} LEADING:{8} TRAILING:{9} SLIDINGWINDOW:{10} MINLEN:{11}".format(trimmomatic_jar, threads, trimmomatic_phred, logfile, fastq[0], trimmedP, trimmomatic_adapters, trimmomatic_illuminaclip, trimmomatic_leading, trimmomatic_trailing, trimmomatic_slidingwindow, trimmomatic_minlen)

		os.system(cmd) 

		return([trimmedP])
