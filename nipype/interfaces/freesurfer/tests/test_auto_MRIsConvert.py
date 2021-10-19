# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import MRIsConvert


def test_MRIsConvert_inputs():
    input_map = dict(
        annot_file=dict(argstr="--annot %s", extensions=None),
        args=dict(argstr="%s"),
        dataarray_num=dict(argstr="--da_num %d"),
        environ=dict(nohash=True, usedefault=True),
        functional_file=dict(argstr="-f %s", extensions=None),
        in_file=dict(argstr="%s", extensions=None, mandatory=True, position=-2),
        label_file=dict(argstr="--label %s", extensions=None),
        labelstats_outfile=dict(argstr="--labelstats %s", extensions=None),
        normal=dict(argstr="-n"),
        origname=dict(argstr="-o %s"),
        out_datatype=dict(mandatory=True, xor=["out_file"]),
        out_file=dict(
            argstr="%s",
            extensions=None,
            genfile=True,
            mandatory=True,
            position=-1,
            xor=["out_datatype"],
        ),
        parcstats_file=dict(argstr="--parcstats %s", extensions=None),
        patch=dict(argstr="-p"),
        rescale=dict(argstr="-r"),
        scalarcurv_file=dict(argstr="-c %s", extensions=None),
        scale=dict(argstr="-s %.3f"),
        subjects_dir=dict(),
        talairachxfm_subjid=dict(argstr="-t %s"),
        to_scanner=dict(argstr="--to-scanner"),
        to_tkr=dict(argstr="--to-tkr"),
        vertex=dict(argstr="-v"),
        xyz_ascii=dict(argstr="-a"),
    )
    inputs = MRIsConvert.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_MRIsConvert_outputs():
    output_map = dict(converted=dict(extensions=None))
    outputs = MRIsConvert.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
