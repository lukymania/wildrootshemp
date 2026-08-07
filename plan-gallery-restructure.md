# Plan: Restructure Product Pages with Clickable Image Galleries

## Phase 1: Generate Corrected Mockup Images

### Wild Relief (3 new images - brown bottles, no floating)
- mockup-wild-relief-tennis-v2.jpg: Brown amber spray bottle on tennis bench
- mockup-wild-relief-vanity-v2.jpg: Brown amber spray bottle on bathroom vanity
- mockup-wild-relief-gym-v2.jpg: Brown amber spray bottle on gym bench (NOT floating by bag)

### Root Relief Roll-On (2 new images - cap off showing roller ball)
- mockup-root-relief-roller-bedside.jpg: Cap OFF showing roller ball on nightstand
- mockup-root-relief-roller-gym.jpg: Cap OFF showing roller ball on gym bench

## Phase 2: Update All 6 Product Pages

### New Structure (each product page checkout section):
```
<div class="checkout-inner">
  <div class="checkout-image-wrap">
    <!-- Main product image (changes when thumbnail clicked) -->
    <img id="mainProductImage" src="primary-cutout.png" class="checkout-image-main">
    
    <!-- Thumbnail gallery below main image -->
    <div class="product-thumbnails">
      <img src="primary-cutout.png" onclick="swapMainImage(this)" class="thumb active">
      <img src="mockup-1.jpg" onclick="swapMainImage(this)" class="thumb">
      <img src="mockup-2.jpg" onclick="swapMainImage(this)" class="thumb">
      <img src="mockup-3.jpg" onclick="swapMainImage(this)" class="thumb">
    </div>
  </div>
  <div class="checkout-content">...</div>
</div>
```

### Remove from Roll-On:
- Remove .image-hover-swap CSS and HTML
- Remove hover hint text
- Integrate cap-off image as a gallery thumbnail

### CSS needed for thumbnail gallery:
```css
.product-thumbnails {
  display: flex;
  gap: 0.75rem;
  justify-content: center;
  margin-top: 1.5rem;
}
.product-thumbnails .thumb {
  width: 70px;
  height: 70px;
  object-fit: cover;
  border-radius: 8px;
  border: 2px solid transparent;
  cursor: pointer;
  transition: all 0.3s ease;
  opacity: 0.7;
}
.product-thumbnails .thumb:hover,
.product-thumbnails .thumb.active {
  border-color: var(--terra-cotta);
  opacity: 1;
  transform: scale(1.05);
}
```

### JavaScript for image swapping:
```javascript
function swapMainImage(thumb) {
  var main = document.getElementById('mainProductImage');
  if (main && thumb.src) {
    main.src = thumb.src;
    main.alt = thumb.alt;
    document.querySelectorAll('.product-thumbnails .thumb').forEach(function(t) {
      t.classList.remove('active');
    });
    thumb.classList.add('active');
  }
}
```

## Phase 3: Deploy
- Commit all changes
- Push to GitHub Pages
