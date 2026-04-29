# SPDX-FileCopyrightText: 2024 Contributors
# SPDX-License-Identifier: MIT

"""MarkItDown - Convert various file formats to Markdown.

This package provides utilities to convert documents, spreadsheets,
presentations, images, audio, and web content into Markdown format.
"""

from markitdown._markitdown import MarkItDown, DocumentConverter, ConversionResult

__all__ = [
    "MarkItDown",
    "DocumentConverter",
    "ConversionResult",
]

__version__ = "0.1.0"
