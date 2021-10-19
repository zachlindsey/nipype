# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import Erode


def test_Erode_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        debug=dict(argstr="-debug", position=1),
        dilate=dict(argstr="-dilate", position=1),
        environ=dict(nohash=True, usedefault=True),
        in_file=dict(argstr="%s", extensions=None, mandatory=True, position=-2),
        number_of_passes=dict(argstr="-npass %s"),
        out_filename=dict(argstr="%s", extensions=None, genfile=True, position=-1),
        quiet=dict(argstr="-quiet", position=1),
    )
    inputs = Erode.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Erode_outputs():
    output_map = dict(out_file=dict(extensions=None))
    outputs = Erode.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
