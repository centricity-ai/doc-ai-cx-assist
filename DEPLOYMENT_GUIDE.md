# GitHub Pages Deployment Guide

This guide explains how to deploy the AI Chatbot Support Service documentation to GitHub Pages.

## Overview

The documentation site has been completely revamped with:
- **Just the Docs** theme for modern, professional UI
- **Single-page documentation** with sticky sidebar navigation and auto-generated TOC
- **Dark mode** with custom styling optimized for technical documentation
- **Enhanced Mermaid diagrams** with dark theme
- **Full-text search** across all documentation
- **PDF export capability** via print-optimized CSS
- **Mobile-responsive design**
- **Interactive API documentation** with syntax highlighting

## What Changed

### Files Modified
1. **Gemfile** - Upgraded to Jekyll 4.3 and Just the Docs theme
2. **_config.yml** - Complete reconfiguration for Just the Docs with all features enabled
3. **index.md** - Consolidated 4,000+ lines of documentation into a single comprehensive page
4. **_sass/custom/custom.scss** - Custom dark mode styling and enhancements
5. **_sass/custom/print.scss** - PDF export optimization

### Files Added
1. **generate_docs.py** - Python script to regenerate documentation from source files
2. **DEPLOYMENT_GUIDE.md** - This file

### Files Backed Up
- **index.md.backup** - Original index.md before consolidation

## Local Preview (Optional)

If you want to preview the site locally before deploying:

```bash
# Install dependencies
bundle install

# Serve locally (may have Ruby version issues - GitHub Pages will handle this)
bundle exec jekyll serve

# If local serve fails due to Ruby version, don't worry - GitHub Pages uses its own environment
```

**Note**: Local preview may fail due to Ruby 2.6 compatibility issues with google-protobuf. This is fine - GitHub Pages uses Ruby 3.x and will build successfully.

## Deployment to GitHub Pages

### Option 1: Automated GitHub Pages Build (Recommended)

GitHub Pages will automatically build and deploy when you push to the main branch.

**Steps:**

1. **Commit all changes:**
   ```bash
   git add Gemfile _config.yml index.md _sass/ generate_docs.py DEPLOYMENT_GUIDE.md
   git commit -m "docs: revamp GitHub Pages with Just the Docs theme and comprehensive single-page documentation

   - Migrate from Cayman to Just the Docs theme for better navigation
   - Consolidate all documentation into single comprehensive index.md (4,265 lines)
   - Add custom dark mode styling with enhanced code blocks and Mermaid diagrams
   - Enable full-text search, PDF export, and mobile-responsive design
   - Configure complete observability and deployment guides
   - Add Python script for regenerating documentation from source files

   🤖 Generated with Claude Code

   Co-Authored-By: Claude <noreply@anthropic.com>"
   ```

2. **Push to GitHub:**
   ```bash
   git push origin main
   ```

3. **Enable GitHub Pages** (if not already enabled):
   - Go to repository Settings → Pages
   - Source: Deploy from a branch
   - Branch: `main`, folder: `/ (root)`
   - Click "Save"

4. **Wait for deployment** (~2-5 minutes):
   - GitHub Actions will build the site
   - Visit: https://centricity-ai.github.io/doc-ai-cx-assist/

### Option 2: Manual Build (Not Recommended)

If you need to build manually:

```bash
# Build site
bundle exec jekyll build

# Output will be in _site/ directory
# Deploy _site/ contents to your hosting provider
```

## Post-Deployment Verification

After deployment, verify the following:

### ✅ Checklist

- [ ] Site loads at https://centricity-ai.github.io/doc-ai-cx-assist/
- [ ] Dark mode is enabled by default
- [ ] Sidebar navigation appears with all sections
- [ ] Table of Contents is generated and links work
- [ ] Search functionality works (try searching "API" or "MongoDB")
- [ ] Mermaid diagrams render correctly
- [ ] Code blocks have syntax highlighting
- [ ] HTTP method badges display correctly (GET, POST, PUT, DELETE)
- [ ] Mobile view is responsive
- [ ] All anchor links work (click TOC items)
- [ ] "View on GitHub" button works
- [ ] PDF export works (Ctrl/Cmd + P)

## Updating Documentation

To update documentation in the future:

### Option 1: Edit index.md Directly

```bash
# Edit the file
vim index.md  # or use your preferred editor

# Commit and push
git add index.md
git commit -m "docs: update [section name]"
git push origin main
```

### Option 2: Update Source and Regenerate

```bash
# Edit source files
vim README.md  # or backend-doc-files/*.md

# Regenerate index.md
python3 generate_docs.py

# Commit and push
git add README.md index.md
git commit -m "docs: update [section name]"
git push origin main
```

## Troubleshooting

### Issue: GitHub Pages build fails

**Solution:**
1. Check the Actions tab in GitHub for build logs
2. Verify Gemfile syntax is correct
3. Ensure _config.yml YAML is valid
4. Check that all file paths in _config.yml exist

### Issue: Mermaid diagrams don't render

**Solution:**
1. Clear browser cache
2. Verify Mermaid CDN is accessible
3. Check browser console for JavaScript errors
4. Ensure diagram syntax is valid

### Issue: Search doesn't work

**Solution:**
1. Wait for GitHub Pages to fully build (can take up to 10 minutes)
2. Clear browser cache
3. Verify `search_enabled: true` in _config.yml

### Issue: Styling looks broken

**Solution:**
1. Verify _sass/custom/custom.scss was committed
2. Check browser console for CSS loading errors
3. Clear browser cache and hard refresh (Ctrl+Shift+R)

### Issue: PDF export doesn't work

**Solution:**
1. Use browser's print function (Ctrl/Cmd + P)
2. Select "Save as PDF" as the destination
3. Ensure "Background graphics" is enabled in print settings

## Advanced Configuration

### Changing Color Scheme

Edit `_config.yml`:

```yaml
# Options: dark, light, or custom
color_scheme: dark
```

### Adding Logo

1. Add logo image to `assets/images/logo.png`
2. Update `_config.yml`:
   ```yaml
   logo: "/assets/images/logo.png"
   ```

### Customizing Footer

Edit `_config.yml`:

```yaml
footer_content: "Your custom footer text here"
```

### Adding Analytics

Add Google Analytics or other analytics:

```yaml
# _config.yml
ga_tracking: UA-XXXXXXXXX-X
ga_tracking_anonymize_ip: true
```

## Performance Optimization

The site is already optimized for performance:

- ✅ Minimal external dependencies
- ✅ CSS and JS minification (handled by GitHub Pages)
- ✅ Lazy loading for Mermaid diagrams
- ✅ Efficient search indexing
- ✅ Mobile-optimized responsive design

## Maintenance

### Regular Tasks

1. **Update dependencies** (quarterly):
   ```bash
   bundle update
   git add Gemfile.lock
   git commit -m "chore: update dependencies"
   git push
   ```

2. **Regenerate documentation** (when source files change):
   ```bash
   python3 generate_docs.py
   git add index.md
   git commit -m "docs: regenerate documentation"
   git push
   ```

3. **Monitor build status** (check GitHub Actions tab)

## Support

For issues or questions:
- **GitHub Issues**: https://github.com/centricity-ai/doc-ai-cx-assist/issues
- **Just the Docs Documentation**: https://just-the-docs.com/
- **Jekyll Documentation**: https://jekyllrb.com/docs/

---

**Maintained by**: bluntjoint — Rishabh A. | Centricity AI
**Last Updated**: January 14, 2025
