# takes params:
# - Root to md
# For creation flag (default):
# - Section (if none, appends to the last)
# - href to task(s)
# For update flag:
# - task number
# - href solutions root (root/number.lang)


# Tasks:
# - info parser from leetcode +
# - md table creator
# - md table parser
# - md table correction

import argparse
from parse_leet import parse_hrefs
from parse_md import mod_md

parser = argparse.ArgumentParser(
    description='Create/Modify your LeetCode table.')
parser.add_argument('-p', '--md-path', default='README.md', type=str)
parser.add_argument('-s', '--md-section', default='', type=str)
parser.add_argument('-hrf', '--question-href', nargs='+', type=str)

args = parser.parse_args()
questions = parse_hrefs(args.question_href)
mod_md(args.md_path, args.md_section, questions)
