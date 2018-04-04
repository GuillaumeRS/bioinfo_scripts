# Script filtering a vcf (with no header) based on major allelic depth fequency of individual samples (AD field)
# Given a threshold of minimum major allelic depth frequency, and positions of studied
# samples (0 = first sample), it will print only variants with major allelic frequency greater than the 
# threshold for all the studied samples.
# arguments in this order : /path_to_vcf.vcf min_major_allelic_ratio_threshold sample_1_pos sample_2_pos sample_N_pos...
# ex : python ./filter_allelic_frequency.py ./test.vcf 0.6 1 3

import sys

file_path = sys.argv[1]
AF_threshold = sys.argv[2]
list_samples = sys.argv[3:]

with open(file_path) as f:
	for line in f:
	#for all line of a given VCF
		if line[:1]!='#':
		#except header
			split_line = line.split("\t")
			list_major_AF =[];
			for i in split_line[9:]:
			#for all samples of a line, computes the major allele frequency and stores 
			#it in the list "list_major_AF", gives 1.0 if missing genotype, 0 if no coverage
				split_field = i.split(":")
				if split_field[0] != '.':
					list_AD = split_field[1].split(",")
					list_AD = map(int, list_AD)
					if (max(list_AD)==0):
						major_AF = 0
					else:
						major_AF =  float(max(list_AD))/float(sum(list_AD))
				else:
					major_AF = 1.0
				list_major_AF.append(major_AF)
			all_freq_greater_than_threshold = True
			for j in list_samples:
			 	if list_major_AF[int(j)] < float(AF_threshold):
			 		all_freq_greater_than_threshold = False
			if (all_freq_greater_than_threshold):
				print line,

