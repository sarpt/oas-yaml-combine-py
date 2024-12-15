from ctypes import *
import argparse

lib = cdll.LoadLibrary("./vendor/liboasyamlcombine.so")

def resolve_references(input_path: str, output_path: str, refs_dir: str, inline_local: bool, inline_remote: bool, keep_local: bool):
	result = lib.oasYamlCombine(
		c_char_p(str.encode(input_path)),
		c_char_p(str.encode(output_path)),
		c_char_p(str.encode(refs_dir)),
		1 if inline_local else 0,
		1 if inline_remote else 0,
		1 if keep_local else 0
	)

	if result == 0:
		return


if __name__ == '__main__':
	parser=argparse.ArgumentParser()

	parser.add_argument("--input", help="Do the bar option", default="")
	parser.add_argument("--output", help="Foo the program", default="")
	parser.add_argument("--refsdir", help="Foo the program", default="")
	parser.add_argument("--inlinelocal", help="Foo the program", action="store_true", default=False)
	parser.add_argument("--inlineremote", help="Foo the program", action="store_true", default=False)
	parser.add_argument("--keeplocal", help="Foo the program", action="store_true", default=False)

	args=parser.parse_args()

	resolve_references(input_path=args.input, output_path=args.output, refs_dir=args.refsdir, inline_local=args.inlinelocal, inline_remote=args.inlineremote, keep_local=args.keeplocal)