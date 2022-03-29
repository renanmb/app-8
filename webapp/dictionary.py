import justpy as jp
import definition

class Dictionary:
    path = "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Instant Dictionary", classes="text-4xl m2")
        jp.Div(a=div, text="Get the definition ", classes="text-lg")

        input_div = jp.Div(a=div, classes="grid grid-cols-2")
        output_div = jp.Div(a=div, classes="m-2 p-2 text-lg border-2 h-40")

        # input_box will need the attribute outputdiv = output_div to execute the instantaneous changes
        input_box = jp.Input(a=input_div, placeholder="Type in a word here...", outputdiv = output_div,
                 classes="m-2 bg-gray-100 border-2 border-gray-200 rounded w-64 focus:bg-white "
                         "focus:outline-none "
                         "focus:border-purple-500 py-2 px-4")
        input_box.on('input', cls.get_definition)

        # Without the Button it is required an input event
        # jp.Button(a=input_div, text="Get Definition", classes="border-2 text-gray-500",
        #           click=cls.get_definition, outputdiv=output_div, inputbox=input_box)

        jp.Div(a=div, classes="m-2 p-2 text-lg border-2 h-40")

        print(cls,req)

        return wp

# static method is a method inside a class that behaves as a function

    @staticmethod
    def get_definition(widget, msg):
        # defined = definition.Definition(widget.inputbox.value).get()
        defined = definition.Definition(widget.value).get()

        widget.outputdiv.text = "".join(defined)