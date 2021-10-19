# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..model import SegStatsReconAll


def test_SegStatsReconAll_inputs():
    input_map = dict(
        annot=dict(
            argstr="--annot %s %s %s",
            mandatory=True,
            xor=("segmentation_file", "annot", "surf_label"),
        ),
        args=dict(argstr="%s"),
        aseg=dict(extensions=None),
        avgwf_file=dict(argstr="--avgwfvol %s"),
        avgwf_txt_file=dict(argstr="--avgwf %s"),
        brain_vol=dict(argstr="--%s"),
        brainmask_file=dict(argstr="--brainmask %s", extensions=None),
        calc_power=dict(argstr="--%s"),
        calc_snr=dict(argstr="--snr"),
        color_table_file=dict(
            argstr="--ctab %s",
            extensions=None,
            xor=("color_table_file", "default_color_table", "gca_color_table"),
        ),
        copy_inputs=dict(),
        cortex_vol_from_surf=dict(argstr="--surf-ctx-vol"),
        default_color_table=dict(
            argstr="--ctab-default",
            xor=("color_table_file", "default_color_table", "gca_color_table"),
        ),
        empty=dict(argstr="--empty"),
        environ=dict(nohash=True, usedefault=True),
        etiv=dict(argstr="--etiv"),
        etiv_only=dict(),
        euler=dict(argstr="--euler"),
        exclude_ctx_gm_wm=dict(argstr="--excl-ctxgmwm"),
        exclude_id=dict(argstr="--excludeid %d"),
        frame=dict(argstr="--frame %d"),
        gca_color_table=dict(
            argstr="--ctab-gca %s",
            extensions=None,
            xor=("color_table_file", "default_color_table", "gca_color_table"),
        ),
        in_file=dict(argstr="--i %s", extensions=None),
        in_intensity=dict(argstr="--in %s --in-intensity-name %s", extensions=None),
        intensity_units=dict(
            argstr="--in-intensity-units %s", requires=["in_intensity"]
        ),
        lh_orig_nofix=dict(extensions=None, mandatory=True),
        lh_pial=dict(extensions=None, mandatory=True),
        lh_white=dict(extensions=None, mandatory=True),
        mask_erode=dict(argstr="--maskerode %d"),
        mask_file=dict(argstr="--mask %s", extensions=None),
        mask_frame=dict(requires=["mask_file"]),
        mask_invert=dict(argstr="--maskinvert"),
        mask_sign=dict(),
        mask_thresh=dict(argstr="--maskthresh %f"),
        multiply=dict(argstr="--mul %f"),
        non_empty_only=dict(argstr="--nonempty"),
        partial_volume_file=dict(argstr="--pv %s", extensions=None),
        presurf_seg=dict(extensions=None),
        rh_orig_nofix=dict(extensions=None, mandatory=True),
        rh_pial=dict(extensions=None, mandatory=True),
        rh_white=dict(extensions=None, mandatory=True),
        ribbon=dict(extensions=None, mandatory=True),
        segment_id=dict(argstr="--id %s..."),
        segmentation_file=dict(
            argstr="--seg %s",
            extensions=None,
            mandatory=True,
            xor=("segmentation_file", "annot", "surf_label"),
        ),
        sf_avg_file=dict(argstr="--sfavg %s"),
        subcort_gm=dict(argstr="--subcortgray"),
        subject_id=dict(argstr="--subject %s", mandatory=True, usedefault=True),
        subjects_dir=dict(),
        summary_file=dict(
            argstr="--sum %s", extensions=None, genfile=True, position=-1
        ),
        supratent=dict(argstr="--supratent"),
        surf_label=dict(
            argstr="--slabel %s %s %s",
            mandatory=True,
            xor=("segmentation_file", "annot", "surf_label"),
        ),
        total_gray=dict(argstr="--totalgray"),
        transform=dict(extensions=None, mandatory=True),
        vox=dict(argstr="--vox %s"),
        wm_vol_from_surf=dict(argstr="--surf-wm-vol"),
    )
    inputs = SegStatsReconAll.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_SegStatsReconAll_outputs():
    output_map = dict(
        avgwf_file=dict(extensions=None),
        avgwf_txt_file=dict(extensions=None),
        sf_avg_file=dict(extensions=None),
        summary_file=dict(extensions=None),
    )
    outputs = SegStatsReconAll.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
