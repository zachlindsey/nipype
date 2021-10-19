# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import MRConvert


def test_MRConvert_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        axes=dict(argstr="-axes %s", sep=","),
        bval_scale=dict(argstr="-bvalue_scaling %s"),
        coord=dict(argstr="-coord %s", sep=" "),
        environ=dict(nohash=True, usedefault=True),
        grad_file=dict(argstr="-grad %s", extensions=None, xor=["grad_fsl"]),
        grad_fsl=dict(argstr="-fslgrad %s %s", xor=["grad_file"]),
        in_bval=dict(extensions=None),
        in_bvec=dict(argstr="-fslgrad %s %s", extensions=None),
        in_file=dict(argstr="%s", extensions=None, mandatory=True, position=-2),
        nthreads=dict(argstr="-nthreads %d", nohash=True),
        out_file=dict(
            argstr="%s", extensions=None, mandatory=True, position=-1, usedefault=True
        ),
        scaling=dict(argstr="-scaling %s", sep=","),
        vox=dict(argstr="-vox %s", sep=","),
    )
    inputs = MRConvert.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_MRConvert_outputs():
    output_map = dict(out_file=dict(extensions=None))
    outputs = MRConvert.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
