# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..svm import SVMTrain


def test_SVMTrain_inputs():
    input_map = dict(
        alphas=dict(
            argstr="-alpha %s",
            extensions=None,
            name_source="in_file",
            name_template="%s_alphas",
            suffix="_alphas",
        ),
        args=dict(argstr="%s"),
        censor=dict(argstr="-censor %s", extensions=None),
        environ=dict(nohash=True, usedefault=True),
        in_file=dict(
            argstr="-trainvol %s", copyfile=False, extensions=None, mandatory=True
        ),
        kernel=dict(argstr="-kernel %s"),
        mask=dict(argstr="-mask %s", copyfile=False, extensions=None, position=-1),
        max_iterations=dict(argstr="-max_iterations %d"),
        model=dict(
            argstr="-model %s",
            extensions=None,
            name_source="in_file",
            name_template="%s_model",
            suffix="_model",
        ),
        nomodelmask=dict(argstr="-nomodelmask"),
        num_threads=dict(nohash=True, usedefault=True),
        options=dict(argstr="%s"),
        out_file=dict(
            argstr="-bucket %s",
            extensions=None,
            name_source="in_file",
            name_template="%s_vectors",
            suffix="_bucket",
        ),
        outputtype=dict(),
        trainlabels=dict(argstr="-trainlabels %s", extensions=None),
        ttype=dict(argstr="-type %s", mandatory=True),
        w_out=dict(argstr="-wout"),
    )
    inputs = SVMTrain.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_SVMTrain_outputs():
    output_map = dict(
        alphas=dict(extensions=None),
        model=dict(extensions=None),
        out_file=dict(extensions=None),
    )
    outputs = SVMTrain.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
