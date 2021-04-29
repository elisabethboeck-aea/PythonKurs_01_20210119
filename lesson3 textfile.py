with open("lesson3_exampletext.txt", "r") as sample_file:    # "r" = read
    content = sample_file.read()
    print(content)

with open("lesson3_exampletext.txt", "r") as sample_file_two:
    content_two = sample_file_two.read().splitlines()

    for line in content_two:
        print(line)

with open("lesson3_newtextfile.txt", "w") as sample_write:
    sample_write.write("Hallo, das ist ein Test :)")
