# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..patchmatch import PatchMatch


def test_PatchMatch_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        cs_size=dict(argstr="-cs %i"),
        database_file=dict(
            argstr="-db %s", extensions=None, mandatory=True, position=3
        ),
        environ=dict(nohash=True, usedefault=True),
        in_file=dict(argstr="-i %s", extensions=None, mandatory=True, position=1),
        it_num=dict(argstr="-it %i"),
        mask_file=dict(argstr="-m %s", extensions=None, mandatory=True, position=2),
        match_num=dict(argstr="-match %i"),
        out_file=dict(
            argstr="-o %s",
            extensions=None,
            name_source=["in_file"],
            name_template="%s_pm.nii.gz",
            position=4,
        ),
        patch_size=dict(argstr="-size %i"),
        pm_num=dict(argstr="-pm %i"),
    )
    inputs = PatchMatch.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_PatchMatch_outputs():
    output_map = dict(out_file=dict(extensions=None))
    outputs = PatchMatch.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
