#!/bin/bash
python parsing.py gpu-bench/gpu-l2-cache/amdmi200/workloads/omni-data/amd-l2-cache-0 omnidata/amd_l2_cache_0_k0

for k in {0..5}; do
	for ((b_c = 32; b_c <= 1024; b_c += 32)); do

    	python parsing.py ./amd_l2_cache_${b_c}_k${k} ./parsed/amd_stream_${b_c}_k${k}
    done
done
