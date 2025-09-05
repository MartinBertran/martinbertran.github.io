Research Interests
======
* Model calibration and uncertianty quantification
* Out of distribution model robustness
* Model auditing for robustness, fairness and privacy



Education
======
* Ph.D in Electrical and Computer Engineering, Duke University, Pratt School of Engineering, 2022
  * Thesis: Robustness and Generalization Under Distribution Shifts. Advisor: Guillermo Sapiro
* B.S. in Electrical Engineering, Universidad de la Republica, Faculty of Engineering, 2015

Professional Experience
======
* Amazon Web Services -- Applied Scientist * 2022 - to date
  * Responsible AI team. Designed evaluation for AWS language and speech models used in service cards on robustness, safety, and fairness. 
  * Developed approaches to measure privacy leakage risks (membership inference attacks) on production models
  * Designed benchmarks to measure privacy and controllability on agentic workflows
  * Developed approaches for efficient hypothesis testing on live models

* Apple -- Machine Learning Research Intern * 2021-2021
  * Interned at the Machine Learning Research Group, working on extracting task-relevant state in Reinforcement Learning.


* Intel AI -- Software Graduate Intern * 2020-2020
  * Graduate internship in Deep Reinforcement Learning in Robotics.

  
Services and Skills
======
* Reviewing: ACL, AISTATS, EMNLP, FAccT, ICLR, ICML, NeurIPS, AAAI
* Teaching: teaching assistant for: Information Theory, graduate level (2019, Duke University), and Random Signals and Noise, graduate level (2018, Duke University)
* Software: Python (Pytorch, Hugging Face, vLLM )

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