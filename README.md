# fsl_wgs_pipeline
Whole-genome sequencing quality control and assembly pipeline

## Citation

If you found the fsl_wgs_pipeline, its source code, and/or any of its associated databases useful, please cite:

Carroll, Laura M. 2019. fsl_wgs_pipeline: Whole-genome sequencing quality control and assembly. Version 1.0.0. https://github.com/lmc297/fsl_wgs_pipeline.

## Usage and Options
```
usage: fsl_wgs_pipeline -i </path/to/list/of/isolate/file/paths.txt> -o </path/to/output/directory/> [-other options]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Path to tab-separated list of isolate file paths and
                        names, one isolate per line; paired-end reads should
                        have the path to forward reads, path to reverse reads,
                        and the desired isolate name, each separated by a tab,
                        while single-end reads should have the path to the
                        reads and the desired isolate name, separated by a tab
  -o OUTPUT, --output OUTPUT
                        Path to desired output directory
  --threads [THREADS]   Optional argument; integer; number of threads; default
                        = 1
  --fastqc_path [FASTQC_PATH]
                        Optional argument for use with --trimmed_fastqc True;
                        fastqc, unless path to fastqc is supplied; path to
                        fastqc; default = fastqc (fastqc is in your path)
  --multiqc [MULTIQC]   Optional argument; True or False; run multiqc on reads
                        and/or assemblies; default = True
  --multiqc_path [MULTIQC_PATH]
                        Optional argument; multiqc or path to multiqc; path to
                        multiqc; default = multiqc (multiqc is in the user's
                        path
  --trimmer [TRIMMER]   Optional argument; trimmomatic or False; trim reads
                        using trimmomatic or skip read trimming (--trimmer
                        False); default = trimmomatic
  --trimmomatic_jar [TRIMMOMATIC_JAR]
                        Argument for use with --trimmer trimmomatic;
                        trimmomatic-0.39.jar, unless path to trimmomatic jar
                        file is supplied; path to trimmomatic jar file (named
                        trimmomatic-version.jar); default =
                        trimmomatic-0.39.jar (jar for trimmomatic version 0.39
                        is in your path)
  --trimmomatic_adapters [TRIMMOMATIC_ADAPTERS]
                        Argument for use with --trimmer trimmomatic; False,
                        unless path to trimmomatic adapter sequences is
                        supplied; path to trimmomatic adapter sequences;
                        default = False (no path supplied)
  --trimmomatic_phred [TRIMMOMATIC_PHRED]
                        Optional argument for use with --trimmer trimmomatic;
                        phred33 or phred64; specify phred quality encoding of
                        fastq files to be trimmed (note that this should not
                        be changed unless working with very, very old Illumina
                        data); default = phred33
  --trimmomatic_illuminaclip [TRIMMOMATIC_ILLUMINACLIP]
                        Optional argument for use with --trimmer trimmomatic;
                        integer:integer:integer; ILLUMINACLIP seed mismatches
                        (specifies the maximum mismatch count which will still
                        allow a full match to be performed), palindrome clip
                        threshold (specifies how accurate the match between
                        the two 'adapter ligated' reads must be for PE
                        palindrome read alignment), and simple clip threshold
                        (specifies how accurate the match between any adapter
                        etc. sequence must be against a read), each separated
                        by a colon (<seed mismatches>:<palindrome clip
                        threshold>:<simple clip threshold>); default = 2:30:10
  --trimmomatic_leading [TRIMMOMATIC_LEADING]
                        Optional argument for use with --trimmer trimmomatic;
                        integer; argument to pass to trimmomatic's LEADING
                        argument (cut bases off the start of a read, if below
                        a threshold quality); default = 3
  --trimmomatic_trailing [TRIMMOMATIC_TRAILING]
                        Optional argument for use with --trimmer trimmomatic;
                        integer; argument to pass to trimmomatic's TRAILING
                        argument (cut bases off the end of a read, if below a
                        threshold quality); default = 3
  --trimmomatic_slidingwindow [TRIMMOMATIC_SLIDINGWINDOW]
                        Optional argument for use with --trimmer trimmomatic;
                        integer:integer; SLIDINGWINDOW window size (specifies
                        the number of bases to average across) and required
                        quality (specifies the average quality required),
                        separated by a colon (<window size>:<required
                        quality>); default = 4:15
  --trimmomatic_minlen [TRIMMOMATIC_MINLEN]
                        Optional argument for use with --trimmer trimmomatic;
                        integer; argument to pass to trimmomatic's MINLEN
                        argument (drop the read if it is below a specified
                        length); default = 36
  --trimmed_fastqc [TRIMMED_FASTQC]
                        Optional argument for use with --trimmer trimmomatic;
                        True or False; run fastqc on trimmed Illumina reads;
                        default = True
  --assembler [ASSEMBLER]
                        Optional argument; spades or False; assemble genome
                        with spades or skip assembly (--assembler False);
                        default = spades
  --spades_path [SPADES_PATH]
                        Argument for use with --assembler spades; spades.py,
                        unless path to spades.py is supplied; path to
                        spades.py; default = spades.py (spades.py is in the
                        user's path)
  --spades_m [SPADES_M]
                        Optional argument for use with --assembler spades;
                        integer; memory limit for spades in Gb (spades
                        terminates if it reaches this limit); default = 20
  --min_contig_length [MIN_CONTIG_LENGTH]
                        Optional argument for use with --assembler spades;
                        integer; remove contigs less than specified length (in
                        bp) from each assembly (note that this only applies to
                        'final' assemblies copied into the 'contigs' directory
                        in the 'fsl_wgs_pipeline_final_results' directory; all
                        original, unfiltered assemblies are unchanged and
                        remain in the isolate's respective directory in the
                        'spades_output' directory in the
                        'fsl_wgs_pipeline_final_results' directory; default =
                        200
  --quast [QUAST]       Optional argument for use with --assembler spades;
                        True or False; run quast on assembled genomes; default
                        = True
  --quast_path [QUAST_PATH]
                        Argument for use with --quast True; quast.py, unless
                        path to quast.py is supplied; path to quast.py;
                        default = quast.py (quast.py is in the user's path)
  --quast_min_contig [QUAST_MIN_CONTIG]
                        Optional argument for use with --quast True; integer;
                        --min-contig threshold for quast contig length to
                        consider (in bp; shorter contigs won't be taken into
                        account, except for specific metrics); default = 1
                        (quast considers all contigs)
  --coverage [COVERAGE]
                        Optional argument for use with --assembler spades;
                        True or False; calculate coverage of assembly by
                        mapping reads back to assembly using bwa/samtools;
                        default = True
  --bwa_path [BWA_PATH]
                        Argument for use with --coverage True; bwa, unless
                        path to bwa is supplied; path to bwa; default = bwa
                        (bwa is in the user's path)
  --samtools_path [SAMTOOLS_PATH]
                        Argument for use with --coverage True; samtools,
                        unless path to samtools is supplied; path to samtools;
                        default = samtools (samtools is in the user's path)
  --version             Print version
```
