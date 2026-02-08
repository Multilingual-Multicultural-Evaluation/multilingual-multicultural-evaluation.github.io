# %%

import csv

with open("data.csv", "r") as f:
    data = list(csv.DictReader(f))

data.sort(key=lambda x: x["archival"])


print("<ul>")
for paper in [x for x in data if x["archival"] == "Archival"]:
    print(f"""<li><span class="paper_title">{paper['title']}</span>; <span class="paper_authors">{paper['authors']}</span></li>""")
print("</ul><br>Further, we welcome the non-archival presentation of the following works:")
print("<ul>")
for paper in [x for x in data if x["archival"] == "Non-archival"]:
    print(f"""<li><span class="paper_title">{paper['title']}</span>; <span class="paper_authors">{paper['authors']}</span></li>""")
print("</ul>")