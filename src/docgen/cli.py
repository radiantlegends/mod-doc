import argparse

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Assemble modular documentation from text files."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    #docgen build build_order.txt output.md
    build_parser = subparsers.add_parser(
        "build",
        help="Build a document from a build order file."
    )
    build_parser.add_argument(
        "build_order_path",
        type=str,
        help="Path to the build order file (e.g., build_order.txt)."
    )
    build_parser.add_argument(
        "output_path",
        type=str,
        help="Where to write the assembled document (e.g., output.md)."
    )
    return parser.parse_args()