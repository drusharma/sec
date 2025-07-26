<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Policy Form</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container mt-5">
        <h2 class="mb-4">{{ 'Edit' if form.policy_no.data else 'Add' }} Policy</h2>
        <form method="POST">
            {{ form.hidden_tag() }}
            <div class="mb-3">
                {{ form.business_lines.label(class="form-label") }}
                {{ form.business_lines(class="form-control") }}
                {% if form.business_lines.errors %}
                    <div class="text-danger">{{ form.business_lines.errors[0] }}</div>
                {% endif %}
            </div>
            <div class="mb-3">
                {{ form.policy_no.label(class="form-label") }}
                {{ form.policy_no(class="form-control") }}
                {% if form.policy_no.errors %}
                    <div class="text-danger">{{ form.policy_no.errors[0] }}</div>
                {% endif %}
            </div>
            <div class="mb-3">
                {{ form.effective_date.label(class="form-label") }}
                {{ form.effective_date(class="form-control") }}
                {% if form.effective_date.errors %}
                    <div class="text-danger">{{ form.effective_date.errors[0] }}</div>
                {% endif %}
            </div>
            <div class="mb-3">
                {{ form.expiration_date.label(class="form-label") }}
                {{ form.expiration_date(class="form-control") }}
                {% if form.expiration_date.errors %}
                    <div class="text-danger">{{ form.expiration_date.errors[0] }}</div>
                {% endif %}
            </div>
            {{ form.applicants_id(type="hidden") }}
            <button type="submit" class="btn btn-primary">Save Policy</button>
            <a href="{{ url_for('index') }}" class="btn btn-secondary">Cancel</a>
        </form>
    </div>
</body>
</html>
