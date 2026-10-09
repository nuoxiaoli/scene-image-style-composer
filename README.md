# Scene Image Style Composer 🎞️

**场景图像风格转化 Skill · v2.0.0**

一个面向图片生成/图片编辑助手的中文优先 Skill：**先读懂照片，再决定怎么设计。** 它把原始照片转化为四种创意视觉表现，并坚持保留原场景的空间关系、主体辨识度和重要色彩线索。

> This repository contains a **text-based creative direction Skill**, not a standalone photo editor or a pretrained image model. Generating the actual picture requires a compatible assistant with image-generation/editing capabilities.

## Four modes / 四种模式

| Mode | 名称 | 主要特点 | 默认画幅 |
|---|---|---|---|
| 1 · `zine` | 同场景撕口拼贴 | 按照片中的水线、树冠、建筑边缘等自然形成撕口；同场景插画衔接摄影，色彩跨界延续 | 优先沿用照片方向 |
| 2 · `ink-postcard` | 哑光米白水墨明信片 | 上半实景保持写实；下半极简淡墨几何重构；底部英文标题与描述 | 竖版，推荐3:4 |
| 3 · `surreal-pop` | 超现实平涂拼贴 | 主体保色、2–3组哑光平涂色块、一个来自照片的唯一巨物、弧形小元素群 | 3:4 |
| 4 · `second-world` | 第二世界摄影二创 | 上半尽可能忠实摄影、下半米白留白；把照片里的真实结构重新理解成可互动的另一世界 | 3:4，上下严格1:1 |

## Quick start / 快速开始

1. 下载本仓库 ZIP 并解压，或克隆仓库。
2. 在支持自定义 Skill 的 AI 助手中导入包含 `SKILL.md` 的文件夹；如果助手没有 Skill 导入功能，可把 `SKILL.md` 和对应的 `references/mode-*.md` 作为自定义规则提供给助手。
3. 上传一张原创或获许可使用的摄影作品，指定 `模式1`、`模式2`、`模式3` 或 `模式4`；也可以交由 Skill 根据照片自动选择。
4. 说「直接出图」或「先给我最终提示词」。图像编辑功能取决于你使用的助手本身。

**示例指令：**

```text
加载 scene-image-style-composer，使用模式4处理我上传的照片。
输出3:4竖版，上下1:1。上半尽可能忠实保留原照，
下半用自然暖米白留白，从原图真实结构推导一个独特的“第二世界”，
小人必须真正参与互动而不是装饰。直接出图。
```

更多用法：[`examples/usage-examples.md`](examples/usage-examples.md)。

## Project structure / 项目结构

```text
scene-image-style-composer/
├── SKILL.md                         # 入口规则与模式路由
├── references/
│   ├── mode-1-zine.md               # 模式1
│   ├── mode-2-ink-postcard.md       # 模式2
│   ├── mode-3-surreal-pop.md        # 模式3
│   ├── mode-4-second-world.md       # 模式4
│   └── quality-gates.md             # 全模式审查清单
├── examples/
│   └── usage-examples.md            # 调用案例
├── scripts/
│   └── validate_skill.py            # 基础静态完整性检查
├── .github/workflows/
│   └── validate.yml                 # Pull Request 检查
├── README.md
├── NOTICE.md
├── CONTRIBUTING.md
├── LICENSE
└── .gitignore
```

## Key principles / 核心原则

- 先识别主体、结构、空间、光线、留白，再决定转化手法。
- 摄影部分是场景真实性的锚，不得凭空重建原本不存在的主体和背景。
- 不强行使用固定尺寸的摄影区，不套统一撕纸贴图模板。
- 装饰元素必须有来源；尤其「第二世界」模式必须有画面因果和物理互动逻辑。
- **准确保留原照像素**不能依赖纯提示词承诺。模式2和4如需“零改动”，应通过合成流程把原图的裁切区域直接放在上半部分，仅在下方区域生成。
- 无论使用何种工具，不上传用户照片到仓库、issue 或示例资料夹，除非明确授权。

## License and attribution / 许可证与来源说明

- 此仓库的独立编写文本及示例以 [MIT License](LICENSE) 开源。
- 模式1的命名和设计方向参考用户给出的 `scenes-gathered-zine-v1-3`；本仓库不含该项目的源文件、参考图或内部资产。**它不是原项目的官方升级版，也不声称获其作者认可。** 详见 [`NOTICE.md`](NOTICE.md)。
- 你的输入照片、第三方素材、字体及图像生成服务的输出可能有独立权利限制，MIT 不会自动覆盖它们。

## Contributing

欢迎提交问题报告和文案改进。请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，尤其不要附带未经许可的摄影作品。
