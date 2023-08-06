# check, if variants of interest locate to low coverage regions

rule inspect_variants_of_interest:
    input:
        bed = os.path.join(DATAFOLDER["masking"], "{sample}", "{sample}.lowcov.bed"),
        vcf_filtered = os.path.join(DATAFOLDER["variant_calling"], "{sample}", "{sample}.filtered.vcf.gz"),
        voi = VAR_VOI
    output:
        voi_exact = os.path.join(DATAFOLDER["masking"], "{sample}", "{sample}.voi_exact.vcf"),
        voi_not_found = os.path.join(DATAFOLDER["masking"], "{sample}", "{sample}.voi_not_found.vcf"),
        voi_low_cov = os.path.join(DATAFOLDER["masking"], "{sample}", "{sample}.voi_low_coverage.vcf"),
        voi_diff = os.path.join(DATAFOLDER["masking"], "{sample}", "{sample}.voi_diff_voi.vcf"),
        voi_diff_sample = os.path.join(DATAFOLDER["masking"], "{sample}", "{sample}.voi_diff_sample.vcf")
    conda:
        "../envs/bcftools.yaml"
    singularity:
        "docker://rkibioinf/bcftools:1.11--19c96f3"
    log:
        os.path.join(DATAFOLDER["logs"], "masking", "{sample}.check_voi.log")
    shell:
        r"""
            bgzip -c {input.voi} > {input.voi}.gz
            bcftools index -f {input.vcf_filtered} 
            bcftools index -f {input.voi}.gz


            bcftools isec -c none -n=2 -w2 -o {output.voi_exact} {input.vcf_filtered} {input.voi}.gz # identical REF and ALT
            bcftools isec -c all -n~01 -w2 -o {output.voi_not_found} {input.vcf_filtered} {input.voi}.gz # voi not found, regardless ALT
            bcftools isec -T {input.bed} -o {output.voi_low_cov} {input.voi}.gz # low coverage vois

            bgzip -c {output.voi_exact} > {output.voi_exact}.gz
            bcftools index -f {output.voi_exact}.gz
            bgzip -c {output.voi_not_found} > {output.voi_not_found}.gz
            bcftools index -f {output.voi_not_found}.gz
            
            bcftools isec -n~100 -w1 -o {output.voi_diff} {input.voi}.gz {output.voi_exact}.gz {output.voi_not_found}.gz # vio with different ALT in voi file

            bgzip -c {output.voi_diff} > {output.voi_diff}.gz
            bcftools index -f {output.voi_diff}.gz
            
            bcftools isec -c all -n=2 -w1 -o {output.voi_diff_sample} {input.vcf_filtered} {output.voi_diff}.gz # voi with different ALT in vcf sample file
        """
