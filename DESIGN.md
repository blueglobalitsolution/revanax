# Design System Inspired by ReevanaX

> Auto-extracted from `https://reevanax.com/` on 2026-08-06

## 1. Visual Theme & Atmosphere

Friendly, approachable design with rounded shapes and generous whitespace.

The hero section leads with "Ready for your luxurious & unique experience?".

**Key Characteristics:**
- Roboto as the heading font (custom web font loaded via @font-face)
- Roboto as the body font for all running text
- Heading weight 600, letter-spacing 0.5px
- Light/white background (#ffffff) as the primary canvas
- Primary accent `#be4400` used for CTAs and brand highlights
- 4 shadow level(s) detected — tinted shadows
- Rounded corners (10px+) creating a friendly, approachable feel
- Tags: light, rounded, accented, sans-serif

## 2. Color Palette & Roles

### Primary
- **Primary Accent** (`#be4400`) · `--color-primary`: Brand color, CTA backgrounds, link text, interactive highlights.
- **Secondary Accent** (`#864d26`) · `--color-secondary`: Secondary brand, hover states, complementary highlights.
- **Background** (`#ffffff`) · `--color-bg`: Page background, primary canvas.
- **Background Secondary** (`#fbfbf2`) · `--color-bg-secondary`: Cards, surfaces, alternating sections.

### Text
- **Text Primary** (`#89868d`) · `--color-text`: Headings and body text.
- **Text Secondary** (`#666666`) · `--color-text-secondary`: Muted text, captions, placeholders.

### Borders & Surfaces
- **Border** (`#fbfbf2`) · `--color-border`: Dividers, outlines, input borders.

### Full Extracted Palette

| # | Hex | CSS Variable | Role | Area | Contrast |
|---|---|---|---|---|---|
| 1 | `#864d26` | `--palette-1` | block | large | text-light |
| 2 | `#fbfbf2` | `--palette-2` | section | large | text-dark |
| 3 | `#ceae80` | `--palette-3` | text-accent | large | text-dark |
| 4 | `#1d2327` | `--palette-4` | block | medium | text-light |
| 5 | `#be4400` | `--palette-5` | button | medium | text-light |
| 6 | `#5a321b` | `--palette-6` | text-accent | small | text-light |
| 7 | `#ffffff` | `--palette-7` | badge | small | text-dark |
| 8 | `#1dbe61` | `--palette-8` | badge | small | text-dark |
| 9 | `#66b266` | `--palette-9` | text-accent | small | text-dark |

## 3. Typography Rules

- **Heading Font:** `Roboto` (web font)
- **Body Font:** `Roboto` (web font)

### Type Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|---|---|---|---|---|---|
| H1 | Roboto | 45px | 600 | 45px | 0.5px |
| H2 | Sora | 22px | 500 | 22px | normal |
| H4 | Roboto | 21.112px | 400 | 29.76px | normal |
| Body | -apple-system | 16px | 400 | 24px | normal |

### Type Scale

| Token | Size | Suggested Usage |
|---|---|---|
| Display | `70px` | headings |
| H1 | `50px` | headings |
| H2 | `45px` | headings |
| H3 | `30px` | headings |
| H4 | `25px` | headings |
| Body L | `24px` | body / supporting text |
| Body | `22px` | body / supporting text |
| Small | `21.112px` | body / supporting text |
| XS | `20px` | body / supporting text |
| Caption | `18px` | body / supporting text |

## 4. Component Stylings

### Primary Button

```css
.btn-primary {
  background: transparent;
  color: #c3c4c7;
  border-radius: 0px;
  padding: 0px 0px;
  font-size: 13px;
  font-weight: 400;
  border: none;
  cursor: pointer;
}
```

### Ghost Button

```css
.btn-ghost {
  background: transparent;
  color: #89868d;
  border-radius: 0px;
  padding: 0px 0px;
  font-size: 16px;
  font-weight: 400;
  border: none;
  cursor: pointer;
}
```

### Filled Button

```css
.btn-filled {
  background: #ceae80;
  color: #864d26;
  border-radius: 0px;
  padding: 0px 25px;
  font-size: 17px;
  font-weight: 500;
  border: none;
  cursor: pointer;
}
```

### Filled Button 2

```css
.btn-filled-2 {
  background: #ceae80;
  color: #864d26;
  border-radius: 50px;
  padding: 12px 24px;
  font-size: 25px;
  font-weight: 700;
  border: none;
  cursor: pointer;
}
```

### Filled Button 3

```css
.btn-filled-3 {
  background: #864d26;
  color: #69727d;
  border-radius: 50px;
  padding: 0px 0px;
  font-size: 20px;
  font-weight: 400;
  border: none;
  cursor: pointer;
}
```

### Filled Button 4

```css
.btn-filled-4 {
  background: #25d366;
  color: #ffffff;
  border-radius: 50px;
  padding: 0px 0px;
  font-size: 16px;
  font-weight: 400;
  border: none;
  cursor: pointer;
}
```

## 5. Layout Principles

- **Base spacing unit:** `8px` — use multiples (16px, 24px, 32px, etc.)

### Spacing Scale (extracted from real elements)

| Token | Value | Role |
|---|---|---|
| spacing-1 | `8px` | element |
| spacing-2 | `9.88875px` | element |
| spacing-3 | `10px` | element |
| spacing-4 | `6px` | element |
| spacing-5 | `15px` | element |
| spacing-6 | `30px` | card |
| spacing-7 | `4px` | element |
| spacing-8 | `20px` | element |

### Border Radius Scale

| Token | Value | Element |
|---|---|---|
| radius-button | `10px` | button |
| radius-card | `50px` | card |
| radius-subtle | `3px` | subtle |
| radius-subtle | `5px` | subtle |
| radius-subtle | `4px` | subtle |
| radius-button | `15px` | button |

## 6. Depth & Elevation

| Level | Shadow | Usage |
|---|---|---|
| Mid | `rgba(0, 0, 0, 0.2) 0px 3px 5px 0px` | Dropdowns, popovers |
| Deep | `rgba(0, 0, 0, 0.07) 0px 0px 50px 0px` | Hero sections, deep layers |
| Mid | `rgba(0, 0, 0, 0.2) 0px 2px 5px 0px` | Dropdowns, popovers |
| Low | `rgb(134, 77, 38) 0px 0px 3px 0px` | Cards, subtle elevation |


## 7. Do's and Don'ts

### Do
- Use `#ffffff` as the primary background color
- Use `Roboto` for all headings and `Roboto` for body text
- Use `#be4400` as the single dominant accent/CTA color
- Maintain `8px` as the base spacing unit — all gaps should be multiples
- Use rounded corners (`10px`+) consistently for all interactive elements
- Apply the shadow system for elevation — use the extracted shadow values
- Use weight 600 for headings to match the brand's typographic voice

### Don't
- Don't use colors outside the extracted palette without justification
- Don't substitute Roboto/Roboto with generic alternatives
- Don't use irregular spacing — stick to 8px grid
- Don't use dark/black backgrounds — this is a light-themed design
- Don't use sharp corners — they feel hostile in this rounded design language
- Don't use pure black (#000000) for text — use `#89868d` instead
- Don't add decorative elements not present in the original design — no badges, ribbons, banners, or ornaments unless the source site uses them
- Don't invent UI patterns the source site doesn't have — if the original has no NEW badge, don't add one just because a red is in the palette

## 8. Responsive Behavior

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | < 640px | Single column, stack sections, reduce font sizes ~80% |
| Tablet | 640–1024px | 2-column where appropriate, maintain spacing ratios |
| Desktop | 1024–1440px | Full layout as designed |
| Wide | > 1440px | Max-width container, center content |

- Touch targets: minimum 44×44px on mobile
- Maintain 8px base unit across breakpoints — only scale multipliers

## 9. Agent Prompt Guide

### Quick Color Reference

```
Background:  #ffffff
Text:        #89868d
Accent:      #be4400
Secondary:   #864d26
Border:      #fbfbf2
```

### Example Prompts

1. "Build a hero section with a `#ffffff` background, `Roboto` heading in `#89868d`, and a `#be4400` CTA button with 0px radius."
2. "Create a pricing card using background `#fbfbf2`, border `#fbfbf2`, `Roboto` for text, and 24px padding."
3. "Design a navigation bar — `#ffffff` background, `#89868d` links, `#be4400` for active state."
4. "Build a feature grid with 3 columns, 24px gap, each card using the card component style."
5. "Create a footer with `#89868d` background, `#ffffff` text, and 16px padding."

### Iteration Guide

1. Start with layout structure (sections, grid, spacing)
2. Apply colors from the palette — background first, then text, then accents
3. Set typography — font families, sizes from the type scale, weights
4. Add components — buttons, cards, inputs using the specs above
5. Apply border-radius consistently across all elements
6. Add shadows for depth — use the extracted shadow values, not defaults
7. Check responsive behavior — test mobile and tablet layouts
8. Final pass — verify all colors match, spacing is consistent, fonts are correct

## 10. CSS Custom Properties

> 149 custom properties extracted from `:root` / `html` stylesheets.

### Color Variables

| Variable | Value |
|---|---|
| `--e-a-color-white` | `#fff` |
| `--e-a-color-black` | `#000` |
| `--e-a-color-logo` | `#fff` |
| `--e-a-color-primary` | `#f3bafd` |
| `--e-a-color-primary-bold` | `#d004d4` |
| `--e-a-color-secondary` | `#515962` |
| `--e-a-color-success` | `#0a875a` |
| `--e-a-color-danger` | `#dc2626` |
| `--e-a-color-info` | `#2563eb` |
| `--e-a-color-warning` | `#f59e0b` |
| `--e-a-color-accent` | `#93003f` |
| `--e-a-color-global` | `#1dddbf` |
| `--e-a-color-accent-promotion` | `#93003f` |
| `--e-a-bg-default` | `#fff` |
| `--e-a-bg-invert` | `#0c0d0e` |
| `--e-a-bg-hover` | `#f1f2f3` |
| `--e-a-bg-active` | `#e6e8ea` |
| `--e-a-bg-active-bold` | `#d5d8dc` |
| `--e-a-bg-loading` | `#f9fafa` |
| `--e-a-bg-logo` | `#000` |
| `--e-a-bg-primary` | `#fae8ff` |
| `--e-a-bg-secondary` | `#515962` |
| `--e-a-bg-success` | `#f2fdf5` |
| `--e-a-bg-info` | `#f0f7ff` |
| `--e-a-bg-danger` | `#fef1f4` |
| `--e-a-bg-warning` | `#fffbeb` |
| `--e-a-bg-chip` | `#f1f2f3` |
| `--e-a-color-txt` | `#515962` |
| `--e-a-color-txt-muted` | `#818a96` |
| `--e-a-color-txt-disabled` | `#babfc5` |
| ... | *(73 more)* |

### Spacing Variables

| Variable | Value |
|---|---|
| `--wp-admin--admin-bar--height` | `32px` |
| `--direction-multiplier` | `1` |
| `--e-a-border-radius` | `3px` |
| `--wp-admin-border-width-focus` | `2px` |
| `--wp--preset--aspect-ratio--square` | `1` |
| `--wp--preset--spacing--20` | `0.44rem` |
| `--wp--preset--spacing--30` | `0.67rem` |
| `--wp--preset--spacing--40` | `1rem` |
| `--wp--preset--spacing--50` | `1.5rem` |
| `--wp--preset--spacing--60` | `2.25rem` |
| `--wp--preset--spacing--70` | `3.38rem` |
| `--wp--preset--spacing--80` | `5.06rem` |
| `--width-sidebar` | `320px` |
| `--container-width` | `1191px` |
| `--boxed-offset` | `20px` |
| `--woo-width-sidebar` | `270px` |

### Typography Variables

| Variable | Value |
|---|---|
| `--e-a-font-family` | `Roboto,Arial,Helvetica,sans-serif` |
| `--wp--preset--font-size--small` | `13px` |
| `--wp--preset--font-size--medium` | `20px` |
| `--wp--preset--font-size--large` | `36px` |
| `--wp--preset--font-size--x-large` | `42px` |
| `--primary-font` | `Roboto` |
| `--font-size` | `16px` |
| `--line-height` | `1.86em` |
| `--letter-spacing` | `0px` |
| `--secondary-font` | `Roboto` |

### Other Variables

| Variable | Value |
|---|---|
| `--page-title-display` | `block` |
| `--e-a-border` | `1px solid var(--e-a-border-color)` |
| `--e-a-border-bold` | `1px solid var(--e-a-border-color-bold)` |
| `--e-a-btn-color-invert` | `var(--e-a-color-txt-invert)` |
| `--e-a-btn-color-disabled` | `var(--e-a-color-txt-disabled)` |
| `--e-a-transition-hover` | `all .3s` |
| `--wp-admin-theme-color--rgb` | `56,88,233` |
| `--wp-admin-theme-color-darker-10--rgb` | `33,69,230` |
| `--wp-admin-theme-color-darker-20--rgb` | `24,58,214` |
| `--wp-block-synced-color--rgb` | `122,0,223` |
| `--wp-bound-block-color` | `var(--wp-block-synced-color)` |
| `--wp--preset--aspect-ratio--4-3` | `4/3` |
| `--wp--preset--aspect-ratio--3-4` | `3/4` |
| `--wp--preset--aspect-ratio--3-2` | `3/2` |
| `--wp--preset--aspect-ratio--2-3` | `2/3` |
| ... | *(5 more)* |
