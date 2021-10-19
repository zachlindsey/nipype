# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..cifti import CiftiSmooth


def test_CiftiSmooth_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        cerebellum_corrected_areas=dict(
            argstr="cerebellum-corrected-areas %s",
            extensions=None,
            position=10,
            requires=["cerebellum_surf"],
        ),
        cerebellum_surf=dict(
            argstr="-cerebellum-surface %s", extensions=None, position=9
        ),
        cifti_roi=dict(argstr="-cifti-roi %s", extensions=None, position=11),
        direction=dict(argstr="%s", mandatory=True, position=3),
        environ=dict(nohash=True, usedefault=True),
        fix_zeros_surf=dict(argstr="-fix-zeros-surface", position=13),
        fix_zeros_vol=dict(argstr="-fix-zeros-volume", position=12),
        in_file=dict(argstr="%s", extensions=None, mandatory=True, position=0),
        left_corrected_areas=dict(
            argstr="-left-corrected-areas %s", extensions=None, position=6
        ),
        left_surf=dict(
            argstr="-left-surface %s", extensions=None, mandatory=True, position=5
        ),
        merged_volume=dict(argstr="-merged-volume", position=14),
        out_file=dict(
            argstr="%s",
            extensions=None,
            keep_extension=True,
            name_source=["in_file"],
            name_template="smoothed_%s.nii",
            position=4,
        ),
        right_corrected_areas=dict(
            argstr="-right-corrected-areas %s", extensions=None, position=8
        ),
        right_surf=dict(
            argstr="-right-surface %s", extensions=None, mandatory=True, position=7
        ),
        sigma_surf=dict(argstr="%s", mandatory=True, position=1),
        sigma_vol=dict(argstr="%s", mandatory=True, position=2),
    )
    inputs = CiftiSmooth.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_CiftiSmooth_outputs():
    output_map = dict(out_file=dict(extensions=None))
    outputs = CiftiSmooth.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
