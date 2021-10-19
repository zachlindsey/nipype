# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import QualityIndex


def test_QualityIndex_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        autoclip=dict(argstr="-autoclip", usedefault=True, xor=["mask"]),
        automask=dict(argstr="-automask", usedefault=True, xor=["mask"]),
        clip=dict(argstr="-clip %f"),
        environ=dict(nohash=True, usedefault=True),
        in_file=dict(argstr="%s", extensions=None, mandatory=True, position=-2),
        interval=dict(argstr="-range", usedefault=True),
        mask=dict(argstr="-mask %s", extensions=None, xor=["autoclip", "automask"]),
        out_file=dict(
            argstr="> %s",
            extensions=None,
            keep_extension=False,
            name_source=["in_file"],
            name_template="%s_tqual",
            position=-1,
        ),
        quadrant=dict(argstr="-quadrant", usedefault=True),
        spearman=dict(argstr="-spearman", usedefault=True),
    )
    inputs = QualityIndex.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_QualityIndex_outputs():
    output_map = dict(out_file=dict(extensions=None))
    outputs = QualityIndex.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
