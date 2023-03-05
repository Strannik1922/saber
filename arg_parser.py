import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Tool to merge two log files')

    parser.add_argument(
        'log1_file',
        metavar='<path/to/log1>',
        type=Path,
        help='path to first log file',
    )

    parser.add_argument(
        'log2_file',
        metavar='<path/to/log2>',
        type=Path,
        help='path to second log file'
    )

    parser.add_argument(
        '-o', '--output',
        type=Path,
        default='log_merged.jsonl',
        help='path to output file',
        dest='merged_log_file',
    )

    return parser.parse_args()
