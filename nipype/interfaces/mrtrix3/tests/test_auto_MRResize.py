# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import MRResize


def test_MRResize_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        bval_scale=dict(argstr="-bvalue_scaling %s"),
        environ=dict(nohash=True, usedefault=True),
        grad_file=dict(argstr="-grad %s", extensions=None, xor=["grad_fsl"]),
        grad_fsl=dict(argstr="-fslgrad %s %s", xor=["grad_file"]),
        image_size=dict(
            argstr="-size %d,%d,%d", mandatory=True, xor=["voxel_size", "scale_factor"]
        ),
        in_bval=dict(extensions=None),
        in_bvec=dict(argstr="-fslgrad %s %s", extensions=None),
        in_file=dict(argstr="%s", extensions=None, mandatory=True, position=-2),
        interpolation=dict(argstr="-interp %s", usedefault=True),
        nthreads=dict(argstr="-nthreads %d", nohash=True),
        out_file=dict(
            argstr="%s",
            extensions=None,
            keep_extension=True,
            name_source=["in_file"],
            name_template="%s_resized",
            position=-1,
        ),
        scale_factor=dict(
            argstr="-scale %g,%g,%g", mandatory=True, xor=["image_size", "voxel_size"]
        ),
        voxel_size=dict(
            argstr="-voxel %g,%g,%g", mandatory=True, xor=["image_size", "scale_factor"]
        ),
    )
    inputs = MRResize.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_MRResize_outputs():
    output_map = dict(out_file=dict(extensions=None))
    outputs = MRResize.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
