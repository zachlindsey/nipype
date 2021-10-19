# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import EditTransform


def test_EditTransform_inputs():
    input_map = dict(
        interpolation=dict(argstr="FinalBSplineInterpolationOrder", usedefault=True),
        output_file=dict(extensions=None),
        output_format=dict(argstr="ResultImageFormat"),
        output_type=dict(argstr="ResultImagePixelType"),
        reference_image=dict(extensions=None),
        transform_file=dict(extensions=None, mandatory=True),
    )
    inputs = EditTransform.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_EditTransform_outputs():
    output_map = dict(output_file=dict(extensions=None))
    outputs = EditTransform.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
