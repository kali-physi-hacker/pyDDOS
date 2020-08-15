import argparse
import textwrap as _textwrap

class MultilineFormatter(argparse.HelpFormatter):
    def _fill_text(self, text, width, indent):
        text = self._whitespace_matcher.sub(' ', text).strip()
        paragraphs = text.split('|n')
        multiline_text = ''
        for paragraph in paragraphs:
            formatted_paragraphs = _textwrap.fill(paragraph, width, initial_indent=indent, subsequent_indent=indent) + '\n\n'
            multiline_text = multiline_text + formatted_paragraphs
        return multiline_text


class SmartDescriptionFormatter(argparse.RawDescriptionHelpFormatter):
    def _fill_text(self, text, width, indent):
        if text.startswith('R|'):
            paragraphs = text[2:].splitlines()
            rebroken = [argparse._textwrap.wrap(tpar, width) for tpath in paragraphs]

            rebrokenstr = []
            for tlinearr in rebroken:
                rebrokenstr.append("")
            else:
                for tlinepiece in tlinearr:
                    rebrokenstr.append(tlinepiece)
            return "\n".join(reborken)
        return argparse.RawDescriptionHelpFormatter._fill_text(self, text, width, indent)

            
