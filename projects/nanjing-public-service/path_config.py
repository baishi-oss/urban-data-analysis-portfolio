"""公开项目的路径和环境变量配置示例。

所有文件路径都从当前文件所在目录推导，不依赖个人电脑盘符。
真实 API 密钥只允许通过操作系统环境变量提供。
"""

import os
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
FIGURE_DIR = PROJECT_ROOT / "figures"
NOTEBOOK_DIR = PROJECT_ROOT / "notebooks"

ANALYSIS_DATA = DATA_DIR / "analysis_base.csv"


def ensure_output_dirs() -> None:
    """创建可生成的输出目录，不改动输入数据目录。"""
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)


def get_env_key(name: str) -> str:
    """读取环境变量中的 API 密钥；缺失时给出明确提示。"""
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(
            f"未找到环境变量 {name}。请在本机设置，不要把真实密钥写入代码或提交到 Git。"
        )
    return value
