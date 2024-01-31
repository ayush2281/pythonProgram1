#JSON(JavaScirpt object Noraion).
#its manually used for storing and trasnferring data betwwn the browser and server.
#Json is text, written with java script object notation.
# python too support JSON with built-in package called JSON.
#import JSON
                      # JSON supports mainly 6 data types
                      # 1. string 2. number 3. boolean 4.null 5. obejct 6. array
                      # JSON format exist as a string.
                      # p = '{"name":"WS", "lang":["Python","Java"]}'
import json
d={
    'course_name': 'Python',
    'fees':15000
}
f = json.dumps(d)
print(type(f))
print(f)