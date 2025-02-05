from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
from qwen_vl_utils import process_vision_info
from PIL import Image


model = Qwen2VLForConditionalGeneration.from_pretrained(
    "Qwen/Qwen2-VL-2B-Instruct", torch_dtype="auto", device_map="auto"
)

processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-2B-Instruct")

# Replace with your local image path
image_path = 'images.jpeg'  
# Load the image from the local path using PIL
image = Image.open(image_path).convert("RGB")

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "image": image,
            },
            {"type": "text", "text": "Extract the text from the image."},
        ],
    }
]

text = processor.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)
image_inputs, video_inputs = process_vision_info(messages)
inputs = processor(
    text=[text],
    images=image_inputs,
    videos=video_inputs,
    padding=True,
    return_tensors="pt",
)
inputs = inputs.to("cuda")


generated_ids = model.generate(**inputs, max_new_tokens=128)
generated_ids_trimmed = [
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
output_text = processor.batch_decode(
    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
)

print("Extracted Text:", output_text)

cleaned_output = output_text[0].replace('\n', ' ').strip()

print("Extracted Text:", cleaned_output)

from gtts import gTTS
import os

text = cleaned_output 

# Convert text to speech
tts = gTTS(text=text, lang='en')

# Save the audio file
tts.save("output.mp3")

os.system("start output.mp3")
