# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import Cat


def test_Cat_inputs():
    input_map = dict(
        args=dict(argstr="%s"),
        environ=dict(nohash=True, usedefault=True),
        in_files=dict(argstr="%s", mandatory=True, position=-2),
        keepfree=dict(argstr="-nonfixed"),
        num_threads=dict(nohash=True, usedefault=True),
        omitconst=dict(argstr="-nonconst"),
        out_cint=dict(
            xor=["out_format", "out_nice", "out_double", "out_fint", "out_int"]
        ),
        out_double=dict(
            argstr="-d",
            xor=["out_format", "out_nice", "out_int", "out_fint", "out_cint"],
        ),
        out_file=dict(
            argstr="> %s", extensions=None, mandatory=True, position=-1, usedefault=True
        ),
        out_fint=dict(
            argstr="-f",
            xor=["out_format", "out_nice", "out_double", "out_int", "out_cint"],
        ),
        out_format=dict(
            argstr="-form %s",
            xor=["out_int", "out_nice", "out_double", "out_fint", "out_cint"],
        ),
        out_int=dict(
            argstr="-i",
            xor=["out_format", "out_nice", "out_double", "out_fint", "out_cint"],
        ),
        out_nice=dict(
            argstr="-n",
            xor=["out_format", "out_int", "out_double", "out_fint", "out_cint"],
        ),
        outputtype=dict(),
        sel=dict(argstr="-sel %s"),
        stack=dict(argstr="-stack"),
    )
    inputs = Cat.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Cat_outputs():
    output_map = dict(out_file=dict(extensions=None))
    outputs = Cat.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
