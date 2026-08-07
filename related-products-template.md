# Standardized Related Products Template (Daily Roots Style)

## CSS to insert (replace existing related products CSS)
```css
/* ===================== RELATED PRODUCTS ===================== */
.related-products {
  padding: 100px 0;
  background: #ffffff;
}
.related-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
}
.related-card {
  background: #faf8f5;
  border-radius: 12px;
  border: 1px solid rgba(44,44,44,0.1);
  overflow: hidden;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  text-decoration: none;
  display: block;
}
.related-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 40px rgba(0,0,0,0.08);
  border-color: rgba(44,44,44,0.2);
}
.related-card-img {
  height: 220px;
  background: #f5f2ed;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}
.related-card-img img {
  max-height: 180px;
  width: auto;
  transition: transform 0.5s ease;
}
.related-card:hover .related-card-img img { transform: scale(1.05); }
.related-card-badge {
  position: absolute;
  top: 12px;
  left: 12px;
  padding: 4px 10px;
  border-radius: 9999px;
  font-size: 0.65rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}
.related-card-badge.rollon { background: #C17A5F; color: #fff; }
.related-card-badge.spray { background: #9CAF88; color: #fff; }
.related-card-badge.strength { background: #2D4A3E; color: #fff; }
.related-card-badge.evening { background: #7B6BA8; color: #fff; }
.related-card-badge.daily { background: #C8913A; color: #fff; }
.related-card-badge.pet { background: #A67C52; color: #fff; }
.related-card-content { padding: 28px; }
.related-card-content h3 {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 1.15rem;
  font-weight: 600;
  color: #2c2c2c;
  margin-bottom: 6px;
}
.related-card-content .related-desc {
  font-size: 0.8rem;
  color: #6b6b6b;
  margin-bottom: 16px;
}
.related-meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.related-price {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 1.3rem;
  font-weight: 600;
  color: #2c2c2c;
}
.related-btn {
  padding: 8px 20px;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  border: 1.5px solid #9caf88;
  color: #7a8f6a;
  background: transparent;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.related-btn:hover {
  background: #9caf88;
  color: #fff;
}
@media (max-width: 768px) {
  .related-grid { grid-template-columns: 1fr; }
}
```

## HTML structure for each page's 3 cards:

### ROOT RELIEF shows: Spray, Deep Roots, Deep Rest
### WILD RELIEF shows: Deep Roots, Deep Rest, Daily Roots
### DEEP ROOTS shows: Deep Rest, Daily Roots, Spray
### DEEP REST shows: Daily Roots, Spray, Roll-On
### DAILY ROOTS already correct (reference)
### PAW & ROOT shows: Daily Roots, Deep Roots, Spray
