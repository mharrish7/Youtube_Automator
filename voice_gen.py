from gradio_client import Client, file

import shutil
import os
import time 


def generate(text, client):
	result = client.predict(
			text,	# str in 'Input Prompt' Textbox component
			"\n",	# str in 'Line Delimiter' Textbox component
			"None",	# Literal['Happy', 'Sad', 'Angry', 'Disgusted', 'Arrogant', 'Custom', 'None'] in 'Emotion' Radio component
			"",	# str in 'Custom Emotion' Textbox component
			"male1",	# Literal['beerus', 'daniel', 'eliah', 'geto', 'girl', 'gojo', 'gojo2', 'goku', 'gt', 'harvey', 'leo', 'male1', 'me', 'michal', 'sukuna', 'tom', 'trump', 'will', 'random', 'microphone'] in 'Voice' Dropdown component
			file('https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav'),	# filepath in 'Microphone Source' Audio component
			0,	# float in 'Voice Chunks' Number component
			1,	# float (numeric value between 1 and 6)
				#					in 'Candidates' Slider component
			0,	# float in 'Seed' Number component
			256,	# float (numeric value between 2 and 512)
				#					in 'Samples' Slider component
			200,	# float (numeric value between 0 and 512)
				#					in 'Iterations' Slider component
			0.8,	# float (numeric value between 0 and 1)
				#					in 'Temperature' Slider component
			"DDIM",	# Literal['P', 'DDIM'] in 'Diffusion Samplers' Radio component
			8,	# float (numeric value between 1 and 32)
					#				in 'Pause Size' Slider component
			0,	# float (numeric value between 0 and 1)
					#				in 'CVVP Weight' Slider component
			0.8,	# float (numeric value between 0 and 1)
					#				in 'Top P' Slider component
			1,	# float (numeric value between 0 and 1)
					#				in 'Diffusion Temperature' Slider component
			1,	# float (numeric value between 0 and 8)
					#				in 'Length Penalty' Slider component
			2,	# float (numeric value between 0 and 8)
					#				in 'Repetition Penalty' Slider component
			2,	# float (numeric value between 0 and 4)
					#				in 'Conditioning-Free K' Slider component
			[],	# List[Literal['Half Precision', 'Conditioning-Free']] in 'Experimental Flags' Checkboxgroup component
			False,	# bool in 'Use Original Latents Method (AR)' Checkbox component
			False,	# bool in 'Use Original Latents Method (Diffusion)' Checkbox component
			api_name="/generate"
	)
	return result[0]

def save_file(src_file, dest_path):
	shutil.copy(src_file, dest_path)


def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def voice_main():
	client = Client("http://127.0.0.1:7860/")
	f = open('text.txt')
	text_input = f.read()
	text_input = text_input.replace(':',' ').replace('-',' ').replace('_'," ").replace('!','.').replace('*',"").replace(',','.')
	lines = text_input.strip().split('\n')
	folder_path = "./outputs/audio"
	create_folder_if_not_exists(folder_path)
	sentences = []
	f = open("./outputs/line_by_line.txt","w", encoding="utf-8")
	for line in lines:
		temp = line.strip().split('.')
		for temp_sentence in temp:
			temp_sentence = temp_sentence.strip()
			if temp_sentence != "":
				f.write(temp_sentence + "\n")
				sentences.append(temp_sentence)
	count = 0
	progress = 0
	total_words = len(text_input.split(" "))
	print("Total Words: ", total_words)
	print("*"*25+"STARTING"+"*"*25)
	max_count = len(sentences)
	while count < max_count:
		try:
			sentence = sentences[count]
			result = generate(sentence.strip(), client)
			progress += len(sentence.split(' '))
			save_file(result,folder_path + f"/part{count}.wav")
			print(f"part{count} saved..")
			print(f"Progress: {((progress/total_words)*100):.2f}%")
			count += 1
			time.sleep(0.5)
		except Exception:
			print("Error")
			time.sleep(1)
			continue


def split_words():
	f = open('text.txt')
	text_input = f.read()
	text_input = text_input.replace(':',' ').replace('-',' ').replace('_'," ").replace('!','.').replace('*',"").replace(',','.')
	lines = text_input.strip().split('\n')
	folder_path = "./outputs/audio"
	create_folder_if_not_exists(folder_path)
	f = open("./outputs/line_by_line.txt","w", encoding="utf-8")
	for line in lines:
		temp = line.strip().split('.')
		for temp_sentence in temp:
			temp_sentence = temp_sentence.strip()
			if temp_sentence != "":
				f.write(temp_sentence + "\n")

if __name__ == "__main__":
	voice_main()