# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..registration import DiffeoScalarVol


def test_DiffeoScalarVol_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        environ=dict(nohash=True, usedefault=True),
        flip=dict(argstr="-flip %d %d %d"),
        in_file=dict(argstr="-in %s", extensions=None, mandatory=True),
        interpolation=dict(argstr="-interp %s", usedefault=True),
        out_file=dict(
            argstr="-out %s",
            extensions=None,
            keep_extension=True,
            name_source="in_file",
            name_template="%s_diffeoxfmd",
        ),
        resampling_type=dict(argstr="-type %s"),
        target=dict(argstr="-target %s", extensions=None, xor=["voxel_size"]),
        transform=dict(argstr="-trans %s", extensions=None, mandatory=True),
        voxel_size=dict(argstr="-vsize %g %g %g", xor=["target"]),
    )
    inputs = DiffeoScalarVol.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_DiffeoScalarVol_outputs():
    output_map = dict(out_file=dict(extensions=None))
    outputs = DiffeoScalarVol.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
