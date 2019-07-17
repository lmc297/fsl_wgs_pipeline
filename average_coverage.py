import sys, os, glob

class AverageCoverage:
	"""
	Calculate average coverage by mapping reads back to assemblies
	"""

	def __init__(self, final_results_directory, isolate_name, bwa_path, samtools_path, threads, fastq, contigs):

		self.final_results_directory = final_results_directory
		self.isolate_name = isolate_name
		self.bwa_path = bwa_path
		self.samtools_path = samtools_path
		self.threads = threads
		self.fastq = fastq
		self.contigs = contigs

	def bwa_coverage(self, final_results_directory, isolate_name, bwa_path, samtools_path, threads, fastq, contigs):

		if not os.path.isdir(final_results_directory + "average_coverage"):
			os.mkdir(final_results_directory + "average_coverage")

		cmd_index = "{0} index {1}".format(bwa_path, contigs)
		os.system(cmd_index)

		cmd_mem = "{0} mem -t {1} {2} {3} > {4}.sam".format(bwa_path, threads, contigs, " ".join(fastq), final_results_directory + "average_coverage/" + isolate_name)
		os.system(cmd_mem)

		cmd_view = "{0} view -Sb {1} > {2}.bam".format(samtools_path, final_results_directory + "average_coverage/" + isolate_name + ".sam", final_results_directory + "average_coverage/" + isolate_name)
		os.system(cmd_view)

		os.remove(final_results_directory + "average_coverage/" + isolate_name + ".sam")

		cmd_sort = "{0} sort {1} -o {2}".format(samtools_path, final_results_directory + "average_coverage/" + isolate_name + ".bam", final_results_directory + "average_coverage/" + isolate_name + "_sorted.bam")
		os.system(cmd_sort)

		os.remove(final_results_directory + "average_coverage/" + isolate_name + ".bam")
		
		cmd_samindex = "{0} index {1}".format(samtools_path, final_results_directory + "average_coverage/" + isolate_name + "_sorted.bam")
		os.system(cmd_samindex)

		os.system(samtools_path + " depth " + final_results_directory + "average_coverage/" + isolate_name + "_sorted.bam | awk '{sum+=$3} END { print sum/NR}' >> " + final_results_directory + "average_coverage/" + isolate_name + "_average_coverage.txt")

		os.system("rm " + final_results_directory + "average_coverage/" + isolate_name + "_sorted.bam*")
		os.system("rm " + final_results_directory + "contigs/" + isolate_name + ".fasta.*")
