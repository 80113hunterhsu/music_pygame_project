with open('notes.txt') as f:
    lines = f.readlines()

# print(type(lines))

note_list = []
for i in range(len(lines)):
    note_list.append(lines[i].replace("<music21.pitch.Pitch ", "").replace(">,\n", "").replace(">", "").replace(" ", ""))

print(note_list)
# for i in note_list:
#     print(i)

note_type = []
for i in range(len(note_list)):
    if (note_list[i] in note_type):
        continue
    else: 
        note_type.append(note_list[i])

note_type.sort()

# print(note_type)
# for i in note_type:
#     print(i)