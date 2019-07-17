import sys, os, glob

class SequenceData:
	"""
	Load sequence data in various formats
	"""

	def __init__(self, infile, isolate):
		self.infile = infile
		self.isolate = isolate

	def load_fastq(self, infile, isolate):
		seq = []
		if len(isolate) == 3:
			forward, reverse, prefix = isolate[0], isolate[1], isolate[2]
			seq.extend([forward, reverse])
			
		elif len(isolate) == 2:
			se, prefix = isolate[0], isolate[1]
			seq.extend([se.strip()])
		else:
			print "There is a line in your input file, " + infile + ", that is not formatted correctly."
			print "Lines corresponding to paired-end reads should be formatted as 'forward_reads.fastq.gz <tab> reverse_reads.fastq.gz <tab> basename'"
			print "Lines corresponding to single-end reads should be formatted as 'single_reads.fastq.gz <tab> basename.'"
			print "The line causing the error is:"
			print "\t".join(isolate)
			sys.exit()
		return(seq, prefix)
				
