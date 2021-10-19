# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import MotionOutliers


def test_MotionOutliers_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        dummy=dict(argstr="--dummy=%d"),
        environ=dict(nohash=True, usedefault=True),
        in_file=dict(argstr="-i %s", extensions=None, mandatory=True),
        mask=dict(argstr="-m %s", extensions=None),
        metric=dict(argstr="--%s"),
        no_motion_correction=dict(argstr="--nomoco"),
        out_file=dict(
            argstr="-o %s",
            extensions=None,
            hash_files=False,
            keep_extension=True,
            name_source="in_file",
            name_template="%s_outliers.txt",
        ),
        out_metric_plot=dict(
            argstr="-p %s",
            extensions=None,
            hash_files=False,
            keep_extension=True,
            name_source="in_file",
            name_template="%s_metrics.png",
        ),
        out_metric_values=dict(
            argstr="-s %s",
            extensions=None,
            hash_files=False,
            keep_extension=True,
            name_source="in_file",
            name_template="%s_metrics.txt",
        ),
        output_type=dict(),
        threshold=dict(argstr="--thresh=%g"),
    )
    inputs = MotionOutliers.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_MotionOutliers_outputs():
    output_map = dict(
        out_file=dict(extensions=None),
        out_metric_plot=dict(extensions=None),
        out_metric_values=dict(extensions=None),
    )
    outputs = MotionOutliers.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
