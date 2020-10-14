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

## 自动创建文档

使用脚本可以快速获取指定Leetcode ID 的题目描述，并自动生成文件模板，省去网上搜索及初始化描述信息的时间。

```bash
python3 scripts/new.py <question_id>

# example
python3 scripts/new.py 1
```

脚本`new.py`位于GitHub <https://github.com/Litreily/leetcode/blob/master/scripts/new.py>

下面是使用脚本自动生成的文件`1.two-sum.md`，超级方便有木有。

```markdown
# 两数之和

!!! info ""
    **难度**：简单  
    **链接**：<https://leetcode-cn.com/problems/two-sum/>

## 描述

给定一个整数数组 `nums` 和一个目标值 `target`，请你在该数组中找出和为目标值的那 **两个** 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

**示例:**

 ```
 给定 nums = [2, 7, 11, 15], target = 9

 因为 nums[0] + nums[1] = 2 + 7 = 9
 所以返回 [0, 1]
 ```

## 题解
```

## reference

- [wang - leetcode前300道题详解](https://leetcode.wang/)
