# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import LocalBistat


def test_LocalBistat_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        automask=dict(argstr="-automask", xor=["weight_file"]),
        environ=dict(nohash=True, usedefault=True),
        in_file1=dict(argstr="%s", extensions=None, mandatory=True, position=-2),
        in_file2=dict(argstr="%s", extensions=None, mandatory=True, position=-1),
        mask_file=dict(argstr="-mask %s", extensions=None),
        neighborhood=dict(argstr="-nbhd '%s(%s)'", mandatory=True),
        num_threads=dict(nohash=True, usedefault=True),
        out_file=dict(
            argstr="-prefix %s",
            extensions=None,
            keep_extension=True,
            name_source="in_file1",
            name_template="%s_bistat",
            position=0,
        ),
        outputtype=dict(),
        stat=dict(argstr="-stat %s...", mandatory=True),
        weight_file=dict(argstr="-weight %s", extensions=None, xor=["automask"]),
    )
    inputs = LocalBistat.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_LocalBistat_outputs():
    output_map = dict(out_file=dict(extensions=None))
    outputs = LocalBistat.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
