#!/bin/sh
# Regenerate privacy.html and terms.html from the app's bundled legal texts.
set -eu
legal="${1:?usage: tools/build.sh <path to voice-test/Resources/Legal>}"
root="$(cd "$(dirname "$0")/.." && pwd)"
python3 "$root/tools/txt2html.py" "$legal/PrivacyPolicy.txt" "$root/privacy.html" "Privacy Policy" "$root/tools/template.html"
python3 "$root/tools/txt2html.py" "$legal/AppTermsOfUse.txt" "$root/terms.html" "Terms of Use" "$root/tools/template.html"
