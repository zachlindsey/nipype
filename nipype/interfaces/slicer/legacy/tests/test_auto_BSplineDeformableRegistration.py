# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..registration import BSplineDeformableRegistration


def test_BSplineDeformableRegistration_inputs():
    input_map = dict(
        FixedImageFileName=dict(argstr="%s", extensions=None, position=-2),
        MovingImageFileName=dict(argstr="%s", extensions=None, position=-1),
        args=dict(argstr="%s"),
        constrain=dict(argstr="--constrain "),
        default=dict(argstr="--default %d"),
        environ=dict(nohash=True, usedefault=True),
        gridSize=dict(argstr="--gridSize %d"),
        histogrambins=dict(argstr="--histogrambins %d"),
        initialtransform=dict(argstr="--initialtransform %s", extensions=None),
        iterations=dict(argstr="--iterations %d"),
        maximumDeformation=dict(argstr="--maximumDeformation %f"),
        outputtransform=dict(argstr="--outputtransform %s", hash_files=False),
        outputwarp=dict(argstr="--outputwarp %s", hash_files=False),
        resampledmovingfilename=dict(
            argstr="--resampledmovingfilename %s", hash_files=False
        ),
        spatialsamples=dict(argstr="--spatialsamples %d"),
    )
    inputs = BSplineDeformableRegistration.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_BSplineDeformableRegistration_outputs():
    output_map = dict(
        outputtransform=dict(extensions=None),
        outputwarp=dict(extensions=None),
        resampledmovingfilename=dict(extensions=None),
    )
    outputs = BSplineDeformableRegistration.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
