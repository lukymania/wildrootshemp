# Wild Roots Hemp - Shopify Theme Setup Guide

## Theme Overview
This is a complete Shopify 2.0 theme for Wild Roots Hemp, a family-founded nano-hemp wellness brand. The theme features the brand's signature sage and forest green color palette with cream backgrounds, section-based homepage editing, and full e-commerce functionality.

## Theme Structure (35 files)

```
wildroots-shopify-theme/
  assets/
    theme.css            - Main stylesheet (brand design system)
    theme.js             - Cart, FAQ, nav, gallery JavaScript
  config/
    settings_schema.json - Theme customization settings
  layout/
    theme.liquid         - Main layout with cart drawer
  locales/
    en.default.json      - Translation strings
  sections/
    announcement-bar.liquid   - Dismissible promo bar
    header.liquid             - Sticky nav with logo, menu, cart
    footer.liquid             - 4-column footer with menus
    hero-banner.liquid        - Homepage hero section
    featured-products.liquid  - Product grid section
    science-spotlight.liquid  - Nano-hemp science section
    family-story.liquid       - Family photo + story section
    testimonials.liquid       - Customer reviews slider
    trust-badges.liquid       - Trust/quality badges
    journal-featured.liquid   - Latest blog posts section
  snippets/
    css-variables.liquid      - Brand color CSS variables
    meta-tags.liquid          - OG, Twitter Card, schema.org JSON-LD
  templates/
    index.liquid              - Homepage (composes 7 sections)
    product.liquid            - Product page with cart, reviews, related
    collection.liquid         - Collection grid with filters
    blog.liquid               - Blog listing ("The Root Journal")
    article.liquid            - Blog post template
    cart.liquid               - Full cart page with checkout
    page.liquid               - Generic page template
    page.our-story.liquid     - Our Story page
    page.the-science.liquid   - The Science page
    page.family.liquid        - Family overview page
    page.family-member.liquid - Individual family member profile
    page.contact.liquid       - Contact page with form
    page.faq.liquid           - FAQ accordion page
    search.liquid             - Search results
    list-collections.liquid   - All collections listing
    customers/login.liquid    - Customer login
    customers/register.liquid - Customer registration
    customers/account.liquid  - Customer account dashboard
  products-import.csv          - Product data for import
```

---

## Step 1: Upload the Theme to Shopify

### Option A: Shopify CLI (recommended for developers)

1. Install Shopify CLI: `npm install -g @shopify/cli`
2. Login: `shopify auth login --store=your-store.myshopify.com`
3. Navigate to theme directory: `cd wildroots-shopify-theme`
4. Push to development theme: `shopify theme push --unpublished`
5. Or push to live: `shopify theme push --live`

### Option B: Shopify Admin (for non-developers)

1. Zip the theme folder (ensure all files are included)
2. In Shopify Admin, go to **Online Store > Themes**
3. Click **Add theme > Upload zip file**
4. Select `wildroots-shopify-theme.zip`
5. Theme will appear in Theme Library

---

## Step 2: Configure Theme Settings

In the theme editor (**Online Store > Customize**):

### Colors (under Theme Settings > Colors)
- **Primary**: #2D4A3E (deep forest green)
- **Accent**: #C17A5F (terra cotta)
- **Background**: #F5F0E8 (cream)
- **Text**: #3D2B1F (dark brown)

### Logo (under Theme Settings > Logo)
- Upload the Wild Roots Hemp logo (transparent PNG)
- The logo from the static site is at `assets/images/wild-roots-circle-logo.png`

### Social Media (under Theme Settings > Social Media)
- Add Instagram, Facebook, Twitter/X, Pinterest URLs

### Typography (under Theme Settings > Typography)
- Headings: Playfair Display (pre-configured)
- Body: Lato (pre-configured)

---

## Step 3: Create Navigation Menus

In Shopify Admin, go to **Online Store > Navigation**:

### Main Menu (`main-menu`)
- Home → /
- Shop → /collections/all
- Our Story → /pages/our-story
- The Science → /pages/the-science
- Family → /pages/family
- Journal → /blogs/news
- Contact → /pages/contact

### Footer Shop Menu (`footer-shop`)
- Daily Roots → /products/daily-roots
- Deep Roots → /products/deep-roots
- Deep Rest → /products/deep-rest
- Root Relief → /products/root-relief
- Wild Relief → /products/wild-relief
- Paw & Root → /products/paw-root

### Footer Company Menu (`footer-company`)
- Our Story → /pages/our-story
- The Science → /pages/the-science
- Family → /pages/family
- Journal → /blogs/news

### Footer Support Menu (`footer-support`)
- FAQ → /pages/faq
- Contact → /pages/contact
- Shipping & Returns → /pages/shipping-returns
- Privacy Policy → /pages/privacy-policy

---

## Step 4: Create Pages

In Shopify Admin, go to **Online Store > Pages > Add page**:

Create each page with the corresponding template:

