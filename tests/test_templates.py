from python_boilerplate.templates.template_with_jinja2 import render


def test_render() -> None:
    assert (
        render("template1.j2")
        == """\
This is template 1

Variable: This is the test variable

Function: The test functions says: hello"""
    )
