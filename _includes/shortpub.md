
Selected Publications
======
<ul class="cv-pubs">
{%- comment -%}
Grab only items marked selected: true. Fallback if it was written as a string.
{%- endcomment -%}
{%- assign selected_true = site.publications | where: "selected", true -%}
{%- assign selected_str  = site.publications | where: "selected", "true" -%}
{%- assign selected_pubs = selected_true | concat: selected_str | uniq -%}
{%- assign selected_pubs = selected_pubs | sort: "date" | reverse -%}

{%- for post in selected_pubs limit: 200 -%}
  <li>
    <span class="pub-title">{{ post.title }}</span>
    {%- if post.venue %}<span class="pub-venue"> — <i>{{ post.venue }}</i></span>{% endif -%}
    {%- if post.date %}<span class="pub-year">, {{ post.date | date: "%Y" }}</span>{% endif -%}
    {%- if post.paperurl and post.paperurl != "" %} · <a href="{{ post.paperurl }}">Paper</a>{% endif -%}
    {%- if post.bibtexurl and post.bibtexurl != "" %} · <a href="{{ post.bibtexurl }}">BibTeX</a>{% endif -%}
  </li>
{%- endfor -%}
</ul>