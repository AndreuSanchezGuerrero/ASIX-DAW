import random
import string

names = ["Anabel","Ariana","Arielle","Ashley","Audrey","Autumn","Baen","Baethan","Baird","Baldemar","Baldwin","Banan","Banning","Bardaric","Barnom","Barrett","Barrington","Barron","Barry","Barton","Bartram","Basil","Baxter","Bayard","Beacan","Beacher","Beal","Beau","Beauvais","Beck","Benen","Benjamin","Bennett","Benniton","Benoit","Berkeley","Bert","Bertin","Bingham","birche","Blaine","Blair","Blaise","Blake","Booker","Boris","Bradley","Brandon","Brayden","Brett","Brian","Brit","Brock","Keanan","Kearne","Kearney","Keaton","Kedric","Keely","Keith","Kelby","Kelly","Kelvyn","Ken","Kendall","Kenneth","Kent","Kerwin","Kevin","Kimball","Kingston","Kolby","Konrad","Kyle","Kacia","Kaitlyn","Kalista","Karen","Karla","Karisma","Katherine","Katrina","Lafayette","Lamar","Lambart","Lamont","Lance","Lancelot","Landis","Landon","Langdon","Langley","Laramie","Lars","Lasalle","Laughlin","Laurent","Layton","Lawley","Leal","Leander","Lear","Lee","Leigh","Lehman","Harcourt","Harbin","Hardy","Harford","Harlan","Harland","Harmon","Harold","Harris","Hartman","Hartwood","Haslett","Haven","Hawly","Hendrix","Hadley","Hailey","Halle","Hallette","Hannah","Harmony","Harriet","Hazel","Heather","Hearne","Heidi","Heida","Helene","Helga","Helma","Heloise","Hetha","Hilda","Hilary","Holda","Honore","Huela","Hyacinth","Ian","Ignatius","Irving","Ianthe","Ida","Idalie","Idelle","Ilse","Ingrid","Iona","Iris","Irma","Irmine"]
e = "    "
for i in range(1,30):
    cognoms = f"{e*2}<cognom>{random.choice(names)}</cognom>\n"
    for i in range(0,random.randint(1,4)):
        if random.randint(1,2) == 2:
            cognom = f"{e*2}<cognom>{random.choice(names)}</cognom>\n"
        else:
            cognom = ""
        cognoms = cognoms + cognom
    print(f"{e}<alumne>\n{e*2}<NIF>{str(random.randint(111111111,999999999))+ random.choice(string.ascii_letters).upper()}</NIF>\n{e*2}<nom>{random.choice(names)}</nom>\n{cognoms}{e}</alumne>")