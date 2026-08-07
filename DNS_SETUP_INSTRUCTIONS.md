# DNS A Record Setup for GitHub Pages SSL

## Problem
Three domains are missing SSL certificates because GitHub Pages cannot verify domain ownership. This causes HTTPS to fail with `ERR_CERT_COMMON_NAME_INVALID`.

## Affected Domains
| Domain | Status | Repo |
|--------|--------|------|
| **thecbdreviewers.com** | No SSL cert | thecbdreviewers |
| **cbdreviewhouse.info** | No SSL cert | cbdreviewhouse-info |
| **nanocbdlab.com** | No SSL cert | nanocbdlab |

## Working Domains (for reference)
| Domain | Status | Repo |
|--------|--------|------|
| cbdreviewhouse.com | SSL OK | cbdreviewhouse |
| nanocbdrankings.com | SSL OK | nanocbdrankings |

---

## DNS Records to Add at Your Domain Registrar

### thecbdreviewers.com

Add these 4 A records pointing the root domain (@) to GitHub Pages:

| Type | Host/Name | Points To | TTL |
|------|-----------|-----------|-----|
| A | @ | 185.199.108.153 | 600 |
| A | @ | 185.199.109.153 | 600 |
| A | @ | 185.199.110.153 | 600 |
| A | @ | 185.199.111.153 | 600 |

### cbdreviewhouse.info

| Type | Host/Name | Points To | TTL |
|------|-----------|-----------|-----|
| A | @ | 185.199.108.153 | 600 |
| A | @ | 185.199.109.153 | 600 |
| A | @ | 185.199.110.153 | 600 |
| A | @ | 185.199.111.153 | 600 |

### nanocbdlab.com

| Type | Host/Name | Points To | TTL |
|------|-----------|-----------|-----|
| A | @ | 185.199.108.153 | 600 |
| A | @ | 185.199.109.153 | 600 |
| A | @ | 185.199.110.153 | 600 |
| A | @ | 185.199.111.153 | 600 |

---

## Step-by-Step Instructions

1. **Log into your domain registrar** (e.g., Namecheap, GoDaddy, Google Domains, Cloudflare, etc.)

2. **Navigate to DNS Management** (may be called "DNS Records", "Advanced DNS", "DNS Settings")

3. **Add the 4 A records** for each of the 3 domains above
   - Use `@` for the Host/Name field (represents the root domain)
   - If your registrar doesn't support `@`, use the full domain name (e.g., `thecbdreviewers.com`) or leave it blank depending on your registrar's convention
   - TTL can be set to "Automatic" or 600 seconds (10 minutes)

4. **Save the changes**

5. **Wait for DNS propagation** (typically 5-60 minutes)

6. **Verify DNS is set correctly** by running this in a terminal:
   ```bash
   dig thecbdreviewers.com +noall +answer -t A
   ```
   You should see 4 lines matching the 4 IP addresses above.

---

## What Happens Next

| Step | Timeline |
|------|----------|
| DNS propagation | 5-60 minutes |
| GitHub Pages detects DNS | Within a few hours |
| SSL certificate provisioned | Up to 24 hours |
| HTTPS enforcement enabled | After certificate exists |

---

## Verification

Once the SSL certificate is provisioned, these URLs should work:

- https://thecbdreviewers.com
- https://cbdreviewhouse.info
- https://nanocbdlab.com

You can check the certificate status by visiting:
- https://github.com/lukymania/thecbdreviewers/settings/pages
- https://github.com/lukymania/cbdreviewhouse-info/settings/pages
- https://github.com/lukymania/nanocbdlab/settings/pages

Look for a green checkmark next to "Enforce HTTPS" in the Pages settings.

---

## Troubleshooting

### If the certificate still doesn't appear after 24 hours:

1. Go to the repo Settings -> Pages on GitHub
2. Remove the custom domain and save
3. Re-add the custom domain and save
4. This forces GitHub to re-check DNS and re-provision the certificate

### If you see "Certificate is being provisioned":

Wait. This is normal. GitHub handles the SSL certificate automatically once DNS is verified. Do not add manual SSL certificates.

---

## GitHub Pages IP Addresses (for reference)

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

These are GitHub's static IPs for Pages. All 4 must be added for proper routing and redundancy.
