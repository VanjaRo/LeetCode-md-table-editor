# function should parse the source href, returning list of dictionaries :
# [
#   {"href": ..., "id": ...,  "title": ..., "difficulty": ...},
#   ...,
# ]

# from selenium import webdriver
from requests import post
from typing import Dict, List

# css-101rr4k –– class for info
# css-v3d350  –– title
# css-10o4wqw –– difficulty


def parse_hrefs(hrefs: List[str]) -> List[Dict[str, str]]:
    diff_classes = {
        "css-14oi08n": "Easy",
        "css-dcmtd5": "Medium",
        "css-t42afm": "Hard",
    }
    ret = []

    for href in hrefs:
        title_slug = href.split("/")[-2]
        req_data = {"operationName": "questionData", "variables": {"titleSlug": title_slug}, "query": "query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    langToValidPlayground\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    envInfo\n    libraryUrl\n    __typename\n  }\n}\n"}
        res_data = post('https://leetcode.com/graphql', json=req_data).json()

        q = res_data['data']['question']
        q_id = q["questionId"]
        q_title = title_slug.replace("-", " ")
        q_diff = q["difficulty"]

        ret.append({
            "href": href,
            "id": q_id,
            "title": q_title,
            "difficulty": q_diff,
        })
    return ret


if __name__ == '__main__':
    pass
    # data = {"operationName": "problemsetQuestionList", "variables": {"categorySlug": "", "skip": 0, "limit": 1, "filters": {"searchKeywords": "12"}},
    #         "query": "query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\n  problemsetQuestionList: questionList(\n    categorySlug: $categorySlug\n    limit: $limit\n    skip: $skip\n    filters: $filters\n  ) {\n    total: totalNum\n    questions: data {\n      acRate\n      difficulty\n      freqBar\n      frontendQuestionId: questionFrontendId\n      isFavor\n      paidOnly: isPaidOnly\n      status\n      title\n      titleSlug\n      topicTags {\n        name\n        id\n        slug\n      }\n      hasSolution\n      hasVideoSolution\n    }\n  }\n}\n"}
    # res_data = post('https://leetcode.com/graphql', json=data).json()
    # print(res_data["data"])
    # print(parse_hrefs(["https://leetcode.com/problems/integer-to-roman/"]))
