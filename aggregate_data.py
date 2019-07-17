import sys, glob, os, gzip

class FinalSummary:
	"""
	Create a final output file listing stats for all isolates
	"""

	def __init__(self, final_results_directory, isolate_name, fastq, assembler, quast, coverage):

		self.final_results_directory = final_results_directory
		self.isolate_name = isolate_name
		self.fastq = fastq
		self.assembler = assembler
		self.quast = quast
		self.coverage = coverage

	def aggregate_data(self, final_results_directory, isolate_name, fastq, assembler, quast, coverage):

		if not os.path.exists(final_results_directory + "fsl_wgs_pipeline_final_summary.txt"):
			outfile = open(final_results_directory + "fsl_wgs_pipeline_final_summary.txt", "a")
			print >> outfile, "\t".join(["isolate", "reads_1", "reads_2", "reads_1_filesize", "reads_2_filesize", "contigs", "contigs_filesize", "total_genome_length", "n_contigs", "N50", "L50", "largest_contig_length", "GC_percent", "Ns_per_100Kbp", "average_coverage"])
			outfile.close()

		final = []
		final.append(isolate_name)
		final.extend(fastq)
		if len(fastq) == 1:
			final.append("NA")
		final.append(os.path.getsize(fastq[0]))
		if len(fastq) == 2:
			final.append(os.path.getsize(str(fastq[1])))
		elif len(fastq) == 1:
			final.append("NA")
		if assembler != "False":
			contigs = final_results_directory + "contigs/" + isolate_name + ".fasta"
			final.append(contigs)
			final.append(os.path.getsize(str(contigs)))
			if quast == "True":
				infile = open(final_results_directory + "quast_results/" + isolate_name + "_quast_out/transposed_report.tsv", "r")
				for line in infile:
					if "# contigs (>= 0 bp)" not in line:
						splits = line.split("\t")
						final.append(splits[-7].strip())
						final.append(splits[-9].strip())
						final.append(splits[-5].strip())
						final.append(splits[-3].strip())
						final.append(splits[-8].strip())
						final.append(splits[-6].strip())
						final.append(splits[-1].strip())
				infile.close()
			else:
				final + ["NA"] * 7
		else:
			final + ["NA"] * 9

		if coverage == "True":

			infile = open(final_results_directory + "average_coverage/" + isolate_name + "_average_coverage.txt", "r")
			for line in infile:
				if len(line.strip()) > 0:
					final.append(line.strip())
			infile.close()
		else:
			final.append("NA")

		outfile = open(final_results_directory + "fsl_wgs_pipeline_final_summary.txt", "a")
		print >> outfile, "\t".join([str(fin) for fin in final])
		outfile.close() 	
