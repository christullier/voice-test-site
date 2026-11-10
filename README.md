# voice-test-site

Privacy policy, terms, and support pages for the MemoHelper iOS app, served with GitHub Pages.

- Privacy Policy: https://christullier.github.io/voice-test-site/privacy.html
- Support: https://christullier.github.io/voice-test-site/support.html
- Terms of Use: https://christullier.github.io/voice-test-site/terms.html

## Update the legal pages

The app bundles the source texts. After you change them in the app, regenerate the pages:

```bash
./tools/build.sh ../voice-test/voice-test/Resources/Legal
```

## Update the screenshots

The home page uses the App Store captures from the app repository. After you make new captures, copy them again:

```bash
for n in journal transcript playing-dark search related importing settings; do
  src=../voice-test/scripts/app-store-screenshots/captures/$n.png
  magick "$src" -resize x1400 /tmp/$n.png
  sips -s format jpeg -s formatOptions 80 /tmp/$n.png --out img/$n.jpg
  cwebp -q 78 -quiet /tmp/$n.png -o img/$n.webp
  avifenc -q 62 -s 4 /tmp/$n.png img/$n.avif
done
```
