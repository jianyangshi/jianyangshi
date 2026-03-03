#!/usr/bin/env python3
"""下载 YOLO 模型文件（默认保存为 yolos.pt）。"""

from __future__ import annotations

import argparse
import pathlib
import urllib.request


DEFAULT_URL = "https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11s.pt"
DEFAULT_OUTPUT = "yolos.pt"


def download_file(url: str, output_path: pathlib.Path) -> None:
    """从给定 URL 下载文件到本地。"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url) as response, output_path.open("wb") as f:
        f.write(response.read())


def main() -> None:
    parser = argparse.ArgumentParser(description="下载模型文件到本地")
    parser.add_argument(
        "--url",
        default=DEFAULT_URL,
        help=f"模型下载地址（默认: {DEFAULT_URL}）",
    )
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT,
        help=f"保存文件名（默认: {DEFAULT_OUTPUT}）",
    )
    args = parser.parse_args()

    output_path = pathlib.Path(args.output)
    download_file(args.url, output_path)
    print(f"下载完成: {output_path.resolve()}")


if __name__ == "__main__":
    main()
