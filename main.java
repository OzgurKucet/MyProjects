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
                
                System.out.print(array[0]+" Türkçesi :");
                int hak = 3;
                while(scanner.hasNextLine()){
                    if(hak == 0){
                        System.out.println("doðrusu:"+array[1]);
                        yanlisSayisi++;
                        break;
                    }
                    
                    String ad = scan.nextLine();
                    try{
                    	if(ad.equals("1")){
                    		System.out.println("doðrusu:"+array[1]);
                    		jokerSayisi++;
                            break;
                    	}
                    if(array[1].equals(ad)){
                        System.out.println("Doðru...");
                        dogruSayisi++;
                        break;
                    }
                    else if(!array[2].isEmpty()){
                        if(array[2].equals(ad)){
                        System.out.println("Doðru...");
                        dogruSayisi++;
                        break;
                        }                        
                    }
                    else if(!array[3].isEmpty()){
                        if(array[3].equals(ad)){
                        System.out.println("Doðru...");
                        dogruSayisi++;
                        break;
                        }                        
                    }
                    }catch (ArrayIndexOutOfBoundsException ex) {
                        
                    }
                    
                    System.out.println("Yanlýþ girdiniz tekrar deneyin kalan hak: "+hak);
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
                
                System.out.print(array[1]+" Ýngilizcesi :");
                int hak = 3;
                while(scanner.hasNextLine()){
                    if(hak == 0){
                        System.out.println("doðrusu:"+array[0]);
                        yanlisSayisi++;
                        break;
                    }
                    
                    String ad = scan.nextLine();
                    try{
                    	if(ad.equals("1")){
                    		System.out.println("doðrusu:"+array[0]);
                    		jokerSayisi++;
                            break;
                    	}
                    if(array[0].equals(ad)){
                        System.out.println("Doðru...");
                        dogruSayisi++;
                        break;
                    }
                          
                   
                    }catch (ArrayIndexOutOfBoundsException ex) {
                        
                    }
                    
                    System.out.println("Yanlýþ girdiniz tekrar deneyin kalan hak: "+hak);
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
		
			
		String islemler = "Hangi Bölümü Açmak Ýstiyorsun\n"
						+ "1.Bölüm A harfi ile Baþliyanlar için 1 gir\n"
						+ "2.Bölüm B harfi ile Baþliyanlar için 2 gir\n"
						+ "3.Bölüm C harfi ile Baþliyanlar için 3 gir\n"
						+ "4.Bölüm D ve E harfi ile Baþliyanlar için 4 gir\n"
						+ "5.Bölüm F ve G harfi ile Baþliyanlar için 5 gir\n"
						+ "6.Bölüm H ve I harfi ile Baþliyanlar için 6 gir\n"
						+ "7.Bölüm J,K ve L harfi ile Baþliyanlar için 7 gir\n"
						+ "8.Bölüm M ve N harfi ile Baþliyanlar için 8 gir\n"
						+ "9.Bölüm O ve P harfi ile Baþliyanlar için 9 gir\n"
						+ "10.Bölüm Q ve R harfi ile Baþliyanlar için 10 gir\n"
						+ "11.Bölüm S harfi ile Baþliyanlar için 11 gir\n"
						+ "12.Bölüm T,U,W,Y ve Z harfi ile Baþliyanlar için 12 gir\n"
						+ "Çýkýþ için -1 e basýn...\n";
		
		
		
		while(true){
			System.out.println("Türkçeden ingilizceye çevirmek için 1\n"
					 		 + "Ýngilizceden türkçeye çevirmek için 2 girin\n");
	
			int dilIslem = scan.nextInt();
						
			if(dilIslem == 2){
				System.out.println(islemler);
				System.out.print("seçim:");
				int islem = scan.nextInt();
				if(islem == -1){
					System.out.println("Programdan çýkýlýyor...");
					break;
				}
				if(islem < 7 && islem >0){
					KelimeYazTr(DosyaIsmi(islem));
				}
				else{
					System.out.println("Geçersiz iþlem! Tekrar Deneyin...");
				}
			
			}
			else if(dilIslem == 1){
				System.out.println(islemler);
				System.out.print("seçim:");
				int islem = scan.nextInt();
				if(islem == -1){
					System.out.println("Programdan çýkýlýyor...");
					break;
				}
				if(islem < 7 && islem >0){
					KelimeYazEn(DosyaIsmi(islem));
				}
				else{
					System.out.println("Geçersiz iþlem! Tekrar Deneyin...");
				}
				
			}
		
		}
	
	}
}
