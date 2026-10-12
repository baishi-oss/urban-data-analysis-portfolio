# 第二周：JSON 与异常处理

## 学习目标

- 用 `json.load()` 读取设施记录。
- 遍历数据并累计数量。
- 用 `json.dump()` 输出可读的中文 JSON。
- 捕获文件不存在和 JSON 格式错误。
- 使用 `pathlib` 避免本机绝对路径。

```powershell
python main.py
```

程序读取同目录 `facilities.json`，把统计结果写入 `result.json`。
