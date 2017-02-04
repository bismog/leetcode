#!/usr/bin/env python

import markdown
# html = markdown.markdown(source, extensions=['markdown_checklist.extension'])
source = "checklist.md"
html = markdown.markdown(source, extensions=['markdown_checklist.extension'])
