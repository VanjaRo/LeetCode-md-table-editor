from typing import Dict, List

# Main:
# Add to the existing group +
# Create group
# Add to the new group
# Change status of existing

# Additional :
# Sort by id the group
# Sort by difficuly


HEADER = """| Status  |  #  |                               Title                               | **Difficulty** |                                    Solution                                    |
| :-----: | :-: | :---------------------------------------------------------------: | :------------: | :----------------------------------------------------------------------------: |"""


def get_table_el(info: Dict[str, str]) -> str:
    q_id = info["id"]
    q_href = info["href"]
    q_title = info["title"]
    q_diff = info["difficulty"]

    # modifing existing
    q_sol_rep = "none"
    q_sol_lang = ""
    if "solution_rep" in info and "solution_lang" in info:
        q_sol_rep = info["solution_rep"]
        q_sol_lang = info["solution_lang"]

    ret = f"| &#9744; |  {q_id}  | [{q_title}]({q_href}) |    **{q_diff}**    | {q_sol_rep + q_sol_lang} |\n"

    return ret


def srch_el(lines: List[str], head_title: str) -> int:
    i = 0
    if head_title == "":
        return -1
    else:
        # Searching for specific title to modify a task
        curr_title = ""
        right_title = False
        free_lines = 0

        for line in lines:
            if len(line) == 1 and right_title:
                if free_lines == 1:
                    break
                free_lines += 1
            elif len(line) > 1 and line[:2] == "##":
                ln_els = line.split()
                title_tag = ln_els[1]
                if title_tag == "Title:":
                    curr_title = ln_els[2]
                    if curr_title.lower() == head_title.lower():
                        right_title = True
            i += 1
    return i


def mod_md(root: str, info: List[Dict[str, str]]) -> None:
    for el in info:
        f = open(root, "r")
        lines = f.readlines()

        table_el = get_table_el(el)

        head_title = ""
        if "head" in el:
            head_title = el["head"]

        i = srch_el(lines, head_title)

        # lines = lines[:i] + [table_el] + lines[i:]
        if i == -1:
            lines = lines[:] + [table_el]
        else:
            lines = lines[:i] + [table_el] + lines[i:]

        f.close()
        f = open(root, "w")
        f.writelines(lines)
        f.close()


if __name__ == '__main__':
    f = open("tmp.txt", "w")
    f.writelines(["str"])
