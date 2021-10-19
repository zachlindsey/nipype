# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..minc import Beast


def test_Beast_inputs():
    input_map = dict(
        abspath=dict(argstr="-abspath", usedefault=True),
        args=dict(argstr="%s"),
        clobber=dict(argstr="-clobber", usedefault=True),
        confidence_level_alpha=dict(argstr="-alpha %s", usedefault=True),
        configuration_file=dict(argstr="-configuration %s", extensions=None),
        environ=dict(nohash=True, usedefault=True),
        fill_holes=dict(argstr="-fill"),
        flip_images=dict(argstr="-flip"),
        input_file=dict(argstr="%s", extensions=None, mandatory=True, position=-2),
        library_dir=dict(argstr="%s", mandatory=True, position=-3),
        load_moments=dict(argstr="-load_moments"),
        median_filter=dict(argstr="-median"),
        nlm_filter=dict(argstr="-nlm_filter"),
        number_selected_images=dict(argstr="-selection_num %s", usedefault=True),
        output_file=dict(
            argstr="%s",
            extensions=None,
            hash_files=False,
            name_source=["input_file"],
            name_template="%s_beast_mask.mnc",
            position=-1,
        ),
        patch_size=dict(argstr="-patch_size %s", usedefault=True),
        probability_map=dict(argstr="-probability"),
        same_resolution=dict(argstr="-same_resolution"),
        search_area=dict(argstr="-search_area %s", usedefault=True),
        smoothness_factor_beta=dict(argstr="-beta %s", usedefault=True),
        threshold_patch_selection=dict(argstr="-threshold %s", usedefault=True),
        voxel_size=dict(argstr="-voxel_size %s", usedefault=True),
    )
    inputs = Beast.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Beast_outputs():
    output_map = dict(output_file=dict(extensions=None))
    outputs = Beast.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
