#!/usr/bin/env python3
"""
Convert $1 -- a markdown file to an HTML file in `/tmp/vim/<parent>/<basename>.html`.
"""

# Standard Library
from os.path import realpath, basename, isfile, isdir, dirname, abspath
import os
import shutil
import subprocess
import sys
import re
import logging
from logging import Logger
from typing import Dict, Iterable, Optional, Set, Text, List
from subprocess import DEVNULL, PIPE, run

from meta import MATHJAX_CONFS, LongOpt, CodeStyle, FromFmt, Ext, ToFmt
from utils import validate_executables, require_exists, vimdir_path, ensure_exists

# initalise logging with sane configuration
logging.basicConfig(level=logging.WARN,
                    format="%(levelname)s:%(asctime)s  %(message)s")

log: Logger = logging.getLogger()

validate_executables(["pandoc"])


# NOTE this will try to include a lua filter from `./task-list.lua`.
class PandocCmd:
    def __init__(
        self,
        input_file: Text,
        stylesheet: Text = vimdir_path("css", "styles.css"),
        javascript: Text = vimdir_path("js", "script.js"),
        from_fmt: FromFmt = FromFmt.MARKDOWN,
        to_fmt: ToFmt = ToFmt.HTML5,
        exts: List[Ext] = [
            Ext.ASCII_IDENTIFIERS,
            Ext.AUTOLINK_BARE_URIS,
            Ext.COMPACT_DEFINITION_LISTS,
            Ext.FENCED_DIVS,
            Ext.GFM_AUTO_IDENTIFIERS,
            Ext.INTRAWORD_UNDERSCORES,
            Ext.MARKDOWN_ATTRIBUTE,
            Ext.MMD_HEADER_IDENTIFIERS,
            Ext.MMD_LINK_ATTRIBUTES,
            Ext.SMART,
            Ext.TEX_MATH_DOLLARS,
            Ext.TEX_MATH_DOUBLE_BACKSLASH,
            Ext.TEX_MATH_SINGLE_BACKSLASH,
        ],
        no_exts: List[Ext] = [Ext.ALL_SYMBOLS_ESCAPABLE, Ext.ESCAPED_LINE_BREAKS],
        long_opts: Dict[LongOpt, Optional[Text]] = {
            LongOpt.ATX_HEADERS: None,
            LongOpt.REFERENCE_LOCATION: "document",
            LongOpt.SECTION_DIVS: None,
            LongOpt.EMAIL_OBFUSCATION: "javascript",
        },
        code_style: CodeStyle = CodeStyle.TANGO,
        mathjax_version: Text = "2.7.5",
        mathjax_conf: Text = "TeX-AMS_HTML",
        width: int = 80,
        toc_depth: int = 3,
    ) -> None:

        log.debug("initalising a PandocCmd object")

        self.exts: List[Ext] = []
        self.no_exts: List[Ext] = []
        self.long_opts: Dict[LongOpt, Optional[Text]] = dict()

        self.set_opts(long_opts).set_exts(exts).set_no_exts(no_exts).set_input_file(
            input_file
        ).set_opt(LongOpt.STANDALONE).set_to_fmt(to_fmt).set_from_fmt(
            from_fmt
        ).set_mathjax(
            mathjax_version, mathjax_conf
        ).set_width(
            width
        ).set_stylesheet(
            stylesheet
        ).set_code_style(
            code_style
        ).set_javascript(
            javascript
        )

        if toc_depth:
            self.set_toc_depth(toc_depth).set_opt(LongOpt.TOC)

        lua_filter: str = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'task-list.lua')

        if isfile(lua_filter):
            self.set_opt(LongOpt.LUA_FILTER, lua_filter)
        else:
            log.error(f'failed to find lua filter ./{lua_filter}')

    def set_from_fmt(self, fmt: FromFmt) -> object:
        assert fmt in FromFmt, f"from format '{fmt}' invalid"
        self.from_fmt: FromFmt = fmt
        return self

    def set_opt(self, key: LongOpt, val: Optional[Text] = None) -> object:
        self.long_opts[key] = val
        return self

    def set_opts(self, pairs: Dict[LongOpt, Optional[Text]]) -> object:
        for (k, v) in pairs.items():
            self.set_opt(k, v)
        return self

    def set_to_fmt(self, fmt: ToFmt) -> object:
        self.to_fmt = fmt
        return self

    def set_input_file(self, file_path: Text) -> object:
        require_exists(file_path)
        self.input_file = file_path
        return self

    def set_width(self, n: int) -> object:
        assert n and n >= 0, f"invalid value {str(n)}"
        return self.set_opt(LongOpt.COLUMNS, str(n))

    def set_stylesheet(self, css_path: Text) -> object:
        require_exists(css_path)
        return self.set_opt(LongOpt.CSS, css_path)

    def set_javascript(self, js_path: Text) -> object:
        require_exists(js_path)
        self.javascript = js_path
        return self

    def set_toc_depth(self, n: int) -> object:
        assert n and n >= 0, f"invalid value {n}"
        return self.set_opt(LongOpt.TOC_DEPTH, str(n))

    def set_code_style(self, style: CodeStyle) -> object:
        return self.set_opt(LongOpt.HIGHLIGHT_STYLE, style._name_.lower())

    def set_mathjax(self, version: Text, cfg: Text) -> object:
        assert cfg and cfg in MATHJAX_CONFS, f"unreconginsed MathJax config {cfg}"
        assert (
            version
            and len(version) >= 3
            and version[0] == "2"
            and version[1] == "."
            and str.isdigit(version[2])
        ), f"unrecognised MathJax version {version}"
        return self.set_opt(
            LongOpt.MATHJAX,
            f"https://cdnjs.cloudflare.com/ajax/libs/mathjax/{version}/MathJax.js?config={cfg}",
        )

    def set_exts(self, exts: Iterable[Ext]) -> object:
        for ext in exts:
            self.set_ext(ext)
        return self

    def set_ext(self, ext: Ext) -> object:
        self.exts.append(ext)
        return self

    def set_no_ext(self, ext: Ext) -> object:
        self.no_exts.append(ext)
        return self

    def set_no_exts(self, exts: Iterable[Ext]) -> object:
        for ext in exts:
            self.set_no_ext(ext)
        return self

    @property
    def args(self) -> List[Text]:

        arguments = ["pandoc", "--from"]

        from_fmt = self.from_fmt._name_.lower()
        if len(self.exts) > 0:
            for ext in self.exts:
                from_fmt += f"+{ext._name_.lower()}"
        if len(self.no_exts) > 0:
            for ext in self.no_exts:
                from_fmt += f"-{ext._name_.lower()}"

        arguments.append(from_fmt)

        arguments.extend(["--to", self.to_fmt._name_.lower()])

        for opt in self.long_opts.keys():
            maybe_val: Optional[Text] = self.long_opts[opt]
            opt_name: Text = opt._name_.lower().replace("_", "-")
            if maybe_val:
                arguments.append(f"--{opt_name}={maybe_val}")
            else:
                arguments.append(f"--{opt_name}")
        log.debug(f"args: {arguments}")
        return arguments

    def before(self, text: Text) -> Text:
        """Fix badly formatted markdown where heading marker `#` is not
        followed by space.

        NOTE: This method is pure.

        :param text: input text before transformations
        :return: output text after transformations
        """
        log.debug("preprocessing [before hook]")
        return re.sub(r"(#+)([A-Z])", "\1 \2", text, re.MULTILINE)

    def after(self, text: Text) -> Text:
        """Transform relative links and references, Inject JavaScript.

        NOTE: This method is pure.

        Match on either src or href e.g.:

            `src="./script.js"` and `href="styles.css"`

        skip over whitespace e.g.:

            `src="    address/file.png"`

        match if relative e.g.:

            `./`
        or match if not an external link with a protocol e.g.:

            `https://stackoverflow.com`

        or match if not a valid directory reference e.g.:

            `/srv/log/log.txt` and `~/file.txt`

        :param text: input text
        :return: output after transformations
        """
        pat = re.compile(r'(href|src)="\s*(\./|(?![a-z]{2,10}://|~|\#|/))')
        d: Text = dirname(self.input_file)
        with open(self.javascript) as f:
            log.debug("postprocessing [after hook]")
            return re.sub(pat, f'\\1="{d}/', text).replace(
                "</body>", f"<script>{f.read()}</script></body>"
            )

    def execute(self) -> Text:
        log.debug("executing")
        with open(self.input_file, encoding="utf-8") as input:
            return self.after(
                run(
                    self.args,
                    encoding="utf-8",
                    input=self.before(input.read()),
                    stderr=DEVNULL,
                    stdout=PIPE,
                ).stdout
            )


if __name__ == "__main__":

    INPUT_FILE = sys.argv[1]

    log.debug(f"input file: {INPUT_FILE}")

    OUTPUT_FILE: Text = os.path.join(
        "/tmp/vim",
        basename(dirname(INPUT_FILE)),
        re.sub(
            r"^(.*)\.(?:r?md|m(?:ark)?down)$",
            r"\1.html",
            basename(INPUT_FILE),
            re.IGNORECASE | re.MULTILINE,
        ),
    )

    log.debug(f"output file: {OUTPUT_FILE}")

    ensure_exists(OUTPUT_FILE)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as output:
        cmd = PandocCmd(INPUT_FILE)
        output.write(cmd.execute())
        print(f"Cmd: {' '.join(cmd.args)}")
        print(f'Output: {output.name}')

# vim:foldmethod=manual:
