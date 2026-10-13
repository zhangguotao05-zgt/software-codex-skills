# 纯软件开发 Skills

供 Codex 开发 App、Web、PC、API、数据库与软件服务的独立私有技能仓库。
当前版本 **v1.0.1**，包含一个完整的 `software-development` skill，按任务加载专项指引。

## 能做什么

- 完成功能、定位缺陷、整理架构，落实高内聚、低耦合、简洁高效的代码原则。
- 处理异步生命周期、账号与缓存隔离、接口兼容、事务、迁移、取消和失败恢复。
- 区分开发、联调、生产配置及 Debug/Release；云端条件未齐时继续本地可验证的工作。
- 按实际影响运行检查，复用有效结果，准确记录平台验收、安装升级和发布剩余项。
- 沿用现有项目、技术栈和角色；普通小修改不启动全套团队流程。

它提供执行指导，不安装 Flutter、Node.js、数据库等产品工具链，也不代表项目已经通过验收。

## 安装与使用

在 Codex 中要求：

```text
使用 skill-installer，从 zhangguotao05-zgt/software-codex-skills 安装
skills/software-development，ref 为 main。
```

访问私有仓库需要自己的 GitHub 授权。也可在 Windows 克隆后安装：

```powershell
gh repo clone zhangguotao05-zgt/software-codex-skills
Set-Location software-codex-skills
.\install_skills.ps1 -WhatIf
.\install_skills.ps1
```

安装器只复制本 skill 到用户的 `.agents/skills`，不覆盖已有同名目录，不修改角色或全局配置。
其他系统可将 `skills/software-development` 整个目录复制到 Codex 的用户 skills 目录。
安装后下一轮对话即可使用；已有安装更新时先保留本地修改，再按文件差异同步。

```text
$software-development
继续当前 App 项目，修复账号切换后列表仍显示旧数据的问题，完成受影响验证并提交。
```

```text
$software-development
检查这个 PC 导入模块的职责与耦合，优先处理真实缺陷，再完成有明确收益的精简。
```

## 文件入口

- [SKILL.md](skills/software-development/SKILL.md)：任务识别、执行顺序和完成判断。
- [架构与契约](skills/software-development/references/architecture.md)：模块、数据权威与重构收益。
- [客户端](skills/software-development/references/clients.md)：App、Web、PC 的状态与生命周期。
- [API 与数据](skills/software-development/references/api-data.md)：权限、事务、迁移与后台任务。
- [验证与交付](skills/software-development/references/delivery.md)：环境、调试、验证复用、打包和发布。
- [验证脚本](scripts/validate_skills.py)：本地及 GitHub Actions 使用同一个轻量入口。

## 维护与验证

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe scripts/validate_skills.py
```

CI 检查 UTF-8、YAML 元数据、文件引用、Python 语法、机器路径、生成物和常见凭据特征。
敏感信息检查是有限的模式检查，不代替提交前人工检查。绿色 CI 表示技能打包符合要求，
不表示任何 App、网站或 PC 产品已完成真实运行验收。

按具体使用反馈调整说明，不为每次失败累加全局审批。修改时同步技能版本、相关指引与验证。
本仓库只包含通用指导和维护工具；不上传产品源码、账号、令牌、设备记录或业务日志。
内容为私有内部资料；保存到 GitHub 不授予公开分发许可。
