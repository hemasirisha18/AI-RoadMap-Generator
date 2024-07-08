import openai

# Set your OpenAI API key
openai.api_key = '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'

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
        max_tokens=1500
    )
    return response.choices[0].message["content"]

def generate_tree(node, data):   # Find all children of the current node
    children = [child for child in data['roadmap'] if child['parent'] == node['id']]
    print("node is", node['title'])
    print("children", children)
    # If there are no children, return a single node
    if not children:
        return '<li><a href="\#" class="ht-tm-element btn btn-outline-primary">'+node['title']+"</a></li>"

    # If there are children, recursively generate the tree for each child
    child_html = ''.join(generate_tree(child, data) for child in children)

    # Return the current node with its children wrapped in a <ul> tag
    return '<li><a href="\#" class="ht-tm-element btn btn-outline-primary">'+node['title']+"</a><ul>"+child_html+"</ul></li>"

def getPrompt(input_prompt):
    base_prompt = """based on my prompt , make up to date roadmap
important response rules :
- collapse response in one line , remove space and new lines 

common rules:
- all should has a parent
- only one root node
- root parent is 0
- root item level should be 0
- no null title
- short and efficient titles
- don't extra description

- response json should be single layer not nested items in items

- choose most related / similar category from here ( based on prompt ):
Software Engineer, Engineer, UPSC, IAS, IPS, Government Jobs
- choose Other Category if you not found right category

- sample response:
{ "category":"...","roadmap:[{"id": 1,"level":1,"parent":5or0,"title":"..."}] }

important items and levels rules:
- minimum 3 levels
- level 1 should has minimum 3 items
- minimum 3 items
- maximum 4 items
- items should be less than 4
- fill only requested fields
- no duplicate subjects

prompt: 
INPUT-TEXT"""
    base_prompt = base_prompt.replace("INPUT-TEXT", input_prompt)
    return base_prompt

def returnSampleTree():
    return {"category":"Software Engineer","roadmap":[{"id":1,"level":0,"parent":0,"title":"Software Engineering Fundamentals"},{"id":2,"level":1,"parent":1,"title":"Programming Languages Basics"},{"id":3,"level":1,"parent":1,"title":"Data Structures and Algorithms"},{"id":4,"level":1,"parent":1,"title":"Object-Oriented Programming"},{"id":5,"level":2,"parent":2,"title":"Python"},{"id":6,"level":2,"parent":2,"title":"Java"},{"id":7,"level":2,"parent":3,"title":"Arrays and Linked Lists"},{"id":8,"level":2,"parent":3,"title":"Sorting and Searching"},{"id":9,"level":2,"parent":4,"title":"Inheritance and Polymorphism"},{"id":10,"level":2,"parent":4,"title":"Design Patterns"},{"id":11,"level":1,"parent":1,"title":"Web Development Basics"},{"id":12,"level":2,"parent":11,"title":"HTML, CSS, and JavaScript"},{"id":13,"level":2,"parent":11,"title":"Front-end Frameworks (e.g., React, Angular)"},{"id":14,"level":2,"parent":11,"title":"Back-end Frameworks (e.g., Node.js, Django)"},{"id":15,"level":1,"parent":1,"title":"Database Management"},{"id":16,"level":2,"parent":15,"title":"SQL Basics"},{"id":17,"level":2,"parent":15,"title":"Database Design"},{"id":18,"level":2,"parent":15,"title":"NoSQL Databases"},{"id":19,"level":1,"parent":1,"title":"Version Control (e.g., Git)"},{"id":20,"level":1,"parent":1,"title":"Software Testing"},{"id":21,"level":2,"parent":20,"title":"Unit Testing"},{"id":22,"level":2,"parent":20,"title":"Integration Testing"},{"id":23,"level":1,"parent":1,"title":"Continuous Integration/Continuous Deployment (CI/CD)"},{"id":24,"level":2,"parent":23,"title":"Jenkins"},{"id":25,"level":2,"parent":23,"title":"Travis CI"}]}