rule rkiQC:
    input: 
        fasta = os.path.join(IUPAC_CNS_FOLDER, "{sample}.iupac_consensus.fasta"),
        coverage = os.path.join(DATAFOLDER["mapping_stats"], "{sample}", "{sample}.coverage.tsv")
    output: 
        qc = temp(os.path.join(DATAFOLDER["qc"], "{sample}", "{sample}.qc.tsv"))
    params:
        cov = CNS_MIN_COV
    conda:
        "../envs/bcftools.yaml"
    singularity:
        "docker://rkibioinf/bcftools:1.11--19c96f3"
    shell:
        r"""
        echo 'sample,#n,#iupac,#lowcov' > {output.qc}
        N=$(tail -n +2 {input.fasta} | tr -cd "N" | wc -c)
        IUPAC=$(tail -n +2 {input.fasta} | tr -cd "RYSWKMBDHVN" | wc -c)
        COVTH=$(awk -F "\t" '{{COV=$3; if (COV < {params.cov}) {{ print COV }} }}' {input.coverage} | wc -l)
        echo {wildcards.sample},$N,$IUPAC,$COVTH >> {output.qc}
        """
