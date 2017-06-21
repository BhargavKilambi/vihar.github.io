class Increment{  
static int count=0;//will get memory only once and retain its value  
  
Increment(){  
count++;  
System.out.println(count);  
}  
  
public static void main(String args[]){  
  
Increment c1=new Increment();  
Increment c2=new Increment();  
Increment c3=new Increment();  
  
 }  
} 