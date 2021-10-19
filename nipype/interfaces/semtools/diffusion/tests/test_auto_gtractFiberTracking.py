# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..gtract import gtractFiberTracking


def test_gtractFiberTracking_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        branchingAngle=dict(argstr="--branchingAngle %f"),
        branchingThreshold=dict(argstr="--branchingThreshold %f"),
        curvatureThreshold=dict(argstr="--curvatureThreshold %f"),
        endingSeedsLabel=dict(argstr="--endingSeedsLabel %d"),
        environ=dict(nohash=True, usedefault=True),
        guidedCurvatureThreshold=dict(argstr="--guidedCurvatureThreshold %f"),
        inputAnisotropyVolume=dict(
            argstr="--inputAnisotropyVolume %s", extensions=None
        ),
        inputEndingSeedsLabelMapVolume=dict(
            argstr="--inputEndingSeedsLabelMapVolume %s", extensions=None
        ),
        inputStartingSeedsLabelMapVolume=dict(
            argstr="--inputStartingSeedsLabelMapVolume %s", extensions=None
        ),
        inputTensorVolume=dict(argstr="--inputTensorVolume %s", extensions=None),
        inputTract=dict(argstr="--inputTract %s", extensions=None),
        maximumBranchPoints=dict(argstr="--maximumBranchPoints %d"),
        maximumGuideDistance=dict(argstr="--maximumGuideDistance %f"),
        maximumLength=dict(argstr="--maximumLength %f"),
        minimumLength=dict(argstr="--minimumLength %f"),
        numberOfThreads=dict(argstr="--numberOfThreads %d"),
        outputTract=dict(argstr="--outputTract %s", hash_files=False),
        randomSeed=dict(argstr="--randomSeed %d"),
        seedThreshold=dict(argstr="--seedThreshold %f"),
        startingSeedsLabel=dict(argstr="--startingSeedsLabel %d"),
        stepSize=dict(argstr="--stepSize %f"),
        tendF=dict(argstr="--tendF %f"),
        tendG=dict(argstr="--tendG %f"),
        trackingMethod=dict(argstr="--trackingMethod %s"),
        trackingThreshold=dict(argstr="--trackingThreshold %f"),
        useLoopDetection=dict(argstr="--useLoopDetection "),
        useRandomWalk=dict(argstr="--useRandomWalk "),
        useTend=dict(argstr="--useTend "),
        writeXMLPolyDataFile=dict(argstr="--writeXMLPolyDataFile "),
    )
    inputs = gtractFiberTracking.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_gtractFiberTracking_outputs():
    output_map = dict(outputTract=dict(extensions=None))
    outputs = gtractFiberTracking.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
