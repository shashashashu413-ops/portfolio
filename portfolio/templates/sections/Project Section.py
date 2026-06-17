<section id="projects">

<div class="container">

<h2>Projects</h2>

<div class="row">

{% for project in projects %}

<div class="col-md-4">

<div class="card">

<img
src="{{ url_for('static',
filename='images/projects/' + project.image) }}"
class="card-img-top">

<div class="card-body">

<h5>{{ project.title }}</h5>

<p>{{ project.description }}</p>

<a
href="{{ project.github_link }}"
target="_blank"
class="btn btn-dark">

GitHub

</a>

</div>

</div>

</div>

{% endfor %}

</div>

</div>

</section>