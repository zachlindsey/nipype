from pathlib import Path
from nipype import Node
from nipype.interfaces.afni import Zeropad
from nipype.testing.fixtures import create_files_in_directory


def test_zeropad_handles_outfile_default(create_files_in_directory):
    filelist, outdir = create_files_in_directory
    zp = Zeropad(I=1)
    zp.inputs.in_files = filelist[0]

    result = zp.run()

    assert (Path(outdir) / "zeropad+tlrc.BRIK").exists()
    assert Path(result.outputs.out_file).name == "zeropad+tlrc.BRIK"


def test_zeropad_handles_outfile_specified_nii_gz(create_files_in_directory):
    filelist, outdir = create_files_in_directory
    zp = Zeropad(I=1, out_file="padded.nii.gz")
    zp.inputs.in_files = filelist[0]

    result = zp.run()

    assert (Path(outdir) / "padded.nii.gz").exists()
    assert Path(result.outputs.out_file).name == "padded.nii.gz"


def test_zeropad_keeps_file_after_node_run(create_files_in_directory):
    filelist, outdir = create_files_in_directory

    zp = Node(
        Zeropad(I=1, out_file="padded.nii.gz"), name="test_zeropad", base_dir=outdir
    )
    zp.inputs.in_files = Path(outdir) / filelist[0]

    result = zp.run()
    assert (Path(zp.output_dir()) / "padded.nii.gz").exists()
    assert Path(result.outputs.out_file).name == "padded.nii.gz"
