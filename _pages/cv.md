---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* Ph.D in Electrical and Computer Engineering, Duke University, Pratt School of Engineering 2022
  * Thesis: Robustness and Generalization Under Distribution Shifts. Advisor: Guillermo Sapiro
* B.S. in Electrical Engineering, Universidad de la Republica, Faculty of Engineering, 2015

Professional Experience
======
* Amazon Web Services | Applied Scientist * 2022 - to date
  Responsible AI team. Designed evaluation for AWS language and speech models used in service cards on robustness, safety, and fairness. Developed approaches to measure privacy leakage risks (membership inference attacks) on production models

* Apple | Machine Learning Research Intern * 2021
  * Interned at the Machine Learning Research Group, working on extracting task-relevant state in Reinforcement Learning.


* Intel AI | Software Graduate Intern * 2020
  * Graduate internship in Deep Reinforcement Learning in Robotics.

  
Services and Skills
======
* Reviewing: ACL, AISTATS, EMNLP, FAccT, ICLR, ICML, NeurIPS, AAAI
* Teaching: teaching assistant for: Information Theory, graduate level (2019, Duke University), and Random Signals and Noise, graduate level (2018, Duke University)
* Software: Python (Pytorch, Hugging Face, vLLM, )

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
<!-- Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Service and leadership
======
* Currently signed in to 43 different slack teams -->
