<section id="skills">

<div class="container">

<h2>Skills</h2>

{% for skill in skills %}

<p>{{ skill.name }}</p>

<div class="progress">

<div
class="progress-bar"
style="width: {{ skill.percentage }}%;">

{{ skill.percentage }}%

</div>

</div>

{% endfor %}

</div>

</section>