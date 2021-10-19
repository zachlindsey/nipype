# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import Despike


def test_Despike_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        environ=dict(nohash=True, usedefault=True),
        in_file=dict(
            argstr="%s", copyfile=False, extensions=None, mandatory=True, position=-1
        ),
        num_threads=dict(nohash=True, usedefault=True),
        out_file=dict(
            argstr="-prefix %s",
            extensions=None,
            name_source="in_file",
            name_template="%s_despike",
        ),
        outputtype=dict(),
    )
    inputs = Despike.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Despike_outputs():
    output_map = dict(out_file=dict(extensions=None))
    outputs = Despike.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
