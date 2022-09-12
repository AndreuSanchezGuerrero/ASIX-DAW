import random
import string
import datetime
start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2020, 2, 1)

time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days
random_number_of_days = random.randrange(days_between_dates)
random_date = start_date + datetime.timedelta(days=random_number_of_days)

names = ["Anabel","Ariana","Arielle","Ashley","Audrey","Autumn","Baen","Baethan","Baird","Baldemar","Baldwin","Banan","Banning","Bardaric","Barnom","Barrett","Barrington","Barron","Barry","Barton","Bartram","Basil","Baxter","Bayard","Beacan","Beacher","Beal","Beau","Beauvais","Beck","Benen","Benjamin","Bennett","Benniton","Benoit","Berkeley","Bert","Bertin","Bingham","birche","Blaine","Blair","Blaise","Blake","Booker","Boris","Bradley","Brandon","Brayden","Brett","Brian","Brit","Brock","Keanan","Kearne","Kearney","Keaton","Kedric","Keely","Keith","Kelby","Kelly","Kelvyn","Ken","Kendall","Kenneth","Kent","Kerwin","Kevin","Kimball","Kingston","Kolby","Konrad","Kyle","Kacia","Kaitlyn","Kalista","Karen","Karla","Karisma","Katherine","Katrina","Lafayette","Lamar","Lambart","Lamont","Lance","Lancelot","Landis","Landon","Langdon","Langley","Laramie","Lars","Lasalle","Laughlin","Laurent","Layton","Lawley","Leal","Leander","Lear","Lee","Leigh","Lehman","Harcourt","Harbin","Hardy","Harford","Harlan","Harland","Harmon","Harold","Harris","Hartman","Hartwood","Haslett","Haven","Hawly","Hendrix","Hadley","Hailey","Halle","Hallette","Hannah","Harmony","Harriet","Hazel","Heather","Hearne","Heidi","Heida","Helene","Helga","Helma","Heloise","Hetha","Hilda","Hilary","Holda","Honore","Huela","Hyacinth","Ian","Ignatius","Irving","Ianthe","Ida","Idalie","Idelle","Ilse","Ingrid","Iona","Iris","Irma","Irmine"]
e = "    "
for i in range(0,50):
    cognoms = ""
    telefons = ""
    data = ""
    edat = ""
    rdi = random.randint(1,3)
    clau = f"{e*2}<clau>"
    if  rdi == 2:
        clau = clau + str(random.randint(111,999))+"_"+str(random_date)
        clau = clau + "</clau>\n"
    elif rdi == 3:
        clau = clau + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        clau = clau + "</clau>\n"
    else:
        clau = ""
    for i in range(1,random.randint(2,3)):
        cognom = f"{e*2}<cognom>{random.choice(names)}</cognom>\n"
        cognoms = cognoms + cognom
    if random.randint(1,2) == 2:
        data = f"{e*2}<datanaixement>"
        data = f"{data}{random.randint(1,31)}/{random.randint(1,12)}/{random.randint(1997,2003)}"
        data = f"{data}</datanaixement>\n"
    else:
        data = f"{e*2}<edat>{random.randint(18,50)}</edat>\n"
    for i in range(1,random.randint(2,5)):
        telefon = f"{e*2}<telefon>{str(random.randint(611111111,699999999))}</telefon>\n"
        telefons = telefons + telefon
    print(f"{e}<soci>\n{clau}{e*2}<nom>{random.choice(names)}</nom>\n{cognoms}{data}{telefons}{e}</soci>")