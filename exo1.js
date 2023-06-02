function  sontInvOuOpp(a,b){

    if(a+b==0 || a*b == 1){
        return true;
    } else{
        return false;
    }
}
function existeInvOuOppConsecutif(T){
    
        if(sontInvOuOpp(T[0]+T[1])){
            return true;
        } else{
            return false;
        }
}

function existeInvOuOpp(T){
    for( var i=0;i<T.length;i++){
        for( var j=0;j<T.length;j++){
            if(sontInvOuOpp(T[i],T[j])){
                return true;
            }
        }
    }
    return false;
}
var a=1;
var b=2;
var tab=[1,2];
var tab2=[1,2,4,10];
var test1= sontInvOuOpp(a,b);
var test2= existeInvOuOppConsecutif(tab);
var test3= existeInvOuOpp(tab);
document.write("Exo1_a "+a+" et "+b+" "+test1+"</br>");
document.write("Exo1_b "+T[0]+" et "+T[1]+" "+test2+"</br>");
document.write("Exo1_c "+test3+"</br>");



// function nbvInvOuOpp(T){
//     var a;
//     var b;
//     var tableau_indice=;
//     for( var i=0;i<T.length;i++){
//         for( var j=0;j<T.length;j++){
//             if(sontInvOuOpp(T[i],T[j])){
//                 tableau_indice[]
//             }
//         }
//     }
//     return false;
// }