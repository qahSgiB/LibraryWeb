from pyPage.Template import templatePath



def render(getData=None, postData=None):
    html = None
    with open(templatePath('main.html'), 'r') as htmlFile:
        html = htmlFile.read()

    is_ = [f'<p>i: {i}</p>' for i in range(5)]
    is_ = ''.join(is_)

    context = {
        'is': is_
    }

    return html.format(**context)
