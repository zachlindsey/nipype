# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import FAST


def test_FAST_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        bias_iters=dict(argstr="-I %d"),
        bias_lowpass=dict(argstr="-l %d", units="mm"),
        environ=dict(nohash=True, usedefault=True),
        hyper=dict(argstr="-H %.2f"),
        img_type=dict(argstr="-t %d"),
        in_files=dict(argstr="%s", copyfile=False, mandatory=True, position=-1),
        init_seg_smooth=dict(argstr="-f %.3f"),
        init_transform=dict(argstr="-a %s", extensions=None),
        iters_afterbias=dict(argstr="-O %d"),
        manual_seg=dict(argstr="-s %s", extensions=None),
        mixel_smooth=dict(argstr="-R %.2f"),
        no_bias=dict(argstr="-N"),
        no_pve=dict(argstr="--nopve"),
        number_classes=dict(argstr="-n %d"),
        other_priors=dict(argstr="-A %s"),
        out_basename=dict(argstr="-o %s", extensions=None),
        output_biascorrected=dict(argstr="-B"),
        output_biasfield=dict(argstr="-b"),
        output_type=dict(),
        probability_maps=dict(argstr="-p"),
        segment_iters=dict(argstr="-W %d"),
        segments=dict(argstr="-g"),
        use_priors=dict(argstr="-P"),
        verbose=dict(argstr="-v"),
    )
    inputs = FAST.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_FAST_outputs():
    output_map = dict(
        bias_field=dict(),
        mixeltype=dict(extensions=None),
        partial_volume_files=dict(),
        partial_volume_map=dict(extensions=None),
        probability_maps=dict(),
        restored_image=dict(),
        tissue_class_files=dict(),
        tissue_class_map=dict(extensions=None),
    )
    outputs = FAST.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
