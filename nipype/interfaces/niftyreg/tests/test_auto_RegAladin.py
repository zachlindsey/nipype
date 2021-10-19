# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..reg import RegAladin


def test_RegAladin_inputs():
    input_map = dict(
        aff_direct_flag=dict(argstr="-affDirect"),
        aff_file=dict(
            argstr="-aff %s",
            extensions=None,
            name_source=["flo_file"],
            name_template="%s_aff.txt",
        ),
        args=dict(argstr="%s"),
        cog_flag=dict(argstr="-cog"),
        environ=dict(nohash=True, usedefault=True),
        flo_file=dict(argstr="-flo %s", extensions=None, mandatory=True),
        flo_low_val=dict(argstr="-floLowThr %f"),
        flo_up_val=dict(argstr="-floUpThr %f"),
        fmask_file=dict(argstr="-fmask %s", extensions=None),
        gpuid_val=dict(argstr="-gpuid %i"),
        i_val=dict(argstr="-pi %d"),
        in_aff_file=dict(argstr="-inaff %s", extensions=None),
        ln_val=dict(argstr="-ln %d"),
        lp_val=dict(argstr="-lp %d"),
        maxit_val=dict(argstr="-maxit %d"),
        nac_flag=dict(argstr="-nac"),
        nosym_flag=dict(argstr="-noSym"),
        omp_core_val=dict(argstr="-omp %i", usedefault=True),
        platform_val=dict(argstr="-platf %i"),
        ref_file=dict(argstr="-ref %s", extensions=None, mandatory=True),
        ref_low_val=dict(argstr="-refLowThr %f"),
        ref_up_val=dict(argstr="-refUpThr %f"),
        res_file=dict(
            argstr="-res %s",
            extensions=None,
            name_source=["flo_file"],
            name_template="%s_res.nii.gz",
        ),
        rig_only_flag=dict(argstr="-rigOnly"),
        rmask_file=dict(argstr="-rmask %s", extensions=None),
        smoo_f_val=dict(argstr="-smooF %f"),
        smoo_r_val=dict(argstr="-smooR %f"),
        v_val=dict(argstr="-pv %d"),
        verbosity_off_flag=dict(argstr="-voff"),
    )
    inputs = RegAladin.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_RegAladin_outputs():
    output_map = dict(
        aff_file=dict(extensions=None),
        avg_output=dict(),
        res_file=dict(extensions=None),
    )
    outputs = RegAladin.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
