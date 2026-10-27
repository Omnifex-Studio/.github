# Omnifex icon sizes

Pixel-size variants of [omnifex-icon.svg](../omnifex-icon.svg), with the original gold artwork, transparent canvas, and spacing.

SVG files retain the float animation, light sweep, and reduced-motion support. PNG files show the stationary mark.

| Size | Animated SVG | Static PNG |
| --- | --- | --- |
| 16 x 16 px | [SVG](omnifex-icon-16.svg) | [PNG](omnifex-icon-16.png) |
| 24 x 24 px | [SVG](omnifex-icon-24.svg) | [PNG](omnifex-icon-24.png) |
| 32 x 32 px | [SVG](omnifex-icon-32.svg) | [PNG](omnifex-icon-32.png) |
| 48 x 48 px | [SVG](omnifex-icon-48.svg) | [PNG](omnifex-icon-48.png) |
| 64 x 64 px | [SVG](omnifex-icon-64.svg) | [PNG](omnifex-icon-64.png) |
| 128 x 128 px | [SVG](omnifex-icon-128.svg) | [PNG](omnifex-icon-128.png) |
| 256 x 256 px | [SVG](omnifex-icon-256.svg) | [PNG](omnifex-icon-256.png) |
| 512 x 512 px | [SVG](omnifex-icon-512.svg) | [PNG](omnifex-icon-512.png) |
| 1024 x 1024 px | [SVG](omnifex-icon-1024.svg) | [PNG](omnifex-icon-1024.png) |

The source SVG embeds a 460 x 460 PNG. The 512 px and 1024 px variants upscale that artwork. The source's generous spacing is preserved at every size, so the visible mark occupies about 55% of each canvas.

## Usage

From the profile README:

```html
<img src="./assets/icons/omnifex-icon-128.svg" width="128" height="128" alt="Omnifex Studio">
```

Choose a PNG for upload fields or applications that require a raster image. For a 64 px display on a 2x screen, use the 128 px PNG and set its display size to 64 px.

## Regenerate

With Python 3 and Inkscape installed, run from the repository root:

```sh
python3 scripts/export-icon-sizes.py
```

The script reads the original SVG and rewrites all listed variants in this directory. The original SVG remains the source for future exports.
