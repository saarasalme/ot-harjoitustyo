from invoke import task
@task
def start(ctx):
    ctx.run("python3 ./RoniPoika.py")


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")

@task
def test(ctx):
    ctx.run("pytest ./tests/ronipoika_test.py")
