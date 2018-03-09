import csv
import jinja2


with open("gv.at.csv") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    rows = list(reader)

domains = set(r[2] for r in rows)

filtdomains = set()
for dom in domains:
    if '@' in dom:
        continue
    if dom.startswith("*") and dom[2:] in domains:
        continue
    elif "www." + dom in domains:
        continue
    filtdomains.add(dom)

sortdomains = list(filtdomains)
sortdomains.sort(key=lambda d: tuple(reversed(d.split("."))))

template = jinja2.Template(open("domainlist_tmpl.html").read())
site = template.render(domains=sortdomains)
with open("domainlist.html", "w") as domainlist:
    domainlist.write(site)
