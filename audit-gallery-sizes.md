# AUDIT: Gallery Sizing + Volume Sizes

## 1. GALLERY SIZING ISSUE

**Root cause:** Product cutouts are SQUARE (1024x1024, aspect 1:1) but lifestyle mockups are LANDSCAPE (1200x896, aspect 1.34:1). The main image CSS only sets `max-width: 400px; width: 100%` with NO fixed height. So when a thumbnail swaps from a square cutout to a landscape mockup, the container shrinks vertically.

**Fix:** Add `height: 400px; object-fit: contain` to `.checkout-image-main` so all images display in a consistent 400x400px area.

## 2. VOLUME SIZE ISSUES

| Product | Label Says | Checkout Spec | Body Text | Status |
|---------|-----------|---------------|-----------|--------|
| Root Relief | 10ml / 0.34oz | 10ml / 0.34 fl oz ✅ | 10ml ✅ | CORRECT |
| Wild Relief | 30ml / 1oz | **60ml / 2 fl oz ❌** | 30ml ✅ | WRONG |
| Deep Roots | 30ml / 1oz | 30ml / 1 fl oz ✅ | 30ml ✅ | CORRECT |
| Deep Rest | 30ml / 1oz | 30ml / 1 fl oz ✅ | 30ml ✅ | CORRECT |
| Daily Roots | 30ml / 1oz | 30ml / 1 fl oz ✅ | 30ml ✅ | CORRECT |
| Paw & Root | 30ml / 1oz | 30ml / 1 fl oz ✅ | 30ml ✅ | CORRECT |

**Only Wild Relief checkout spec is wrong:** 60ml/2fl oz should be 30ml/1fl oz.
