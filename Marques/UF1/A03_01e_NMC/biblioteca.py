import random as rd
tia = ["ULYSSES","James Joyce","THE GREAT GATSBY","F. Scott Fitzgerald","A PORTRAIT OF THE ARTIST AS A YOUNG MAN","James Joyce","LOLITA","Vladimir Nabokov","BRAVE NEW WORLD","Aldous Huxley","THE SOUND AND THE FURY","William Faulkner","CATCH-22","Joseph Heller","DARKNESS AT NOON","Arthur Koestler","SONS AND LOVERS","D.H. Lawrence","THE GRAPES OF WRATH","John Steinbeck","UNDER THE VOLCANO","Malcolm Lowry","THE WAY OF ALL FLESH","Samuel Butler","1984","George Orwell","I, CLAUDIUS","Robert Graves","TO THE LIGHTHOUSE","Virginia Woolf","AN AMERICAN TRAGEDY","Theodore Dreiser","THE HEART IS A LONELY HUNTER","Carson McCullers","SLAUGHTERHOUSE-FIVE","Kurt Vonnegut","INVISIBLE MAN","Ralph Ellison","NATIVE SON","Richard Wright","HENDERSON THE RAIN KING","Saul Bellow","APPOINTMENT IN SAMARRA","John O’Hara","U.S.A.(trilogy)","John Dos Passos","WINESBURG, OHIO","Sherwood Anderson","A PASSAGE TO INDIA","E.M. Forster","THE WINGS OF THE DOVE","Henry James","THE AMBASSADORS","Henry James","TENDER IS THE NIGHT","F. Scott Fitzgerald","THE STUDS LONIGAN TRILOGY","James T. Farrell","THE GOOD SOLDIER","Ford Madox Ford","ANIMAL FARM","George Orwell","THE GOLDEN BOWL","Henry James","SISTER CARRIE","Theodore Dreiser","A HANDFUL OF DUST","Evelyn Waugh","AS I LAY DYING","William Faulkner","ALL THE KING’S MEN","Robert Penn Warren","THE BRIDGE OF SAN LUIS REY","Thornton Wilder","HOWARDS END","E.M. Forster","GO TELL IT ON THE MOUNTAIN","James Baldwin","THE HEART OF THE MATTER","Graham Greene","LORD OF THE FLIES","William Golding","DELIVERANCE","James Dickey","A DANCE TO THE MUSIC OF TIME (series)","Anthony Powell","POINT COUNTER POINT","Aldous Huxley","THE SUN ALSO RISES","Ernest Hemingway","THE SECRET AGENT","Joseph Conrad","NOSTROMO","Joseph Conrad","THE RAINBOW","D.H. Lawrence","WOMEN IN LOVE","D.H. Lawrence","TROPIC OF CANCER","Henry Miller","THE NAKED AND THE DEAD","Norman Mailer","PORTNOY’S COMPLAINT","Philip Roth","PALE FIRE","Vladimir Nabokov","LIGHT IN AUGUST","William Faulkner","ON THE ROAD","Jack Kerouac","THE MALTESE FALCON","Dashiell Hammett","PARADE’S END","Ford Madox Ford","THE AGE OF INNOCENCE","Edith Wharton","ZULEIKA DOBSON","Max Beerbohm","THE MOVIEGOER","Walker Percy","DEATH COMES FOR THE ARCHBISHOP","Willa Cather","FROM HERE TO ETERNITY","James Jones","THE WAPSHOT CHRONICLES","John Cheever","THE CATCHER IN THE RYE","J.D. Salinger","A CLOCKWORK ORANGE","Anthony Burgess","OF HUMAN BONDAGE","W. Somerset Maugham","HEART OF DARKNESS","Joseph Conrad","MAIN STREET","Sinclair Lewis","THE HOUSE OF MIRTH","Edith Wharton","THE ALEXANDRIA QUARTET","Lawrence Durrell","A HIGH WIND IN JAMAICA","Richard Hughes","A HOUSE FOR MR BISWAS","V.S. Naipaul","THE DAY OF THE LOCUST","Nathanael West","A FAREWELL TO ARMS","Ernest Hemingway","SCOOP","Evelyn Waugh","THE PRIME OF MISS JEAN BRODIE","Muriel Spark","FINNEGANS WAKE","James Joyce","KIM","Rudyard Kipling","A ROOM WITH A VIEW","E.M. Forster","BRIDESHEAD REVISITED","Evelyn Waugh","THE ADVENTURES OF AUGIE MARCH","Saul Bellow","ANGLE OF REPOSE","Wallace Stegner","A BEND IN THE RIVER","V.S. Naipaul","THE DEATH OF THE HEART","Elizabeth Bowen","LORD JIM","Joseph Conrad","RAGTIME","E.L. Doctorow","THE OLD WIVES’ TALE","Arnold Bennett","THE CALL OF THE WILD","Jack London","LOVING","Henry Green","MIDNIGHT’S CHILDREN","Salman Rushdie","TOBACCO ROAD","Erskine Caldwell","IRONWEED","William Kennedy","THE MAGUS","John Fowles","WIDE SARGASSO SEA","Jean Rhys","UNDER THE NET","Iris Murdoch","SOPHIE’S CHOICE","William Styron","THE SHELTERING SKY","Paul Bowles","THE POSTMAN ALWAYS RINGS TWICE","James M. Cain","THE GINGER MAN","J.P. Donleavy","THE MAGNIFICENT AMBERSONS","Booth Tarkington"]
titol = []
autor = []
for x in range(0,200,2):
    titol.append(tia[x])

for x in range(1,200,2):
    autor.append(tia[x])

for x in range(0,100):
    print(f"<llibre>\n    <titol>{titol[x]}</titol>\n    <autor>{autor[x]}</autor>\n    <paginas>{rd.randint(200,950)}</paginas>\n    <any>{rd.randint(1930,2000)}</any>\n    <secció>{rd.randint(1,8)}</secció>\n    <fila>{rd.randint(1,20)}</fila>\n    <prestatge>{rd.randint(1,6)}</prestatge>\n</llibre>")