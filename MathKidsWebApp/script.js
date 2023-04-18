var mali=0,tama=0, sagot;

function x(){
    
    var sagoti=sagot;
    var varnum = [0,1,2,3,4,5,6,7,8,9];
    var num1a = varnum[Math.floor(Math.random() * varnum.length)];
    document.getElementById('p2').innerHTML= num1a;  
    
    var num1b = varnum[Math.floor(Math.random() * varnum.length)];
    document.getElementById('p1').innerHTML= num1b;  

    document.getElementById('operation').innerHTML= "+";  
    document.getElementById('equal').innerHTML= "=";  
    sagot=num1a+num1b;
    var userAns=document.getElementById("ans").value;
  document.getElementById("mali").innerHTML = mali;
  document.getElementById("tama").innerHTML = tama;
    
    if(sagoti!=userAns){
    document.getElementById("checking").innerHTML = "Mali";
    mali++;
    }
   else{
   document.getElementById("checking").innerHTML = "Tama";
   tama++;
   }

    }
    
    
    