/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package listasjava.Main;

import java.util.ArrayList;
import java.util.Collections;

/**
 *
 * @author Sala de Sistemas
 */
public class Java {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        int a [] = new int [10];
        
        a[0] = 100;
        a[1] = 200;
        a[2] = 300;
        a[3] = 400;
        
        System.out.println("El valor del array es: "+a[0]);
        
        ArrayList<String> lst = new ArrayList();
        
        lst.add(0, "Emil");
        lst.add("Mateo");
        
        System.out.println("El Valor del array es: "+ lst);
        
        lst.remove(0);
        System.out.println("Array despues de eliminar: "+ lst);
        
        lst.clear();
        System.out.println("Array despues de Limpiar: " +lst);
        
        boolean existe = lst.contains("Emil");
        
        if(existe) {
            System.out.println("Hemos encontrado tu busqueda: " +lst);
        }else{
            System.out.println("Lo lamentamos no hemos encontrado tu busqueda: ");
        }
        
        lst.add(0, "Emil");
        lst.add("Mateo");
        lst.add("Castro");
        lst.add("Gallo");
        
        Collections.sort(lst);
        System.out.println("Ordenando la lista: " + lst);
        
        
        
        
        
        
    }
    
}
