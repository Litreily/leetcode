# LeetCode

!!! summary
    我的 [LeetCode](https://leetcode-cn.com/) 刷题记录

目前主要刷题方向为 **算法** 和 **shell**

## Leetcode 题库

通过浏览器调试工具可以找到leetcode的题库数据。

### 获取题库

- 所有问题：<https://leetcode-cn.com/api/problems/all>

获取到的json文件是经过格式化的ascii字符，中文都被替换成了Unicode，为了方便查阅，需要重新解码保存一下。

```py
# decode.py
import json
import sys

if len(sys.argv) <= 2:
    sys.exit(1)

src = sys.argv[1]
dest = sys.argv[2]

with open(src, 'r') as fin:
    data = json.load(fin)

with open(dest, 'w', encoding='utf-8') as fout:
    json.dump(data, fout, indent=4, ensure_ascii=False)
```

执行以下命令就可以将文件进行格式化，得到正常显示中文的json文件。

```py
python3 decode.py problemset.json problemset_decoded.json
```

### 获取单个题目信息

```bash
curl 'https://leetcode-cn.com/graphql/' \
  -H 'cache-control: no-cache' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36' \
  -H 'content-type: application/json' \
  --data-binary $'{"operationName":"questionData","variables":{"titleSlug":"add-two-numbers"},"query":"query questionData($titleSlug: String\u0021) {\\n  question(titleSlug: $titleSlug) {\\n    questionId\\n    questionFrontendId\\n    title\\n    titleSlug\\n    content\\n    translatedTitle\\n    translatedContent\\n       difficulty\\n    }\\n}\\n"}' \
  -o output.json
```

## reference

- [wang - leetcode前300道题详解](https://leetcode.wang/)
