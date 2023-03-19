package br.com.fiap;

import javax.swing.JOptionPane;

public class Base {

	public static void main(String[] args) {

		
float base = 0.0f, altura = 0.0f , area = 0.0f;
String aux;
try {
	aux = JOptionPane.showInputDialog("Digite a altura do triangulo:");
	altura = Float.parseFloat(aux);
	aux = JOptionPane.showInputDialog("Digite a base do triangulo:");
	base = Float.parseFloat(aux);
	area = altura * base / 2;
	JOptionPane.showMessageDialog(null, "A area do retangulo é:" + area);	
} catch (Exception e) {
	// TODO: handle exception
}
}
}


