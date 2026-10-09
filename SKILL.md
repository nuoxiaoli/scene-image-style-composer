---
name: scene-image-style-composer
description: "Transform an uploaded photograph into one of four scene-grounded visual interpretations: source-aware torn-paper zine collage, ivory ink-study postcard, surreal matte pop collage, or Second World photo narrative poster. Analyze the source's focal point and spatial logic before composing. Use for photo reinterpretation, art direction, image editing, and generation-ready prompts."
---

# Scene Image Style Composer · 场景图像风格转化

Version: 2.0.0 · Language: 中文优先 / English prompts supported

## When to activate

When the user provides a photograph and requests a creative reinterpretation in one of these modes, or asks for a visual transformation prompt:

1. `zine` / `模式1` / `撕纸拼贴` — Scenes Gathered Zine-style source-led collage.
2. `ink-postcard` / `模式2` / `水墨明信片` — ivory matte photo and ink-geometry study.
3. `surreal-pop` / `模式3` / `超现实拼贴` — matte surreal pop collage.
4. `second-world` / `模式4` / `第二世界` — another world discovered inside a photo.

If the user names a mode, follow that mode. Otherwise, choose the mode whose visual mechanism best explains the image and briefly state the choice. If no source photo is supplied, request one instead of inventing photo details. If a user asks for a prompt only, do **not** claim the image was generated.

## Source-first protocol (mandatory)

Before creating a design or prompt:

1. **See the actual uploaded image.** Identify the narrative focal point, visual structure, subject/action, geometry, spatial depth, key color families, directionality, light and potential negative space.
2. Create a compact internal **Scene Card**: `subject / focal point / key geometry / source colors / protected regions / possible reinterpretation / composition constraints`.
3. Define **protected elements**: identity, important objects, physical silhouettes, body pose, original relationships, native colors and lighting according to the selected mode. Do not invent absent scenery.
4. Make the **intervention cause-and-effect** clear: each new visual element must arise from an actual structural detail or original object in the photo.
5. Decide where photography ends, where illustration begins, and why that specific material transition belongs to this particular source image.
6. Apply the selected mode's specific rules, then run `references/quality-gates.md` before output.

### Mode routing

| Mode | Primary mechanism | Canvas | Must preserve | Forbidden shortcut |
|---|---|---|---|---|
| 1 · Zine | Source geometry becomes a torn threshold into a same-scene illustrated field | Source-orientation by default; user ratio wins | Identifiable photographic anchor and original scene logic | Fixed photo coverage, rectangular paste-on, uniform white border |
| 2 · Ink Postcard | Photo above, restrained ink-geometric reinterpretation below | Portrait by default, preferably 3:4 | Top image's subject, layout, native palette, realistic light | Repainting the source top area, busy graphic footer |
| 3 · Surreal Pop | One source-derived giant object distorts scale inside flat shapes | Exactly 3:4 portrait unless overridden | Subject recognition and original subject colors | Multiple giants, gradients, shadows, text |
| 4 · Second World | Source geometry becomes a physically usable alternate reality | Exactly 3:4 portrait; upper/lower 1:1 | Source photo, pose, physical relationships, light and color | Generic torn paper + idle stick figures |

Read the **one** relevant mode file in `references/`:

- `references/mode-1-zine.md`
- `references/mode-2-ink-postcard.md`
- `references/mode-3-surreal-pop.md`
- `references/mode-4-second-world.md`

## How to deliver

**If image editing/generation is available and the user asks to make an image:** use the provided original as the primary reference and generate/edit the image, then add one brief rationale. Do not merely return a prompt in place of the requested picture. If an image tool is unavailable, state that limitation and provide an executable prompt instead.

**If the user asks for prompts / a plan / detailed creative reasoning**, output:

1. `模式` — selected mode and aspect ratio.
2. `画面理解` — focal subject, distinctive source structure, elements to protect.
3. `设计方案` — spatial division, intervention, interaction/edge, materials, typography.
4. `可执行提示词` — ONE specific, cohesive, source-grounded generation/editing prompt.
5. `负面约束` — only the prohibitions relevant to the mode.

Do not invent an exact camera location, subject identity, or unseen details. Avoid generic descriptions like “beautiful scenery” and generic prompts that could apply to every uploaded photo.

## Photo preservation: important technical limitation

Prompt-only image generation cannot guarantee unchanged original pixels. In modes 2 and 4, where the upper photo is required to stay **literally** untouched, prefer a true composite/edit workflow that places an unmodified crop of the source in the upper panel and applies generation only to the lower area. If the available tool cannot do that, say “尽可能忠实保留”, and never falsely promise pixel-identical preservation.

## Exceptions and conflicts

- Explicit user constraints (e.g., `no text`, `no figures`, target aspect ratio) override defaults when feasible; confirm if they fundamentally conflict with a requested mode.
- Mode-specific requirements override generic style preferences. For example, Mode 3's no-text policy does not apply to Mode 2 or Mode 4.
- Do not cross-contaminate modes: no ink-wash in Mode 3; no giant pop-art elements in Mode 4; no black-stick-figure template imposed on Mode 1.
- Respect image rights and privacy. Uploaded photos are never examples to publish to the repository without express approval.
- `scenes-gathered-zine-v1-3` is an external project, **not** a bundled runtime dependency. This Skill implements the user-provided Mode 1 design brief independently; it does not redistribute third-party SKILL files, prompts or art assets. See `NOTICE.md`.

## Quick calls

See `examples/usage-examples.md` for short Chinese invocations, overrides, and a complete prompt-output example.
