from plugin_base import DataTransformer, get_class
import yaml
import sys   

if __name__ == "__main__":
    yaml_file = "extend.yaml"
    if len(sys.argv) > 1:
        yaml_file = sys.argv[1]
        
    with open(yaml_file) as stream:
        config = yaml.safe_load(stream)
    
    hook_list = config["workflow"]

    hooks = [
        get_class(hook_name) for hook_name in hook_list
    ]

    pe = DataTransformer(
        data="hello world",
        hooks=hooks
    )
    
    pe.run()