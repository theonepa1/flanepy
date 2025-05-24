import webview
from typing import Callable, Dict

class ApiBridge:
    def __init__(self) -> None:
        self._apis: Dict[str, Callable] = {}

    # register back-end callables
    def register_api(self, name: str, func: Callable) -> None:
        self._apis[name] = func
        print(f"Registered API: {name}")

    # expose everything to the given window
    def expose_all(self, window: webview.Window) -> None:
        for alias, func in self._apis.items():
            if func.__name__ == alias:          # names already match
                window.expose(func)
            else:                               # need a JS-side alias
                def _wrapper(*args, _f=func, **kwargs):
                    return _f(*args, **kwargs)
                _wrapper.__name__ = alias       # set the JS name
                window.expose(_wrapper)
        print("All APIs exposed to JS")

    # optional: allow Python code to call bridge.method()
    def __getattr__(self, name: str) -> Callable:
        try:
            return self._apis[name]
        except KeyError:
            raise AttributeError(f"No API registered with name '{name}'")

    # convenience function you mentioned
    def health_check(self):
        return {"status": "ok"}
