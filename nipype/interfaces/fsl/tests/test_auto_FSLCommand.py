# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..base import FSLCommand


def test_FSLCommand_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        environ=dict(nohash=True, usedefault=True),
        output_type=dict(),
    )
    inputs = FSLCommand.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
