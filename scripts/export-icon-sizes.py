#!/usr/bin/env python3
"""Export fixed-size SVG and PNG icons. Requires Python 3 and Inkscape."""

from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "profile/assets/omnifex-icon.svg"
OUTPUT = SOURCE.parent / "icons"
SIZES = (16, 24, 32, 48, 64, 128, 256, 512, 1024)
SVG_NS = "http://www.w3.org/2000/svg"


def main():
    inkscape = shutil.which("inkscape")
    if inkscape is None:
        raise SystemExit("Install Inkscape and make its command available on PATH.")

    source = SOURCE.read_text(encoding="utf-8")
    opening = re.search(r"<svg\b[^>]*>", source)
    if opening is None:
        raise SystemExit("The source must contain an SVG root element.")

    # PNGs use the same resting mark as the reduced-motion SVG presentation.
    still = ET.fromstring(source)
    for parent in still.iter():
        for child in list(parent):
            if child.tag == f"{{{SVG_NS}}}style" or "shine" in child.get("class", "").split():
                parent.remove(child)
    ET.register_namespace("", SVG_NS)
    ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")

    OUTPUT.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="omnifex-icon-") as temporary:
        still_path = Path(temporary) / "still.svg"
        ET.ElementTree(still).write(still_path, encoding="utf-8", xml_declaration=True)

        for size in SIZES:
            # Only change the outer canvas dimensions. Keep the viewBox,
            # embedded artwork, animation, and reduced-motion rules intact.
            tag = re.sub(r'\b(width|height)="[^"]*"', lambda match: f'{match[1]}="{size}"', opening[0])
            svg = source[:opening.start()] + tag + source[opening.end():]
            stem = OUTPUT / f"omnifex-icon-{size}"
            stem.with_suffix(".svg").write_text(svg, encoding="utf-8")
            subprocess.run(
                [
                    inkscape,
                    str(still_path),
                    "--export-type=png",
                    "--export-area-page",
                    f"--export-width={size}",
                    f"--export-height={size}",
                    "--export-background-opacity=0",
                    f"--export-filename={stem.with_suffix('.png')}",
                ],
                check=True,
            )
            print(f"Exported {size} x {size} SVG and PNG")


if __name__ == "__main__":
    main()
