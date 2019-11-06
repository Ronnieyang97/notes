test = '1234e'
print(test.isdigit())


<div class="container">
{% for message in get_flashed_messages() %}
    <div class="alert alert-warning">
    <button type="button" class="close" data-dismiss="alert">&times;</button>
    {{ message }}

    </div>
{% endfor %}