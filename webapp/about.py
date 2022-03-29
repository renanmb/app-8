import justpy as jp
from webapp import layout
# from webapp import page

class About():
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is About page!", classes="text-4xl m2")
        jp.Div(a=div, text=""" 
        potato salad 
        """, classes="text-lg")
        return wp

# jp.Route(About.path, About.serve)
# jp.justpy(port=8001)