# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import NwarpApply


def test_NwarpApply_inputs():
    input_map = dict(
        ainterp=dict(argstr="-ainterp %s"),
        args=dict(argstr="%s"),
        environ=dict(nohash=True, usedefault=True),
        in_file=dict(argstr="-source %s", mandatory=True),
        interp=dict(argstr="-interp %s", usedefault=True),
        inv_warp=dict(argstr="-iwarp"),
        master=dict(argstr="-master %s", extensions=None),
        out_file=dict(
            argstr="-prefix %s",
            extensions=None,
            name_source="in_file",
            name_template="%s_Nwarp",
        ),
        quiet=dict(argstr="-quiet", xor=["verb"]),
        short=dict(argstr="-short"),
        verb=dict(argstr="-verb", xor=["quiet"]),
        warp=dict(argstr="-nwarp %s", mandatory=True),
    )
    inputs = NwarpApply.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_NwarpApply_outputs():
    output_map = dict(out_file=dict(extensions=None))
    outputs = NwarpApply.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
