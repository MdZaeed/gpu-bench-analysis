#!/bin/bash

# Loop from 1 to 32

for k in {0..5}; do
	for ((b_c = 32; b_c <= 1024; b_c += 32)); do
	    output_dir="amd_stream_$b_c$"
	    echo "Running omniperf with b_c = $b_c, output directory: $output_dir"
	    ~/omniperf/1.0.10/bin/omniperf analyze -p /home/cup7/rawDatasets/gpu-stream/amd/amd_stream_${b_c}/mi200/ -k ${k} -o ./amd_l2_cache_${b_c}_k${k}
	done
done

