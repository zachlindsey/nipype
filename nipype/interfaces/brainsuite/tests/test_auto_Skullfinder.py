# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..brainsuite import Skullfinder


def test_Skullfinder_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        bgLabelValue=dict(argstr="--bglabel %d"),
        brainLabelValue=dict(argstr="--brainlabel %d"),
        environ=dict(nohash=True, usedefault=True),
        inputMRIFile=dict(argstr="-i %s", extensions=None, mandatory=True),
        inputMaskFile=dict(argstr="-m %s", extensions=None, mandatory=True),
        lowerThreshold=dict(argstr="-l %d"),
        outputLabelFile=dict(argstr="-o %s", extensions=None, genfile=True),
        performFinalOpening=dict(argstr="--finalOpening"),
        scalpLabelValue=dict(argstr="--scalplabel %d"),
        skullLabelValue=dict(argstr="--skulllabel %d"),
        spaceLabelValue=dict(argstr="--spacelabel %d"),
        surfaceFilePrefix=dict(argstr="-s %s"),
        upperThreshold=dict(argstr="-u %d"),
        verbosity=dict(argstr="-v %d"),
    )
    inputs = Skullfinder.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Skullfinder_outputs():
    output_map = dict(outputLabelFile=dict(extensions=None))
    outputs = Skullfinder.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
