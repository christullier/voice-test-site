import html, re, sys

src, dst, title = sys.argv[1], sys.argv[2], sys.argv[3]
lines = open(src, encoding="utf-8").read().splitlines()

def inline(s):
    s = html.escape(s, quote=False)
    return re.sub(r"(https?://[^\s)]+)", r'<a href="\1">\1</a>', s)

body, in_list = [], False
for i, line in enumerate(lines):
    s = line.strip()
    if i == 0:
        continue  # the first line is the document title
    if s.startswith("- "):
        if not in_list:
            body.append("<ul>"); in_list = True
        body.append(f"<li>{inline(s[2:])}</li>")
        continue
    if in_list:
        body.append("</ul>"); in_list = False
    if not s:
        continue
    if re.match(r"^\d+\. ", s):
        body.append(f"<h2>{inline(s)}</h2>")
    elif s.startswith("Last updated:"):
        body.append(f'<p class="meta">{inline(s)}</p>')
    else:
        body.append(f"<p>{inline(s)}</p>")
if in_list:
    body.append("</ul>")

page = open(sys.argv[4], encoding="utf-8").read()
page = page.replace("{{TITLE}}", html.escape(title)).replace("{{BODY}}", "\n".join(body))
open(dst, "w", encoding="utf-8").write(page)
