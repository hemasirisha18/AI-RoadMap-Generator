from django.shortcuts import render

# local imports
from app.pipeline import *

def home(request):
    return render(request, 'app/index.html')

def generate(request):
    if request.POST:
        prompt = request.POST['prompt_msg']
        base_prompt = getPrompt(prompt)
        data = eval(get_completion(base_prompt))
        # data = returnSampleTree()
        print(type(data))
        print(data)
        root_node = next(node for node in data['roadmap'] if node['parent'] == 0)
        tree_html = generate_tree(root_node, data)
        bootstrap_timeline = f"{tree_html}".replace('\#', '#')
        bootstrap_timeline = "<ul>" + bootstrap_timeline + "</ul>"
        context = {'roadmap_title': root_node['title'], 'roadmap_html': bootstrap_timeline}
        return render(request, 'app/index.html/', context)
    return render(request, 'app/index.html')