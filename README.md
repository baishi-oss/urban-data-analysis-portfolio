# 城市数据分析学习与项目作品集

这是一个面向导师和研究合作交流的公开作品集，记录我从 Python 基础练习逐步走向城市更新与空间数据分析的过程。

## 在线浏览

GitHub Pages：<https://baishi-oss.github.io/urban-data-analysis-portfolio/>

## 代表项目

### 南京 2024—2025 年老旧小区周边公共服务分析

以改造名单中的老旧小区为研究对象，围绕 500 米范围内六类公共服务设施，分析区际差异、空间分布、设施结构、圈层衰减和配套盲区。

- [项目代码与分析材料](projects/nanjing-public-service)
- [网页项目说明](https://baishi-oss.github.io/urban-data-analysis-portfolio/projects/nanjing.html)

![南京老旧小区公共服务空间分布](projects/nanjing-public-service/figures/图2_空间分布.png)

### 加州房价探索性数据分析

使用 scikit-learn California Housing 数据集练习异常值检查、特征分布、空间分布、相关性分析和散点图矩阵。

- [项目代码与分析材料](projects/california-housing)
- [网页项目说明](https://baishi-oss.github.io/urban-data-analysis-portfolio/projects/california.html)

![加州房价地理分布](projects/california-housing/figures/03_加州房价地理分布.png)

## 基础学习路径

| 阶段 | 主题 | 主要内容 | 精选成果 |
| --- | --- | --- | --- |
| 第一周 | Python 模块与数据清洗 | 函数、模块拆分、装饰器、字典统计 | [查看](learning/week01-python-basics) |
| 第二周 | JSON 与异常处理 | JSON 读写、累计统计、异常捕获 | [查看](learning/week02-json-io) |
| 第三周 | pandas 数据处理 | 缺失值、重复值、筛选、分组聚合 | [查看](learning/week03-pandas) |
| 第四周 | 数据可视化 | NumPy、Matplotlib、随机游走 | [查看](learning/week04-visualization) |

## 安全与公开范围

- 仓库不包含真实 API 密钥、`.env` 文件、虚拟环境或私人数据。
- Notebook 已清除运行输出和本机绝对路径。
- API 相关代码仅通过环境变量读取密钥，`.env.example` 只提供占位符。
- 原始网页、完整抓取材料和过程性中间文件不在公开范围内。
- 地图平台 POI 数量仅用于学习型探索分析，不替代正式规划调查。

## 本地运行

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

各项目的具体运行方式见对应目录的 README。

## 许可说明

代码可按仓库中的 MIT License 使用。公开数据、项目名称和第三方资料仍遵循其原始来源的许可和引用要求。
