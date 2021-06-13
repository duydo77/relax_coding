import re
eng_vn_dict = {'I':'Tôi', 'love':'yêu', 'dog':'chó'}

# vi = input().lower().split()
vi = 'Tôi yêu cô ấy.'
end = ''
if vi[-1] == '.':
	end = '.'
	vi = vi[:-1]

vi = vi.lower().split()

key = list(eng_vn_dict.keys())
value = [x.lower() for x in eng_vn_dict.values()]

for i in range(len(vi)):
	if (vi[i] in value):
		vi[i] = key[value.index(vi[i])]
	else:
		vi[i] = 'xxx'

print(' '.join(vi) + end)

# có cách chơi dơ hơn là biến eng_vn_dict thành vn_end_dict :)
