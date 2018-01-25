with open("ribo_only_depth_of_coverage_samtools.csv") as f:
	covered_zone = False
	start = ""
	stop = ""
	for line in f:
		scaf , pos , depth = line.split("\t")
		pos_int = int(pos)
		depth_int = int(depth)
		if depth_int == 0 and covered_zone:
			print scaf,"\t",start,"\t",stop
			covered_zone = False
		if depth_int >= 1:
			if covered_zone:
				stop = pos
			if not covered_zone:
				start = pos
				covered_zone = True
