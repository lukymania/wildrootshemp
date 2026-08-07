# Plan: Fix Gallery Issues Round 2

## Issues Identified

### 1. JS Scope (2 pages broken)
- **Wild Relief** (`product-wild-relief.html`): `swapMainImage` defined inside IIFE `(function(){...})();` at line 2777-2787, NOT globally accessible
- **Deep Roots** (`product-deep-roots.html`): `swapMainImage` defined inside IIFE at line 2919-2929, NOT globally accessible
- **Fix**: Change `function swapMainImage(thumb)` → `window.swapMainImage = function(thumb)`
- Other 4 pages: function is in global script scope, works fine

### 2. Deep Rest Mockup Labels (all 3 wrong)
**Actual label from cutout:**
- "WILD ROOTS HEMP" at top
- "THC FREE"
- "DEEP REST NANO-HEMP" (large)
- "EVENING FORMULA"
- "150MG CBN / 150MG NANO-HEMP"
- "30ml | 1oz"
- "MADE IN USA"

**Current mockups show:**
- "DEEP REST Evening Formula 800MG Nano-Hemp + CBN" — WRONG (should be 150MG CBN / 150MG NANO-HEMP)

**Generate 3 new Deep Rest mockups:**
- mockup-deep-rest-bedside-v2.jpg
- mockup-deep-rest-bathtub-v2.jpg  
- mockup-deep-rest-reading-v2.jpg

### 3. Consistent Picture Size
- All pages already use same thumbnail CSS (70px × 70px)
- Daily Roots main image uses `hero-product-img` class with its own sizing
- Need to ensure main product image area stays consistent
