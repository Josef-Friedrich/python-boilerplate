from jinja2 import Environment, PackageLoader, select_autoescape

# https://jinja.palletsprojects.com/en/stable/api/#basics


def render(template_name: str) -> str:
    env = Environment(
        loader=PackageLoader("python_boilerplate", "templates"),
        autoescape=select_autoescape(),
    )

    def test_function(msg: str) -> str:
        return f"The test functions says: {msg}"

    env.globals = {
        "test_variable": "This is the test variable",
        "test_function": test_function,
    }
    template = env.get_template(template_name)
    return template.render()
