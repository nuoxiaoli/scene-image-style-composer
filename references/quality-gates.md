# Quality Gates · 出图前与交付前自检

## A. Every request

- [ ] The supplied photo has actually been inspected; no fabricated subject, color, landmark or human action.
- [ ] One narrative focal point and one dominant visual gesture have been identified.
- [ ] Protected source regions and user constraints are explicit.
- [ ] The intervention is causally linked to a real photographed form; no arbitrary decor.
- [ ] Scene identity, major topology, subject recognition and key perspective remain consistent.
- [ ] Caption, if required, is concise, scene-specific and positioned for composition rather than a fixed template.
- [ ] The answer describes image generation only if an image was actually produced.
- [ ] No user's source photograph, private data or third-party reference asset is added to this repository.

## B. Mode-specific hard checks

### Mode 1 · Zine
- [ ] Photo coverage is decided from the focal scene, not 35% or 50% by default.
- [ ] Torn threshold follows a real contour: shore, crown, architecture, road, light or terrain.
- [ ] Illustrations outside the photo derive exclusively from the same original scene.
- [ ] Color persists at the tear before gradually turning into halftone / dry-brush / silkscreen.
- [ ] One continuous path of hue, shape or motion crosses the material divide.
- [ ] No pasted rectangle, even border or digital-mask appearance.

### Mode 2 · Ink postcard
- [ ] Upper scene is unmodified where a compositing workflow is available; only an intact, proportional crop.
- [ ] Lower area reconstructs all important forms as soft sparse geometries with translucent ink edges.
- [ ] Original palette is carried across without fabricated neon color, clutter or highlights.
- [ ] English title centered near bottom, smaller English subtitle below, ample paper whitespace.
- [ ] Not a scene copy, not a glossy advertisement, not a hard-edge vector poster.

### Mode 3 · Surreal pop
- [ ] 3:4 vertical composition unless user overrides.
- [ ] Source subject is recognizable and maintains original colors.
- [ ] Exactly one exaggerated giant object from the original photograph.
- [ ] Background consists of just 2–3 flat matte irregular shapes with named colors.
- [ ] One graduated arc of source-derived small elements and a few white strokes.
- [ ] No gradients, cast shadows, text or watermark.

### Mode 4 · Second World
- [ ] 3:4 vertical canvas; top and bottom equally tall.
- [ ] Upper real photo unchanged except proportional crop, when compositing allows.
- [ ] Exactly one photo-derived visual mechanism generates the second world.
- [ ] The cut/edge is not generic decoration; it is part of that mechanism.
- [ ] Bottom is largely warm ivory paper, not crowded with objects.
- [ ] 0–3 black-outline figures if and only if physically useful, not decorative.
- [ ] One modest English handwritten caption, unless user says no text.
- [ ] Viewer should feel the reinterpretation was latent in this particular photograph.

## C. Truth-in-editing

A generative model can change original pixels despite instructions. If exact photo fidelity is requested, use deterministic placement of the untouched crop as the preserved panel and constrain any generative editing to the other region. Otherwise label the result as *faithful, not guaranteed pixel-identical*.
