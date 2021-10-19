# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..image import Rescale


def test_Rescale_inputs():
    input_map = dict(
        in_file=dict(extensions=None, mandatory=True),
        invert=dict(),
        percentile=dict(usedefault=True),
        ref_file=dict(extensions=None, mandatory=True),
    )
    inputs = Rescale.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Rescale_outputs():
    output_map = dict(out_file=dict(extensions=None))
    outputs = Rescale.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
