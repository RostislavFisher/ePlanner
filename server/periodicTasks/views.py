from periodicTasks import app
# from server.settings import app

@app.task
def test(arg):
    print(arg)
