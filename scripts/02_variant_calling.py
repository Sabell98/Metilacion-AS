import os, subprocess

path_bamfiles_aligned = '../results/01_alignment'
reference_genome = '/home/rare/arlen/reference/chm13v22.fasta'
results = '../results/02_variant_calling'


def variant_calling(path_bamfiles_aligned, reference_genome, results):
    os.makedirs(results, exist_ok=True)
    for x in os.listdir(path_bamfiles_aligned):
        if x.endswith('.bam'):
            file = os.path.join(path_bamfiles_aligned, x)
            svsig = os.path.join(results, x.replace('.bam', '.svsig.gz'))
            vcf = os.path.join(results, x.replace('.bam', '.vcf'))

            # Paso 1: generar señal de variantes estructurales
            cmd_discover = ['pbsv', 'discover', f'{file}', f'{svsig}']
            subprocess.run(cmd_discover, check=True)

            # Paso 2: llamado de variantes estructurales
            cmd_call = ['pbsv', 'call', f'{reference_genome}', f'{svsig}', f'{vcf}']
            subprocess.run(cmd_call, check=True)

variant_calling(path_bamfiles_aligned, reference_genome, results)