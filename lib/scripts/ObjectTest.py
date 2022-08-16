import bpy

farts = bpy.ops.transform.translate(value=(1,0,0))
bpy.ops.transform.rotate(value=30,orient_axis='X')
bpy.ops.transform.resize(value=(2,1,3))
bpy.context.object.location[0] += 5

# def send_string(string):

#     def split_str(s):
#         return [c for c in s]

#     string_list = split_str(string.lower())

#     for c in string_list:
#         if c == '.':
#             kb.send(dot)
#         elif c == '(':
#             kb.send(shift,kb9)
#         elif c == ')':
#             kb.send(shift,kb0)
#         elif c == '_':
#             kb.send(shift,minus)
#         elif c == ' ':
#             kb.send(space)
#         elif c == '=':
#             kb.send(equals)
#         elif c == "'":
#             kb.send(quote)
#         elif c == '-':
#             kb.send(minus)
#         elif c ==',':
#             kb.send(comma)
#         elif c == '0':
#             kb.send(kb0)
#         elif c == '1':
#             kb.send(kb1)
#         elif c == '2':
#             kb.send(kb2)
#         elif c == '3':
#             kb.send(kb3)
#         elif c == '4':
#             kb.send(kb4)
#         else:
#             kb.send(eval(c))