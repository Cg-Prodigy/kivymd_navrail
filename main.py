from kivy.factory import Factory
from kaki.app import App
from kivymd.app import MDApp


class HotReload(App,MDApp):
    CLASSES={
        'FloatBuild':'app.main_ui'
    }
    KV_FILES=[
        'app/kivy_lang.kv'
    ]
    AUTORELOADER_PATHS=[
        ('.',{'recursive':True})
    ]

    def build_app(self, first):
        return Factory.FloatBuild()

if __name__=='__main__':
    HotReload().run()