# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..reconst import FitTensor


def test_FitTensor_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        bval_scale=dict(argstr="-bvalue_scaling %s"),
        environ=dict(nohash=True, usedefault=True),
        grad_file=dict(argstr="-grad %s", extensions=None, xor=["grad_fsl"]),
        grad_fsl=dict(argstr="-fslgrad %s %s", xor=["grad_file"]),
        in_bval=dict(extensions=None),
        in_bvec=dict(argstr="-fslgrad %s %s", extensions=None),
        in_file=dict(argstr="%s", extensions=None, mandatory=True, position=-2),
        in_mask=dict(argstr="-mask %s", extensions=None),
        method=dict(argstr="-method %s"),
        nthreads=dict(argstr="-nthreads %d", nohash=True),
        out_file=dict(
            argstr="%s", extensions=None, mandatory=True, position=-1, usedefault=True
        ),
        predicted_signal=dict(argstr="-predicted_signal %s", extensions=None),
        reg_term=dict(argstr="-regularisation %f", max_ver="0.3.13"),
    )
    inputs = FitTensor.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_FitTensor_outputs():
    output_map = dict(
        out_file=dict(extensions=None), predicted_signal=dict(extensions=None)
    )
    outputs = FitTensor.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
