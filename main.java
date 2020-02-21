import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;


public class main {

	private static int soruSayisi;
	private static int jokerSayisi;
	private static int dogruSayisi;
	private static int yanlisSayisi;
	
	public static void KelimeYazTr(String dosyaAdi){
		
		try(Scanner scanner = new Scanner(new FileReader(dosyaAdi))){
			
			while(scanner.hasNextLine()){
                soruSayisi++;
                String kelimeBilgisi = scanner.nextLine();
                
                String[] array = kelimeBilgisi.split(":");
                
                Scanner scan = new Scanner(System.in);
                
                System.out.print(array[0]+" T�rk�esi :");
                int hak = 3;
                while(scanner.hasNextLine()){
                    if(hak == 0){
                        System.out.println("do�rusu:"+array[1]);
                        yanlisSayisi++;
                        break;
                    }
                    
                    String ad = scan.nextLine();
                    try{
                    	if(ad.equals("1")){
                    		System.out.println("do�rusu:"+array[1]);
                    		jokerSayisi++;
                            break;
                    	}
                    if(array[1].equals(ad)){
                        System.out.println("Do�ru...");
                        dogruSayisi++;
                        break;
                    }
                    else if(!array[2].isEmpty()){
                        if(array[2].equals(ad)){
                        System.out.println("Do�ru...");
                        dogruSayisi++;
                        break;
                        }                        
                    }
                    else if(!array[3].isEmpty()){
                        if(array[3].equals(ad)){
                        System.out.println("Do�ru...");
                        dogruSayisi++;
                        break;
                        }                        
                    }
                    }catch (ArrayIndexOutOfBoundsException ex) {
                        
                    }
                    
                    System.out.println("Yanl�� girdiniz tekrar deneyin kalan hak: "+hak);
                    hak--;
                    
                    
                }
                
            }
			
			 System.out.println("\n\n\nPuan="+(soruSayisi-yanlisSayisi-jokerSayisi-1));
	         System.out.println("Dogru Sayisi="+(dogruSayisi));
	         System.out.println("Yanlis Sayisi="+yanlisSayisi+"Joker Sayisi="+jokerSayisi);
	         System.out.println("\n\n\n");
			
			
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		catch (IOException e) {
		e.printStackTrace();
		}
		
	}
	
public static void KelimeYazEn(String dosyaAdi){
		
		try(Scanner scanner = new Scanner(new FileReader(dosyaAdi))){
			
			while(scanner.hasNextLine()){
                soruSayisi++;
                String kelimeBilgisi = scanner.nextLine();
                
                String[] array = kelimeBilgisi.split(":");
                
                Scanner scan = new Scanner(System.in);
                
                System.out.print(array[1]+" �ngilizcesi :");
                int hak = 3;
                while(scanner.hasNextLine()){
                    if(hak == 0){
                        System.out.println("do�rusu:"+array[0]);
                        yanlisSayisi++;
                        break;
                    }
                    
                    String ad = scan.nextLine();
                    try{
                    	if(ad.equals("1")){
                    		System.out.println("do�rusu:"+array[0]);
                    		jokerSayisi++;
                            break;
                    	}
                    if(array[0].equals(ad)){
                        System.out.println("Do�ru...");
                        dogruSayisi++;
                        break;
                    }
                          
                   
                    }catch (ArrayIndexOutOfBoundsException ex) {
                        
                    }
                    
                    System.out.println("Yanl�� girdiniz tekrar deneyin kalan hak: "+hak);
                    hak--;
                    
                    
                }
                
            }
			
			 System.out.println("\n\n\nPuan="+(soruSayisi-yanlisSayisi-jokerSayisi-1));
	         System.out.println("Dogru Sayisi="+(dogruSayisi));
	         System.out.println("Yanlis Sayisi="+yanlisSayisi+"Joker Sayisi="+jokerSayisi);
	         System.out.println("\n\n\n");
			
			
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		catch (IOException e) {
		e.printStackTrace();
		}
		
	}
	
	public static String DosyaIsmi(int i){
		
		return String.format("Kelimeler%d.txt",i);
		
	}
	
	public static void main(String[] args){
		
		
		
		Scanner scan = new Scanner(System.in);
		
			
		String islemler = "Hangi B�l�m� A�mak �stiyorsun\n"
						+ "1.B�l�m A harfi ile Ba�liyanlar i�in 1 gir\n"
						+ "2.B�l�m B harfi ile Ba�liyanlar i�in 2 gir\n"
						+ "3.B�l�m C harfi ile Ba�liyanlar i�in 3 gir\n"
						+ "4.B�l�m D ve E harfi ile Ba�liyanlar i�in 4 gir\n"
						+ "5.B�l�m F ve G harfi ile Ba�liyanlar i�in 5 gir\n"
						+ "6.B�l�m H ve I harfi ile Ba�liyanlar i�in 6 gir\n"
						+ "7.B�l�m J,K ve L harfi ile Ba�liyanlar i�in 7 gir\n"
						+ "8.B�l�m M ve N harfi ile Ba�liyanlar i�in 8 gir\n"
						+ "9.B�l�m O ve P harfi ile Ba�liyanlar i�in 9 gir\n"
						+ "10.B�l�m Q ve R harfi ile Ba�liyanlar i�in 10 gir\n"
						+ "11.B�l�m S harfi ile Ba�liyanlar i�in 11 gir\n"
						+ "12.B�l�m T,U,W,Y ve Z harfi ile Ba�liyanlar i�in 12 gir\n"
						+ "��k�� i�in -1 e bas�n...\n";
		
		
		
		while(true){
			System.out.println("T�rk�eden ingilizceye �evirmek i�in 1\n"
					 		 + "�ngilizceden t�rk�eye �evirmek i�in 2 girin\n");
	
			int dilIslem = scan.nextInt();
						
			if(dilIslem == 2){
				System.out.println(islemler);
				System.out.print("se�im:");
				int islem = scan.nextInt();
				if(islem == -1){
					System.out.println("Programdan ��k�l�yor...");
					break;
				}
				if(islem < 7 && islem >0){
					KelimeYazTr(DosyaIsmi(islem));
				}
				else{
					System.out.println("Ge�ersiz i�lem! Tekrar Deneyin...");
				}
			
			}
			else if(dilIslem == 1){
				System.out.println(islemler);
				System.out.print("se�im:");
				int islem = scan.nextInt();
				if(islem == -1){
					System.out.println("Programdan ��k�l�yor...");
					break;
				}
				if(islem < 7 && islem >0){
					KelimeYazEn(DosyaIsmi(islem));
				}
				else{
					System.out.println("Ge�ersiz i�lem! Tekrar Deneyin...");
				}
				
			}
		
		}
	
	}
}
