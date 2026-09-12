import os
import subprocess


INPUT_DIR = "/mnt/diskrare/ESTUDIANTES/Isabella/Metilacion-AS/results/01_alignment"

OUTPUT_DIR = "/mnt/diskrare/ESTUDIANTES/Isabella/Metilacion-AS/results/02_SNVs_deepvariant"

REF = "/home/rare/arlen/reference/chm13v22.fasta"

THREADS = 32

BIN_VERSION = "1.5.0"


def deepvariant(INPUT_DIR, OUTPUT_DIR, REF, THREADS, BIN_VERSION):

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Directory containing the reference
    REF_DIR = os.path.dirname(REF)

    # Reference filename only
    REF_NAME = os.path.basename(REF)

    for x in sorted(os.listdir(INPUT_DIR)):

        if x.endswith("A.bam") or x.endswith("C.bam"):

            sample = x.replace(".bam", "")

            bam_path = os.path.join(INPUT_DIR, x)

            output_vcf = f"{sample}.vcf.gz"
            output_gvcf = f"{sample}.g.vcf.gz"

            intermediate_directory = os.path.join(
                OUTPUT_DIR,
                f"{sample}_intermediate_results"
            )

            os.makedirs(intermediate_directory, exist_ok=True)

            print(f"\nRunning DeepVariant for: {sample}")
            print(f"BAM: {bam_path}")

            cmd = [
                "docker", "run",
                "--rm",

                # BAM directory
                "-v", f"{INPUT_DIR}:/input:ro",

                # Reference directory
                "-v", f"{REF_DIR}:/reference:ro",

                # Output directory
                "-v", f"{OUTPUT_DIR}:/output",

                f"google/deepvariant:{BIN_VERSION}",

                "/opt/deepvariant/bin/run_deepvariant",

                "--model_type", "PACBIO",

                "--ref", f"/reference/{REF_NAME}",

                "--reads", f"/input/{x}",

                "--output_vcf", f"/output/{output_vcf}",

                "--output_gvcf", f"/output/{output_gvcf}",

                "--num_shards", str(THREADS),

                "--intermediate_results_dir",
                f"/output/{sample}_intermediate_results",
            ]

            print(" ".join(cmd))

            subprocess.run(cmd, check=True)


deepvariant(
    INPUT_DIR,
    OUTPUT_DIR,
    REF,
    THREADS,
    BIN_VERSION
)