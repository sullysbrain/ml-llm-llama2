from transformers import AutoTokenizer, pipeline
import torch

model = "tiiuae/falcon-7b-instruct"
tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
)
newline_token = tokenizer.encode("\n")[0]
my_name = "Alice"
your_name = "Bob"
dialog = []

while True:
    user_input = input("> ")
    dialog.append(f"{my_name}: {user_input}")
    prompt = "\n".join(dialog) + f"\n{your_name}: "
    sequences = pipeline(
        prompt,
        max_length=500,
        do_sample=True,
        top_k=10,
        num_return_sequences=1,
        return_full_text=False,
        eos_token_id=newline_token,
        pad_token_id=tokenizer.eos_token_id,
    )
    print(sequences[0]['generated_text'])
    dialog.append("Bob: "+sequences[0]['generated_text'])