import os, subprocess


bam_path = '../results/01_alignment'
results= '../results/05_callmethylation'
threads = 32


def callmethylation(bam_path, pbcpgtools):
    os.makedirs(results, exist_ok=True)
    for x in os.listdir(bam_path):
        if x.endswith('A.bam') or x.endswith('C.bam'):
            sample_name = x.replace(".bam", "")
            bam_file = os.path.join(bam_path, x)
            output_prefix = os.path.join(results, sample_name)
            cmd = [
                pbcpgtools,
                'aligned_bam_to_cpg_scores',
                '--bam', bam_file,
                '--output-prefix', output_prefix,
                '--threads', {32}
            ]
            subprocess.run(cmd, check=True)

cpg_scores(
    alignment_results,
    results,
    THREADS,
)

#--------------------------------Claude---------------------------------------------

import os, subprocess
 
 
alignment_results = '../results/01_alignment'
results = '../results/05_cpg_scores'
THREADS = 8
 
 
def cpg_scores(alignment_results, results, THREADS):
 
    os.makedirs(results, exist_ok=True)
 
    for x in sorted(os.listdir(alignment_results)):
 
        if x.endswith('A.bam') or x.endswith('C.bam'):
 
            sample_name = x.replace(".bam", "")
 
            bam_path = os.path.join(alignment_results, x)
 
            output_prefix = os.path.join(results, sample_name)
 
            print(f"\nRunning aligned_bam_to_cpg_scores for: {sample_name}")
            print(f"BAM: {bam_path}")
 
            cmd = [
                "aligned_bam_to_cpg_scores",
 
                "--bam", bam_path,
 
                "--output-prefix", output_prefix,
 
                "--threads", str(THREADS),
            ]
 
            print(" ".join(cmd))
 
            subprocess.run(cmd, check=True)
 
 
cpg_scores(
    alignment_results,
    results,
    THREADS,
)
 
