# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..minc import BBox


def test_BBox_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        environ=dict(nohash=True, usedefault=True),
        format_minccrop=dict(argstr="-minccrop"),
        format_mincresample=dict(argstr="-mincresample"),
        format_mincreshape=dict(argstr="-mincreshape"),
        input_file=dict(argstr="%s", extensions=None, mandatory=True, position=-2),
        one_line=dict(argstr="-one_line", xor=("one_line", "two_lines")),
        out_file=dict(argstr="> %s", extensions=None, genfile=True, position=-1),
        output_file=dict(
            extensions=None,
            hash_files=False,
            keep_extension=False,
            name_source=["input_file"],
            name_template="%s_bbox.txt",
            position=-1,
        ),
        threshold=dict(argstr="-threshold"),
        two_lines=dict(argstr="-two_lines", xor=("one_line", "two_lines")),
    )
    inputs = BBox.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_BBox_outputs():
    output_map = dict(output_file=dict(extensions=None))
    outputs = BBox.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
