file = input("enter the file name:")
if file.endswith(".html"):
    print(f"{file} is HTML file")
elif file.endswith(".css"):
    print(f"{file} is CSS file")
elif file.endswith(".js"):
    print(f"{file} is JS file")
elif file.endswith("..py"):
    print(f"{file} is Python file")
elif file.endswith("..md"):
    print(f"{file} is MD file")
elif file.endswith("..png"):
    print(f"{file} is PNG file")
elif file.endswith("..gif"):
    print(f"{file} is GIF file")
else:
    print(f"{file} is unkown file")
# add conditions for .py, .md, .png, .gif, etc 




        