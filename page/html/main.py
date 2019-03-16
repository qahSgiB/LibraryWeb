from pyPage.Template import Template



def render(getData=None, postData=None):
    template = Template.load('main/main.html')

    context = {}
    return template.format(context)
