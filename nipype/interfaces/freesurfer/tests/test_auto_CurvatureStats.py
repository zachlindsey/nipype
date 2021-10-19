# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import CurvatureStats


def test_CurvatureStats_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        copy_inputs=dict(),
        curvfile1=dict(argstr="%s", extensions=None, mandatory=True, position=-2),
        curvfile2=dict(argstr="%s", extensions=None, mandatory=True, position=-1),
        environ=dict(nohash=True, usedefault=True),
        hemisphere=dict(argstr="%s", mandatory=True, position=-3),
        min_max=dict(argstr="-m"),
        out_file=dict(
            argstr="-o %s",
            extensions=None,
            hash_files=False,
            name_source=["hemisphere"],
            name_template="%s.curv.stats",
        ),
        subject_id=dict(argstr="%s", mandatory=True, position=-4, usedefault=True),
        subjects_dir=dict(),
        surface=dict(argstr="-F %s", extensions=None),
        values=dict(argstr="-G"),
        write=dict(argstr="--writeCurvatureFiles"),
    )
    inputs = CurvatureStats.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_CurvatureStats_outputs():
    output_map = dict(out_file=dict(extensions=None))
    outputs = CurvatureStats.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
