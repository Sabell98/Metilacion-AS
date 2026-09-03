import os, subprocess


path_bamfiles='/home/rare/data/genomes/bamfiles'
reference_genome='/home/rare/arlen/reference/chm13v22.fasta'
results='../results/01_alignment'
pbmm2='/home/rare/programs/smrtlink/smrtlink/smrtcmds/bin/pbmm2'


def alignment (path_bamfiles, reference_genome, results, pbmm2):
    os.makedirs(results, exist_ok=True)
    for x in os.listdir(path_bamfiles):
        if x.endswith('A.bam') or x.endswith('C.bam'):
            file=os.path.join(path_bamfiles,x)     
            cmd=[f'{pbmm2}', 'align',
                 f'{reference_genome}', f'{file}',
                 f'{results}/{x}', '--preset',
                 'HIFI', '--sort', 
                 '--log-level', 'INFO',
                 '-j', '32',
                 '-J', '32']
            subprocess.run(cmd,  check=True)
            #print(cmd)

alignment (path_bamfiles, reference_genome, results, pbmm2)            