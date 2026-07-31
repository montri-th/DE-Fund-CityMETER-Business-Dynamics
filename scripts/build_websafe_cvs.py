#!/usr/bin/env python3
"""Build rasterized public CV previews with contact details and signatures withheld."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import fitz


CONTACT_START = "ที่อยู่"
CONTACT_END = "โทรสาร"
CONTACT_NOTE = "Contact details withheld in this web-safe copy."
SIGNATURE_NOTE = "Signature withheld in this web-safe copy."


def first_word_rect(page: fitz.Page, text: str) -> fitz.Rect:
    matches = page.search_for(text)
    if not matches:
        raise ValueError(f"Could not find {text!r} on page {page.number + 1}")
    return matches[0]


def redact_contact_block(page: fitz.Page) -> None:
    start = first_word_rect(page, CONTACT_START)
    end = first_word_rect(page, CONTACT_END)
    block = fitz.Rect(45, start.y0 - 4, page.rect.width - 45, end.y1 + 5)
    page.add_redact_annot(block, fill=(0.97, 0.96, 0.92))
    page.apply_redactions()
    page.insert_textbox(
        fitz.Rect(block.x0 + 8, block.y0 + 8, block.x1 - 8, block.y1 - 8),
        CONTACT_NOTE,
        fontsize=9,
        fontname="helv",
        color=(0.18, 0.26, 0.31),
        align=fitz.TEXT_ALIGN_LEFT,
    )


def redact_signature_images(page: fitz.Page) -> None:
    signature_rects: list[fitz.Rect] = []
    for image in page.get_images(full=True):
        for rect in page.get_image_rects(image[0]):
            if rect.x0 > page.rect.width * 0.55 and rect.y0 > 180:
                signature_rects.append(rect)
    if not signature_rects:
        raise ValueError(f"Could not locate signature image on page {page.number + 1}")
    for rect in signature_rects:
        padded = fitz.Rect(rect.x0 - 3, rect.y0 - 3, rect.x1 + 3, rect.y1 + 3)
        page.add_redact_annot(padded, fill=(0.97, 0.96, 0.92))
    page.apply_redactions()
    for rect in signature_rects:
        note_rect = fitz.Rect(rect.x0, rect.y0 + 3, rect.x1, rect.y1 - 3)
        page.insert_textbox(
            note_rect,
            SIGNATURE_NOTE,
            fontsize=6.5,
            fontname="helv",
            color=(0.18, 0.26, 0.31),
            align=fitz.TEXT_ALIGN_CENTER,
        )


def rasterize_document(source: fitz.Document, output_path: Path, title: str) -> None:
    public = fitz.open()
    matrix = fitz.Matrix(2, 2)
    for page in source:
        pixmap = page.get_pixmap(matrix=matrix, alpha=False)
        image = pixmap.tobytes("jpeg", jpg_quality=86)
        target = public.new_page(width=page.rect.width, height=page.rect.height)
        target.insert_image(target.rect, stream=image)
    public.set_metadata(
        {
            "title": title,
            "author": "Landometer",
            "subject": "Public web-safe CV preview; contact details and signatures withheld",
            "keywords": "DE Fund, CityMETER, CV, web-safe",
            "creator": "Landometer web-safe CV build",
            "producer": "PyMuPDF",
        }
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    public.save(
        output_path,
        garbage=4,
        deflate=True,
        clean=True,
        no_new_id=True,
        preserve_metadata=False,
    )
    public.close()


def build_one(input_path: Path, output_path: Path) -> None:
    source = fitz.open(input_path)
    if len(source) != 3:
        raise ValueError(f"Expected 3 pages in {input_path}, found {len(source)}")
    redact_contact_block(source[0])
    redact_signature_images(source[2])
    title = f"{source.metadata.get('title') or input_path.stem} - web-safe preview"
    rasterize_document(source, output_path, title)
    source.close()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    files = []
    for number in range(1, 12):
        output_path = args.output_dir / f"b{number}-web.pdf"
        build_one(
            args.input_dir / f"b{number}.pdf",
            output_path,
        )
        files.append(
            {
                "roleId": f"B{number}",
                "file": output_path.name,
                "pages": 3,
                "sha256": hashlib.sha256(output_path.read_bytes()).hexdigest(),
            }
        )
    manifest = {
        "schemaVersion": "1.0",
        "purpose": "Public web-safe CV previews for the CityMETER DE Fund explainer",
        "sourcePolicy": "Original evidence PDFs remain access-controlled in Google Drive",
        "privacyTransformations": [
            "withhold personal address block",
            "withhold email and telephone fields",
            "withhold signature imagery",
            "rasterize every page to remove the source text layer and embedded metadata",
        ],
        "files": files,
    }
    (args.output_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
