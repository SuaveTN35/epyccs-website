# EPYCCS.com DNS Configuration Guide

## Domain Registrar: Squarespace

## Required DNS Records for GitHub Pages

### A Records (Root Domain)
| Type | Host | Value |
|------|------|-------|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |

### CNAME Record (WWW Subdomain)
| Type | Host | Value |
|------|------|-------|
| CNAME | www | suavetn35.github.io |

## Setup Steps

1. Log into Squarespace → Settings → Domains → epyccs.com
2. Go to DNS Settings
3. Remove existing A/CNAME records pointing to Squarespace
4. Add the 4 A records above
5. Add the CNAME record above
6. Save changes
7. Wait 15-30 minutes for DNS propagation
8. Go to GitHub: https://github.com/SuaveTN35/epyccs-website/settings/pages
9. Check "Enforce HTTPS" (will be available after DNS propagates)

## Verification

Test DNS propagation:
```bash
dig epyccs.com +short
# Should return GitHub IPs: 185.199.108.153, etc.

dig www.epyccs.com +short
# Should return: suavetn35.github.io
```

## GitHub Pages Configuration
- Repository: SuaveTN35/epyccs-website
- Branch: main
- Folder: /docs
- Custom domain: epyccs.com

## Troubleshooting

If SSL certificate doesn't provision:
1. Remove custom domain in GitHub Pages settings
2. Wait 5 minutes
3. Re-add epyccs.com as custom domain
4. GitHub will re-attempt certificate provisioning
