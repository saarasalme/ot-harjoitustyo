from invoke import task
@task
def start(ctx):
    ctx.run("python3 src/roni_poika.py")

@task
def coverage(ctx):
    ctx.run("coverage run --branch --omit=**/__init__.py,**/game.py,**/snacks.py --source=src/main -m pytest src")

@task(coverage)
def coverageReport(ctx):
    ctx.run("coverage html")

@task
def test(ctx):
    ctx.run("pytest ./src")
    
@task
def lint(ctx):
    ctx.run("pylint src/main")