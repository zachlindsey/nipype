# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..registration import MPRtoMNI305


def test_MPRtoMNI305_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        environ=dict(nohash=True, usedefault=True),
        in_file=dict(argstr="%s", extensions=None, usedefault=True),
        reference_dir=dict(mandatory=True, usedefault=True),
        subjects_dir=dict(),
        target=dict(mandatory=True, usedefault=True),
    )
    inputs = MPRtoMNI305.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_MPRtoMNI305_outputs():
    output_map = dict(
        log_file=dict(extensions=None, usedefault=True), out_file=dict(extensions=None)
    )
    outputs = MPRtoMNI305.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
