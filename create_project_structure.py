import os

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

def create_file(path, content=""):
    with open(path, 'w') as f:
        f.write(content)
    print(f"Created file: {path}")

def create_project_structure():
    base_path = os.getcwd()
    
    # 创建子文件夹
    folders = [
        'data/raw',
        'data/processed',
        'data/external',
        'notebooks/exploratory',
        'notebooks/final',
        'src/data',
        'src/features',
        'src/models',
        'src/visualization',
        'tests',
        'docs',
        'results/figures',
        'results/models'
    ]

    for folder in folders:
        create_directory(os.path.join(base_path, folder))

    # 创建基本文件
    create_file(os.path.join(base_path, 'requirements.txt'))
    create_file(os.path.join(base_path, 'setup.py'))
    # create_file(os.path.join(base_path, 'README.md'), f"# {os.path.basename(base_path)}\n\nProject description goes here.")
    # create_file(os.path.join(base_path, '.gitignore'), "# Python\n__pycache__/\n*.py[cod]\n\n# Notebooks\n.ipynb_checkpoints\n\n# Virtual environment\nvenv/\nenv/\n")

if __name__ == "__main__":
    create_project_structure()
    print(f"Project structure has been created in the current directory.")