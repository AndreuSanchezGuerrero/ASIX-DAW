#fem el bucle pq semre torni a crear el menu excepte q s'apreti la opcio de sortir

while [ $opc -ne 4 ]
do
    #Fem un menu per seleccionar l'exercici que volem executar
    echo "Quin exercici vols executar?"
    echo "1. Canvia la població de Bleins per Blanes."
    echo "2. Elimineu les tres primeres línies."
    echo "3. Imprimeix les línies 5 a 10."
    echo "4. Eliminar les línies que contenen Lane."
    echo "5. Imprimiu totes les línies en què els aniversaris són al novembre o desembre."
    echo "6. Annexa tres asteriscos al final de les línies que comencen amb Fred."
    echo "7. Substitueix la línia que comença per Jose, per JOSE SHA JUBILAT"
    echo "8. Canvia la data de naixement de Popeye per 11/14/46. Suposa que no saps la data original de Popeye. Utilitza una expressió regular per buscar-la."
    echo "9. Elimina totes les línies en blanc."
    echo "10. (Val per 4). Fent servir el awk fes alguna cosa interessant amb el fitxer anterior, indica el que has fet."
    echo "11. Regenera el fitxer original."
    echo "12. Sortir."
    echo "Introdueix el número de l'exercici que vols executar:"
    read opcio

    #Fem un case per executar l'exercici que hem seleccionat cuan ens doni el resultat pausem dins a intro de teclat i regenerem el menu
    case $opcio in
    1) sed 's/Bleins/Blanes/' fitxer.txt;;
    2) sed '1,3d' fitxer.txt;;
    3) sed -n '5,10p' fitxer.txt;;
    4) sed '/Lane/d' fitxer.txt;;
    5) sed -n '/11\|12/p' fitxer.txt;;
    6) sed 's/^Fred/Fred***/' fitxer.txt;;
    7) sed 's/^Jose/JOSE SHA JUBILAT/' fitxer.txt;;
    8) sed 's/3\/19\/35/11\/14\/46/' fitxer.txt;;
    9) sed '/^$/d' fitxer.txt;;
    10) awk '{print $1}' fitxer.txt;;
    11) tee fitxer.txt << EOF
        Steve Blenheim:238-923-7366:95 Latham Lane, Easton, PA 83755:11/12/56:20300
        Betty Boop:245-836-8357:635 Cutesy Lane, Hollywood, CA 91464:6/23/23:14500
        Igor Chevsky:385-375-8395:3567 Populus Place, Caldwell, NJ 23875:6/18/68:23400
        Norma Corder:397-857-2735:74 Pine Street, Dearborn, MI 23874:3/28/45:245700
        Jennifer Cowan:548-834-2348:583 Laurel Ave., Kingsville, TX 83745:10/1/35:58900
        Jon DeLoach:408-253-3122:123 Park St., San Jose, CA 04086:7/25/53:85100
        Karen Evich:284-758-2857:23 Edgecliff Place, Lincoln, NB 92743:7/25/53:85100
        Karen Evich:284-758-2867:23 Edgecliff Place, Lincoln, NB 92743:11/3/35:58200
        Karen Evich:284-758-2867:23 Edgecliff Place, Lincoln, NB 92743:11/3/35:58200
        Fred Fardbarkle:674-843-1385:20 Parak Lane, Duluth, MN 23850:4/12/23:780900
        Fred Fardbarkle:674-843-1385:20 Parak Lane, Duluth, MN 23850:4/12/23:780900
        Lori Gortz:327-832-5728:3465 Mirlo Street, Peabody, MA 34756:10/2/65:35200
        Paco Gutierrez:835-365-1284:454 Easy Street, Decatur, IL 75732:2/28/53:123500
        Ephram Hardy:293-259-5395:235 CarltonLane, Joliet, IL 73858:8/12/20:56700
        James Ikeda:834-938-8376:23445 Aster Ave., Allentown, NJ 83745:12/1/38:45000
        Barbara Kertz:385-573-8326:832 Ponce Drive, Gary, IN 83756:12/1/46:268500
        Lesley Kirstin:408-456-1234:4 Harvard Square, Boston, MA 02133:4/22/62:52600
        William Kopf:846-836-2837:6937 Ware Road, Milton, PA 93756:9/21/46:43500
        Sir Lancelot:837-835-8257:474 Camelot Boulevard, Bath, WY 28356:5/13/69:24500
        Jesse Neal:408-233-8971:45 Rose Terrace, San Francisco, CA 92303:2/3/36:25000
        Zippy Pinhead:834-823-8319:2356 Bizarro Ave., Farmount, IL 84357:1/1/67:89500
        Arthur Putie:923-835-8745:23 Wimp Lane, Kensington, DL 38758:8/31/69:126000
        Popeye Sailor:156-454-3322:945 Bluto Street, Anywhere, USA 29358:3/19/35:22350
        Jose Moreno:385-898-8357:24 Vilar Petit, Bleins, iSpain 17300:5/20/88:1000
        Tommy Savage:408-724-0140:1222 Oxbow Court, Sunnyvale, CA 94087:5/19/66:34200
        Yukio Takeshida:387-827-1095:13 Uno Lane, Ashville, NC 23556:7/1/29:57000
        Vinh Tranh:438-910-7449:8235 Maple Street, Wilmington, VM 29085:9/23/63:68900
    EOF
    ;;
    *) echo "Opció incorrecta";;
    esac

