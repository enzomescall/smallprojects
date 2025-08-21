import galai as gal

model = gal.load_model(name = "standard", num_gpus = None)

input_text = "Outlining the basics of linear regression:"

generated_text = model.generate(input_text = input_text,
                                max_length= 256,
                                new_doc = False,
                                top_p = None)

print(generated_text)