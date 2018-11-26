import re

def convert_file(fin, fout):
	fout.write("{\n")
	space_counter = 0
	old_space_counter = 0
	curly_bracket_counter = 0
	minus_counter = 0
	square_bracket_flag = 0

	for line in fin.readlines():
		space_counter = len(line)-len(line.lstrip())
		match_minus = re.search(r"-", line)

		if match_minus is not None:
			line = line[0:match_minus.start()] + line[match_minus.end()::]
			if (square_bracket_flag == 0):
				fout.write("[\n")
				square_bracket_flag = 1

		if (space_counter > old_space_counter):
			str = " "*space_counter + "{"
			fout.write(str + "\n")
			curly_bracket_counter += 1
		elif (space_counter < old_space_counter):
			str = " "*old_space_counter + "},"
			fout.write(str + "\n")
			curly_bracket_counter -= 1
		old_space_counter = space_counter

		match_str = re.search(r":", line)
		if match_str is not None:
			newline = line [0:space_counter] + "\"" + line[space_counter:match_str.start()] + "\"" + ":"
			if re.search(r":(\s*)\w", line) is not None:
				newline += " \"" + line[(match_str.end()+1):(len(line)-1)] + "\","
			fout.write(newline + "\n")




	if (curly_bracket_counter > 0):
		for i in range(curly_bracket_counter):
			str = " "*old_space_counter + "},"
			fout.write(str + "\n")
			if (old_space_counter >= 4):
				old_space_counter -= 4
	if (square_bracket_flag == 1):
		fout.write("],\n")
	fout.write("};\n")

if  __name__ == "__main__":
	fin = open("Wensday.yml", "r", encoding='UTF-8')
	fout = open("Wensday.json", "w", encoding='UTF-8')
	convert_file(fin, fout)
	fout.close()
	fin.close()
