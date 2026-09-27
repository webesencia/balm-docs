#!/usr/bin/env python3
"""Guard for the "no long dash" rule of the documentation.

Exits 0 when the repository is clean and 1 when it is not, printing every offending
line. Run it before ending a batch and quote its output.

It is deliberately wider than a plain grep for the two characters, because that grep is
what the rule shipped with and dashes still came back three times. It covers:

  1. every Unicode dash-punctuation code point (category Pd), not only U+2014 and
     U+2013. U+2010, U+2011, U+2012 and U+2015 are indistinguishable from a long dash
     in an editor and in the theme editor;
  2. the JSON escaped forms, which a raw character grep cannot see and which is exactly
     how a locale file stores its text;
  3. the HTML entities, which is how a dash reaches a richtext default or a template.

The ASCII hyphen-minus is the only dash allowed.

Python is used rather than grep because the BSD grep shipped with macOS has no -P, so
\\p{Pd} is not available there and the check would silently pass.
"""
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "node_modules", ".shopify"}
SKIP_FILES = {os.path.basename(__file__)}
TEXT_EXT = {
    ".liquid", ".json", ".js", ".css", ".md", ".txt", ".svg", ".html", ".yml", ".yaml", ".py",
}
ESCAPES = re.compile(r"\\u201[0-5]", re.IGNORECASE)
ENTITIES = re.compile(r"&(mdash|ndash|#8212|#8211|#x2014|#x2013);", re.IGNORECASE)


def offending_chars(line):
    # ASCII U+002D is the one dash the rule allows, and it is also category Pd, so the
    # test has to be "dash punctuation that is not ASCII".
    return [c for c in line if ord(c) > 127 and unicodedata.category(c) == "Pd"]


def main():
    failures = []
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in sorted(files):
            if name in SKIP_FILES:
                continue
            if os.path.splitext(name)[1].lower() not in TEXT_EXT:
                continue
            path = os.path.join(base, name)
            rel = os.path.relpath(path, ROOT)
            try:
                with open(path, encoding="utf-8") as fh:
                    lines = fh.readlines()
            except (UnicodeDecodeError, OSError):
                continue
            for no, line in enumerate(lines, 1):
                text = line.rstrip("\n")
                found = offending_chars(text)
                if found:
                    names = ", ".join(
                        "U+%04X %s" % (ord(c), unicodedata.name(c, "?")) for c in sorted(set(found))
                    )
                    failures.append("%s:%d: %s | %s" % (rel, no, names, text.strip()[:110]))
                if ESCAPES.search(text):
                    failures.append("%s:%d: escaped dash | %s" % (rel, no, text.strip()[:110]))
                if ENTITIES.search(text):
                    failures.append("%s:%d: dash entity | %s" % (rel, no, text.strip()[:110]))

    for f in failures:
        print(f)
    if failures:
        print("check-dashes: FAILED, %d line(s). Reformulate the sentence, do not swap "
              "the character for a comma." % len(failures))
        status = 1
    else:
        print("check-dashes: clean. No dash-punctuation code point, no escaped form, no "
              "HTML entity anywhere in the repository.")
        status = 0
    return status


if __name__ == "__main__":
    sys.exit(main())
