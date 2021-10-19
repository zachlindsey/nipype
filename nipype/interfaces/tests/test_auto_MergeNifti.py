# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..dcmstack import MergeNifti


def test_MergeNifti_inputs():
    input_map = dict(
        in_files=dict(mandatory=True),
        merge_dim=dict(),
        out_ext=dict(usedefault=True),
        out_format=dict(),
        out_path=dict(),
        sort_order=dict(),
    )
    inputs = MergeNifti.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_MergeNifti_outputs():
    output_map = dict(out_file=dict(extensions=None))
    outputs = MergeNifti.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
