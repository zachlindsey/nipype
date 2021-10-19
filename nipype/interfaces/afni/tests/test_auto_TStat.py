# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import TStat


def test_TStat_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        environ=dict(nohash=True, usedefault=True),
        in_file=dict(
            argstr="%s", copyfile=False, extensions=None, mandatory=True, position=-1
        ),
        mask=dict(argstr="-mask %s", extensions=None),
        num_threads=dict(nohash=True, usedefault=True),
        options=dict(argstr="%s"),
        out_file=dict(
            argstr="-prefix %s",
            extensions=None,
            name_source="in_file",
            name_template="%s_tstat",
        ),
        outputtype=dict(),
    )
    inputs = TStat.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_TStat_outputs():
    output_map = dict(out_file=dict(extensions=None))
    outputs = TStat.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
