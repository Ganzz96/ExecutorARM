import os
from flask import Flask, request, jsonify

UPLOAD_FOLDER  = '/home/pi/context'

app = Flask(__name__)

def save_reg(regs):
	with open(os.path.join(UPLOAD_FOLDER, "context.txt"), "w") as f:
		for reg in regs:
			f.write(str(reg) + '\n')

def save_code(code):
	with open(os.path.join(UPLOAD_FOLDER, "instruction.s"), "w") as f:
		f.write(code)
	

@app.route('/', methods=['POST'])
def upload_files():
	data = request.get_json()
	
	registers = data['registers']
	code = data['code']

	print(request)

	if registers:
		save_reg(registers)
	else:
		return "You should send context", 400

	if code:
		save_code(code)
	else:
		return "You should send instruction", 400

	os.system("python3 readContext.py context/instruction.s context/context.txt")
	os.system("gcc -o test test.s -mfpu=neon")

	os.system("./test > response.txt")

	out_regs = []

	with open("response.txt") as f:
		for line in f:
			out_regs.append(int(line))

	f.close()

	os.system("rm -rf test.s")
	os.system("rm -rf test")
	os.system("rm -rf response.txt")

	return jsonify({"registers": out_regs}), 200

app.run(host='0.0.0.0', port=8080)
