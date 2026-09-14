# Yuntao OmniGraffle

用于 macOS OmniGraffle 原生学术绘图的 Claude Code / Codex Skill。根据已有 `.graffle` 示例复用字体、浅色分区和连线风格，交付可编辑图源、矢量 PDF，并检查 LaTeX 中的实际效果。

参考 [yuntao-paper-writing](https://github.com/yuntaolu/yuntao-paper-writing) 的 Skill 组织方式。本仓库只包含通用工作流、样式参数和检查工具，不包含未发表论文或原始研究图片。

## 内容

- `SKILL.md`：触发范围、原生绘图与论文检查流程。
- `references/style.md`：个人学术图形风格和颜色参数。
- `references/native-workflow.md`：已在 OmniGraffle 7.26 验证的控制台、文件授权、绘图和导出步骤。
- `scripts/inspect_graffle.py`：只读检查 ZIP、目录包和 plist 格式图源。
- `agents/openai.yaml`：Codex 的 Skill 显示信息。

## 安装

需要 macOS、OmniGraffle，以及所用助手可访问的本机 Computer Use 工具。Python 检查脚本只使用标准库。私有仓库需要有权限的 GitHub 账号。

以下目标路径须尚不存在；如已存在，先检查本地修改，勿直接覆盖：

```sh
git clone git@github.com:yuntaolu/yuntao-omnigraffle.git ~/Projects/yuntao-omnigraffle
mkdir -p ~/.codex/skills ~/.claude/skills
ln -s ~/Projects/yuntao-omnigraffle ~/.codex/skills/yuntao-omnigraffle
ln -s ~/Projects/yuntao-omnigraffle ~/.claude/skills/yuntao-omnigraffle
```

打开新的 Codex / Claude Code 会话，让其重新发现 Skill。安装文件与当前会话已加载的 Skill 列表是两个状态。

## 使用

Codex：`$yuntao-omnigraffle`；Claude Code：`/yuntao-omnigraffle`，或在任务中直接提到 Skill 名称。

> 使用 yuntao-omnigraffle，将方法章节的流程图重绘为本机 OmniGraffle 图源，参考我指定的三个 graffle 文件。保留所有节点、箭头方向和图例含义，实验统计图不改，保存到 fig/src 并更新论文中的 PDF。

## 检查

```sh
python3 scripts/inspect_graffle.py --self-test
python3 scripts/inspect_graffle.py /path/to/figure.graffle
```

检查脚本只能确认文件结构；绘图完成后仍需在 OmniGraffle 中重新打开，检查实际图形和文字，并编译论文核对最终版式。
