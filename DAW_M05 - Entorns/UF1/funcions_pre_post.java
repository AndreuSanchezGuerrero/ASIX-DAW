//Per cada funcio li fem una descripcio, diem quins parametres te i quin tipus de dades retorna

        /*@description: funcio q crea un vector
        @param: enter mes gran que 0 que indica la mida del vector
        @return: retorna el vector creat amb numeros aleatoris*/

        int crearVector (int n){
            int [] v;
            for (int i = 0; i < n; i++) {
                v[i] = Math.Random();  //la funció interna Random de la classe Math retorna un número enter aleatori 
            }
        return v;
        }

        /*
        @description: 
        @param: 
        @return:
        */
        int _______________ (int [][] m){
            int parell=0,senar=0;	
            for (int i = 0; i < m.length; i++) {
                for (int j = 0; j < m.length; j++){
                    if (m[i][j]% 2 == 0) {
                        parell = parell + 1;
                    } else {
                        senar = senar + 1;
                    }
                }
            }
            if (parell > senar){
                return parell;
            }
            else if (senar > parell){
                return senar;
            }
            else return 0;
        }

        /* 
        @description: explicar la funcio
        @param: parametres d'entrada n de tipus enter
        @return: retorna enter
        */

        String mostraContingut(int[] vector){
            int i;
            i=0;
            while(vector[i]!='\0'){
            System.out.print(vector[i]);
            i++;
            }
        }

        /* 
        @description: explicar la funcio
        @param: parametres d'entrada n de tipus enter
        @return: retorna enter
        */

        boolean hihaParells (int[x] v){
            int i=0;
            while ((v[i]%2 != 0) && (i <= v.length)){  //v.lenght ens diu la longitud del vector
                i=i+1;
            }
            return (i != v.length);
        }
    }

