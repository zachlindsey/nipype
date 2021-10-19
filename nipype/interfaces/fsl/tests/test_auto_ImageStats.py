# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import ImageStats


def test_ImageStats_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        environ=dict(nohash=True, usedefault=True),
        in_file=dict(argstr="%s", extensions=None, mandatory=True, position=3),
        index_mask_file=dict(argstr="-K %s", extensions=None, position=2),
        mask_file=dict(argstr="", extensions=None),
        op_string=dict(argstr="%s", mandatory=True, position=4),
        output_type=dict(),
        split_4d=dict(argstr="-t", position=1),
    )
    inputs = ImageStats.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ImageStats_outputs():
    output_map = dict(out_stat=dict())
    outputs = ImageStats.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
