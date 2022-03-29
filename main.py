# import inspect
# from webapp import page
import justpy as jp

# import definition
#
from webapp.about import About
from webapp.home import Home
from webapp.dictionary import Dictionary

# imports = list(globals().values())
# print (imports)
# for obj in imports:
#     if inspect.isclass(obj):
#         if issubclass(obj, page.Page) and obj is not page.Page:
#             jp.Route(obj.path, obj.serve)

jp.Route(Home.path, Home.serve)
jp.Route(About.path, About.serve)
jp.Route(Dictionary.path, Dictionary.serve)

jp.justpy(port=8001)