import pluggy

HOOK_NAMESPACE = "data_transformer" 
PROJECT_NAME = "data_transformer"

hook_spec = pluggy.HookspecMarker(HOOK_NAMESPACE) 
hook_impl = pluggy.HookimplMarker(HOOK_NAMESPACE)

def get_class(class_name):
    return globals()[class_name]

class DataTransformerSpecs:
    @hook_spec
    def transform(self, data_transformer: 'DataTransformer') -> None:
        pass


class DataTransformer:
    def __init__(self, data="", hooks=None) -> None:
        self._pm = pluggy.PluginManager(PROJECT_NAME)
        self._pm.add_hookspecs(DataTransformerSpecs)
        self.data = data
        hooks.reverse()
        self.hooks = hooks
        if hooks:
            self._register_hooks()

    def _register_hooks(self) -> None:
        for hook in self.hooks:
            self._pm.register(hook)

    def run(self):
        self._pm.hook.transform(data_transformer=self)
        return self.data


class UpperHook:
    @hook_impl
    def transform(data_transformer):
        print("inside UpperHook.transform()")
        data_transformer.data = data_transformer.data.upper()
        print(data_transformer.data)

class LowerHook:
    @hook_impl
    def transform(data_transformer):
        print("inside LowerHook.transform()")
        data_transformer.data = data_transformer.data.lower()
        print(data_transformer.data)

class ReverseHook:
    @hook_impl
    def transform(data_transformer):
        print("inside ReverseHook.transform()")
        data_transformer.data = data_transformer.data[::-1] 
        print(data_transformer.data)

if __name__ == "__main__":
    pe = DataTransformer(
        data="hello world",
        hooks=[
            UpperHook,
        ],
    )
    pe.run()
