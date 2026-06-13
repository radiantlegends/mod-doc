from .cli import parse_args
from .io_utils import load_file, write_file
from .assembler import build_document

def main():
    """
    Orchestrates the loading and assembly of documentation modules.
    """
    args = parse_args()
    if(args.command == "build"):
        build_order = load_file(args.build_order_path)
        parsed_list = build_order.split("\n")
        result = build_document(parsed_list)
        write_file(args.output_path, result)