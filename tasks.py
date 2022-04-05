from invoke import task

@task
def foo(ctx):
    print("bar")

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)
