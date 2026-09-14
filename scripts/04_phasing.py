import os, subprocess


reference_genome= '../data/reference_genome.fasta'
variant_results= '../results/02_variant_calling'
deepvariant_results= '../results/03_deepvariant'
alignment_results= '../results/01_alignment'
results= '../results/04_phasing'


def phasing(variant_results, alignment_results, deepvariant_results, reference_genome, results, HiPhase):
    os.makedirs(results, exist_ok=True)
    for x in os.listdir(alignment_results):
        if x.endswith('A.bam') or x.endswith('C.bam'):
            sample_name = x.replace(".bam", "")
            bam_path = os.path.join(alignment_results, x)
            deepvariant_path = os.path.join(deepvariant_results, x)
            variant_path = os.path.join(variant_results, x)
            output_vcf_deepvariant = f"{sample_name.add(Deepvariant)}.phased.vcf.gz" 
            output_vcf_variant = f"{sample_name.add(variant)}.phased.vcf.gz" 

            cmd = (hiphase \
                --bam {bam_path} \
                --vcf {variant_path} \
                --vcf {deepvariant_path} \
                --output-vcf {output_vcf_variant} \
                --output-vcf {output_vcf_deepvariant} \
                --reference {reference_genome} \
                --threads {32})
            subprocess.run(cmd, check=True)


phasing(variant_results, alignment_results, deepvariant_results, reference_genome, results, HiPhase)


#-----------------------------------------Claude---------------------------------------------

import os, subprocess


reference_genome = '../data/reference_genome.fasta'
variant_results = '../results/02_variant_calling'
deepvariant_results = '../results/03_deepvariant'
alignment_results = '../results/01_alignment'
results = '../results/04_phasing'
HiPhase = 'hiphase'   # ruta al ejecutable, o solo "hiphase" si está en el PATH
THREADS = 32


def phasing(variant_results, alignment_results, deepvariant_results,
            reference_genome, results, HiPhase, THREADS):

    os.makedirs(results, exist_ok=True)

    for x in sorted(os.listdir(alignment_results)):

        if x.endswith('A.bam') or x.endswith('C.bam'):

            sample_name = x.replace(".bam", "")

            bam_path = os.path.join(alignment_results, x)

            # Los VCFs se buscan por nombre de muestra + extensión, no por el nombre del BAM
            variant_path = os.path.join(variant_results, f"{sample_name}.vcf.gz")
            deepvariant_path = os.path.join(deepvariant_results, f"{sample_name}.vcf.gz")

            # Rutas de salida dentro del directorio de resultados de phasing
            output_vcf_variant = os.path.join(
                results, f"{sample_name}_variant.phased.vcf.gz"
            )
            output_vcf_deepvariant = os.path.join(
                results, f"{sample_name}_deepvariant.phased.vcf.gz"
            )

            print(f"\nRunning HiPhase for: {sample_name}")
            print(f"BAM: {bam_path}")

            cmd = [
                HiPhase,

                "--bam", bam_path,

                # cada --vcf debe corresponder en orden con su --output-vcf
                "--vcf", variant_path,
                "--vcf", deepvariant_path,

                "--output-vcf", output_vcf_variant,
                "--output-vcf", output_vcf_deepvariant,

                "--reference", reference_genome,

                "--threads", str(THREADS),
            ]

            print(" ".join(cmd))

            subprocess.run(cmd, check=True)


phasing(
    variant_results,
    alignment_results,
    deepvariant_results,
    reference_genome,
    results,
    HiPhase,
    THREADS,
)