| Page Title | Template | Content |
|-----------|----------|---------|
| Our Story | page.our-story | Import content from original our-story.html |
| The Science | page.the-science | Import content from original the-science.html |
| Family | page.family | Import content from original family.html |
| FAQ | page.faq | Import content from original faq-contact.html |
| Contact | page.contact | Use Shopify contact form (content auto-generated) |
| Shipping & Returns | page | Create with store policy info |
| Privacy Policy | page | Create with legal text |

For each page, the **Template suffix** dropdown at the bottom right should be set to the matching template.

---

## Step 5: Create Family Member Pages

Create 6 individual pages for family members:

| Page Title | Template | Metafields to set |
|-----------|----------|-------------------|
| Nick | page.family-member | role: Co-Founder, tagline, intro_heading, profile_image, quote, favorite_product |
| Lucy | page.family-member | (same fields) |
| Cole | page.family-member | (same fields) |
| Mia | page.family-member | (same fields) |
| Ava | page.family-member | (same fields) |
| Rocket | page.family-member | (same fields) |

Metafields are configured under **Settings > Custom data > Pages > Add definition**.

---

## Step 6: Import Products

### Option A: CSV Import (recommended)

1. In Shopify Admin, go to **Products > Import**
2. Upload `products-import.csv`
3. Map fields if needed
4. Review and confirm import

### Option B: Manual Creation

Create 6 products matching the CSV data:

| Handle | Title | Price | Type | Tags |
|--------|-------|-------|------|------|
| daily-roots | Daily Roots Standard Strength | $65.00 | Nano-Hemp Tincture | nano-enhanced, tincture, 300mg |
| deep-roots | Deep Roots Extra Strength | $110.00 | Nano-Hemp Tincture | nano-enhanced, tincture, 600mg |
| deep-rest | Deep Rest Evening Formula | $70.00 | Nano-Hemp Sleep Tincture | nano-enhanced, CBN, evening, sleep |
| root-relief | Root Relief Roll-On | $35.00 | Nano-Hemp Topical | nano-enhanced, topical, roll-on, 100mg |
| wild-relief | Wild Relief Botanical Spray | $70.00 | Nano-Hemp Spray | nano-enhanced, spray, 300mg |
| paw-root | Paw & Root Pet Drops | $65.00 | Pet Hemp Tincture | nano-enhanced, pet, tincture, 300mg |

For each product:
- Upload product image
- Set inventory to 100+ units
- Enable "Track quantity"
- Set SKU from CSV
- Add product description from original site
- Add to "All" collection

### Metafields for Products (optional but recommended)

Under **Settings > Custom data > Products**, add:

| Namespace | Key | Type | Description |
|-----------|-----|------|-------------|
| custom | mg_strength | Single line text | "300MG" |
| custom | volume | Single line text | "1 fl oz (30ml)" |
| custom | serving_size | Single line text | "10MG per serving" |
| custom | extract_type | Single line text | "Nano-Enhanced Hemp" |
| custom | servings | Single line text | "30 servings" |
| custom | nano_enhanced | True/False | true |

---

## Step 7: Upload Product Images

For each product, upload these images to Shopify:
- `product-daily-roots.png` (tincture bottle)
- `product-deep-roots.png` (tincture bottle)
- `product-deep-rest.png` (tincture bottle with moon/dark label)
- `product-root-relief.png` (roll-on bottle)
- `product-wild-relief.png` (spray bottle)
- `product-paw-root.png` (pet tincture bottle)

Images should be placed in `Content > Files` or uploaded directly to each product.

---

## Step 8: Create Blog

In Shopify Admin, go to **Online Store > Blog posts > Manage blogs**:

1. Create or rename the default blog to "The Root Journal"
2. The handle should be "news" or "journal"

Then create blog posts by importing content from the original blog files:

| Title | Image | Date |
|-------|-------|------|
| What Is Nano-Hemp? A Complete Guide | blog-nano-guide.jpg | 2026-01-10 |
| Why We Chose Amber Glass | blog-amber-glass.jpg | 2026-01-15 |
| The Truth About Hemp Product Labels | blog-label-checking.jpg | 2026-02-01 |
| Why Less Is More: Our Four-Ingredient Philosophy | blog-four-ingredients.jpg | 2026-02-15 |
| From Heartland to Coastline | blog-heartland-farm.jpg | 2026-03-01 |
| Nano vs. Traditional Hemp | blog-nano-particles.jpg | 2026-03-15 |
| How a Topical Roll-On Can Help Relieve Tension Headaches | blog-headache-watercolor.jpg | 2026-04-01 |
| Can Hemp Help Your Anxious Pet? | blog-pets-hemp.jpg | 2026-07-05 |
| Why Athletes Are Turning to Nano-Hemp for Recovery | blog-athletes-hemp.jpg | 2026-07-12 |
| How to Build an Evening Ritual with Nano-Hemp for Better Rest | blog-sleep-hemp.jpg | 2026-07-19 |

---

## Step 9: Upload Site Images

Upload all brand images to **Content > Files** in Shopify Admin:

**Hero/Brand:**
- hero-landscape.jpg (homepage hero background)

