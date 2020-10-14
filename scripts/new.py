#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Get info of questions, and create new note for specific question by id

full data parameters as below:
--data-binary $'{"operationName":"questionData","variables":{"titleSlug":"two-sum"},"query":"query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    langToValidPlayground\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    envInfo\n    book {\n      id\n      bookName\n      pressName\n      source\n      shortDescription\n      fullDescription\n      bookImgUrl\n      pressImgUrl\n      productUrl\n      __typename\n    }\n    isSubscribed\n    isDailyQuestion\n    dailyRecordStatus\n    editorType\n    ugcQuestionId\n    style\n    __typename\n  }\n}\n"}'
"""

import requests
import os
import sys
import json
import re

BASE_DIR = sys.path[0]
ROOT_DIR = os.path.split(BASE_DIR)[0]
ALGORITHM_DIR = os.path.join(ROOT_DIR, 'docs/algorithm')
QUESTIONS_FILE = os.path.join(BASE_DIR, 'questions.json')
MKDOCS_FILE = os.path.join(ROOT_DIR, 'mkdocs.yml')


def get_question_by_id(question_id):
    """get question info
    Example of question info:
        {
            "question_id": 1,
            "question__title": "Two Sum",
            "question__title_slug": "two-sum",
            "frontend_question_id": "1",
            "level": 1
        }
    """
    if os.path.exists(QUESTIONS_FILE):
        with open(QUESTIONS_FILE, 'r') as f:
            src = f.read()
    else:
        print(QUESTIONS_FILE + ' not found, please check.')
        sys.exit(1)

    data = json.loads(src)
    questions = data['questions']

    if question_id > len(questions):
        print('quesion_id {} is out of range'.format(question_id))
        sys.exit(1)

    question = questions[question_id - 1]
    if not question_id == question['question_id']:
        print('warning: the question_id is not found in the ' + QUESTIONS_FILE)

    return question


def get_question_info(question):
    question_slug = question['question__title_slug']
    base_url = 'https://leetcode-cn.com/graphql/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
        "content-type": "application/json",
        "referrer": "https://leetcode-cn.com/problems/" + question_slug
    }
    data = {
        "operationName": "questionData",
        "variables": {"titleSlug": question_slug},
        "query": "query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    difficulty\n    hints\n    sampleTestCase\n }\n}\n"
    }
    res = requests.post(base_url, json=data, headers=headers)
    return res.text

def html2md(html):
    """Convert html doc to markdown doc
    replace all matches to related chars.
    """
    rep = {
        '<p>': '', 
        '</p>': '',
        '<strong>': '**',
        '</strong>': '**',
        '&nbsp;': ' ',
        '&gt;': '>',
        '<pre>': '```\n',
        '</pre>': '\n```',
        '<code>': '`',
        '</code>': '`'
        }
    pattern = re.compile('|'.join(rep.keys()))
    md = pattern.sub(lambda m: rep[m.group(0)], html)
    return md

def gen_template(question, question_info):
    """generate template info
    # title

    !!! info ""
        **难度**：简单
        **链接**：<https://leetcode-cn.com/problems/two-sum/>

    ## 描述

    ## 题解
    """
    levels = {
        1: "简单",
        2: "中等",
        3: "困难"
    }
    level = levels.get(question['level'])
    content = html2md(question_info['translatedContent'])
    template = '# {}\n\n'.format(question_info['translatedTitle']) + \
        '!!! info ""\n' + \
        '    **难度**：{}  \n'.format(level) + \
        '    **链接**：<https://leetcode-cn.com/problems/{}/>\n\n'.format(
            question['question__title_slug']) + \
        '## 描述\n\n' + \
        content + \
        '\n## 题解\n\n'

    return template


def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    if not sys.argv[1].isdigit():
        sys.exit(1)
    question_id = int(sys.argv[1])

    question = get_question_by_id(question_id)
    info = get_question_info(question)
    if not info:
        print('get question info fail')
        sys.exit(1)

    question_info = json.loads(info)['data']['question']
    template = gen_template(question, question_info)

    filename = '{}.{}.md'.format(question_id, question['question__title_slug'])
    filepath = os.path.join(ALGORITHM_DIR, filename)
    with open(filepath, 'w') as f:
        print('create new file ' + filepath)
        f.write(template)

    # add item to mkdocs.yml
    with open(MKDOCS_FILE, 'a') as f:
        print('append new file to mkdocs.yml')
        question_item = '    - {}.{}: algorithm/{}\n'.format(
            question_id, question_info['translatedTitle'], filename)
        f.write(question_item)


if __name__ == "__main__":
    main()
