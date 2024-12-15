# OasYamlCombinePy
A wrapper over a dynamic library build of [openapi-utils](https://github.com/sarpt/openapi-utils)

Takes input .yaml file and follows references to inline everything in a single output .yaml file
Tool can resolve local refs (refs pointing to objects in the same file) and remote refs (refs pointing to object in other files)

## requirements
- `liboasyamlcombine.so` from [openapi-utils](https://github.com/sarpt/openapi-utils) needs to be placed in the `vendor` directory (can be obtained from "Releases")
- python >=3.8
- OS needs to support .so (linux, unix, etc.)

## usage
The packages are available at [pypi](https://pypi.org/project/oas-yaml-combine-py/). They include `liboasyamlcombine.so` with them.

The project can be used as either as a cmd which behaves similarily to a cmd from [openapi-utils](https://github.com/sarpt/openapi-utils), or as library exposing `resolve_references` function, example:

```python
from oas_yaml_combine import resolve_references
resolve_references(
    input_path="/some/path/input.yaml",
    output_path="/some/path/output.yaml",
    refs_dir="/some/path/refs",
    inline_local=True,
    inline_remote=True,
    keep_local=False
)
```

## cmd arguments

- `help` - help
- `input` - path to input file that has refs that need to be resolved. When not provided, stdin is used
- `output` - path to output file to which input file with resolved refs should be saved. When not provided, stdout is used
- `refsdir` - path to directory where files containing remote refs are stored. When not provided a directory of input-file is used
- `inlinelocal` - (default: `False`) when set to `True` local refs are replaced with local objects, otherwise local refs stay in place
- `inlineremote` - (default: `False`) when set to `True` remote refs are replaced with remote objects, otherwise remote refs stay in place
- `keeplocal` - (default: `False`) when set to `True` along with `inlinelocal` keeps local reference objects after inlining, otherwise deletes them. When set to `True` with `inlinelocal` set to false does nothing to prevent from making dangling local references, and therefore creating incorrect specifications

## building

`pipx run build` in project root will create packages in `dist` directory