**Our Story:**
- family-cartoon-group.jpg
- nick-lab-partners.png
- nano-science-illustration.jpg
- science-intro-illustration.jpg
- science-skin-barrier-v2.jpg
- science-nanometer-scale.jpg
- nano-fragmentation-encapsulation-process.jpg
- nano-encapsulation-warm.jpg
- root-illustration.jpg

**Family Members:**
- family-mom-tennis.jpg
- family-dad-runner.jpg
- family-son-athlete.jpg
- family-dancer1-ballet.jpg
- family-dancer2-contemporary.jpg
- family-dog-wellness.jpg
- family-surfing-cartoon.jpg

**Blog:**
- blog-nano-guide.jpg, blog-amber-glass.jpg, blog-label-checking.jpg
- blog-four-ingredients.jpg, blog-heartland-farm.jpg, blog-nano-particles.jpg
- blog-headache-watercolor.jpg, blog-pets-hemp.jpg, blog-athletes-hemp.jpg, blog-sleep-hemp.jpg

**Logos:**
- wild-roots-circle-logo.png (footer)
- wild-roots-logo.png (header)

---

## Step 10: Configure Homepage Sections

In the theme editor (**Online Store > Customize**):

### Hero Banner Section
- Background image: hero-landscape.jpg
- Heading: "Where Roots Run Deep"
- Subtitle: "Family-founded nano-hemp wellness"
- Button text: "Shop Now"
- Button link: /collections/all

### Featured Products Section
- Collection: All
- Products to show: 6

### Science Spotlight Section
- Heading: "What Makes Nano-Hemp Different?"
- Comparison image: nano-science-illustration.jpg
- Stats: <100nm, 3-8x, 4 ingredients

### Family Story Section
- Image: family-cartoon-group.jpg
- Text: Import from family.html
- Button: "Meet Our Family" → /pages/family

### Testimonials Section
- Add testimonial blocks with real customer quotes

### Trust Badges Section
- Pre-configured with 4 badges

### Journal Featured Section
- Blog: The Root Journal
- Posts to show: 3

---

## Step 11: Configure Store Settings

### Store Details
- **Store name**: Wild Roots Hemp
- **Store email**: info@wildrootshemp.com
- **Store description**: Family-founded science-backed nano-hemp wellness company with Midwest roots and West Coast wild.

### Payments
- Enable Shopify Payments or Stripe
- Set up credit card processing

### Shipping
- Set up shipping zones (US domestic)
- Add free shipping over $75 rule
- Set flat rate or calculated shipping

### Taxes
- Configure US tax settings
- Set tax rates for states where you have nexus

### Domains
- Add custom domain: wildrootshemp.com
- Set as primary domain

---

## Step 12: Redirect Old URLs (if migrating from existing site)

In Shopify Admin, go to **Online Store > Navigation > URL Redirects**:

Add redirects for any changed URLs:

| From | To |
|------|-----|
| /product-daily-roots.html | /products/daily-roots |
| /product-deep-rest.html | /products/deep-rest |
| /product-deep-roots.html | /products/deep-roots |
| /product-root-relief.html | /products/root-relief |
| /product-wild-relief.html | /products/wild-relief |
| /product-paw-root.html | /products/paw-root |
| /our-story.html | /pages/our-story |
| /the-science.html | /pages/the-science |
| /family.html | /pages/family |
| /contact.html | /pages/contact |
| /faq-contact.html | /pages/faq |
| /journal.html | /blogs/news |

---

## Step 13: Test Before Launch

### Critical Tests
- [ ] All navigation links work
- [ ] Product pages load correctly
- [ ] Add to cart works
- [ ] Cart drawer opens and shows items
- [ ] Checkout process completes
- [ ] Contact form sends emails
- [ ] Blog posts display correctly
- [ ] Mobile responsive on iPhone + Android
- [ ] Tablet layout works
- [ ] Footer links work
- [ ] Social media links open correctly
- [ ] Search functionality works

### SEO Tests
- [ ] Page titles are unique per page
- [ ] Meta descriptions are present
- [ ] Canonical URLs are correct
- [ ] OG tags render in Facebook debugger
- [ ] Twitter cards render correctly
- [ ] Schema.org validates in Google's Rich Results Test
- [ ] Sitemap.xml is accessible at /sitemap.xml

---

## Step 14: Launch

1. Remove password protection (Online Store > Preferences)
2. Set theme as live (Online Store > Themes > Publish)
3. Announce launch

---

## Ongoing Maintenance

- Update product inventory regularly
- Add new blog posts to the Journal
- Monitor customer reviews
- Update the announcement bar for promotions
- Track analytics in Shopify Admin
- Update lastmod in sitemap when content changes

---

## Support

For questions about this theme:
1. Check Shopify documentation: https://help.shopify.com
2. Review Liquid reference: https://shopify.dev/docs/api/liquid
3. Test schema markup: https://search.google.com/test/rich-results

---

## Files Included
- **35 theme files** - Complete Shopify 2.0 theme
- **products-import.csv** - 6 products ready for import
- **SETUP-GUIDE.md** - This guide
