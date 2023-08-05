# -*- coding: utf-8 -*-

"""
PDF Generator
=============

Writing a Hello world PDF:

>>> from pdf_generator import Story, SimpleTemplate, Paragraph
>>> s = Story(SimpleTemplate())
>>> s.append(Paragraph('Hello world', 'h1', fontSize=15))
>>> s.append(Paragraph('pdf_generator is a simple and powerful lib to generate PDFs'))
>>> with open('out.pdf', 'wb') as out:
...     s.build(out, 'Hello World', 'Enix')
"""


from __future__ import absolute_import

__version__ = '1.0'

__all__ = [
    'Story',
    'SimpleTemplate',
    'Paragraph',
]


from pdf_generator.styles import Paragraph
from pdf_generator.pdf_generator import Story
from pdf_generator.templates import SimpleTemplate
