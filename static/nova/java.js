var correctAnswers = 0;
var incorrectAnswer = 0;
function Submitform() {
    var p1Answers = document.querySelector(`Input[name="p1"]:checked`).value;
    var p2Answers = document.querySelector(`Input[name="p2"]:checked`).value;
    var p3Answers = document.querySelector(`Input[name="p3"]:checked`).value;
    var p4Answers = document.querySelector(`Input[name="p4"]:checked`).value;
    var p5Answers = document.querySelector(`Input[name="p5"]:checked`).value;
    var p6Answers = document.querySelector(`Input[name="p6"]:checked`).value;
    var p7Answers = document.querySelector(`Input[name="p7"]:checked`).value;
    var p8Answers = document.querySelector(`Input[name="p8"]:checked`).value;
    var p9Answers = document.querySelector(`Input[name="p9"]:checked`).value;
    var p10Answers = document.querySelector(`Input[name="p10"]:checked`).value;
    
    if (p1Answers === "a") {
        correctAnswers++;
    }else if(p1Answers === "b"){
        incorrectAnswer++;
        //document.write("La respuesta correcta de la <b> P1 es la opción A </b>"+"<br>");
    }else{
        incorrectAnswer++;
       // document.write("La respuesta correcta de la <b> P1 es la opción A </b>"+"<br>");
    }

    if (p2Answers === "b") {
        correctAnswers++;
    }else if(p1Answers === "a"){
        incorrectAnswer++;
        //document.write("La respuesta correcta de la <b> P2 es la opción B </b>"+"<br>");
    }else{
        incorrectAnswer++;
        //document.write("La respuesta correcta de la <b> P2 es la opción B </b>"+"<br>");
    }

    if (p3Answers === "a") {
        correctAnswers++; 
    }else if(p1Answers === "b"){
        incorrectAnswer++;
        //document.write("La respuesta correcta de la <b> P3 es la opcion a </b>"+"<br>");
    }else{
        incorrectAnswer++;
       // document.write("La respuesta correcta de la <b> P3 es la opcion a </b>"+"<br>");  
    }

    if (p4Answers === "a") {
        correctAnswers++;
    }else if(p1Answers === "b"){
        incorrectAnswer++;
       // document.write("La respuesta correcta de la <b> P4 es la opcion a </b>"+"<br>");
    }else{
        incorrectAnswer++;
        //document.write("La respuesta correcta de la <b> P4 es la opcion a </b>"+"<br>");
    }

    if (p5Answers === "c") {
        correctAnswers++;
    }else if(p1Answers === "a"){
        incorrectAnswer++;
        //document.write("La respuesta correcta de la <b> P5 es la opcion c </b>"+"<br>");
    }else{
        incorrectAnswer++;
        //document.write("La respuesta correcta de la <b> P5 es la opcion c </b>"+"<br>");
    }

    if (p6Answers === "b") {
        correctAnswers++; 
    }else if(p1Answers === "a"){
        incorrectAnswer++;
        //document.write("La respuesta correcta de la <b> P6 es la opcion b </b>"+"<br>");
    }else{
        incorrectAnswer++;
        //document.write("La respuesta correcta de la <b> P6 es la opcion b </b>"+"<br>");  
    }

    if (p7Answers === "b") {
        correctAnswers++;
    }else if(p1Answers === "a"){
        incorrectAnswer++;
        //document.write("La respuesta correcta de la <b> P7 es la opcion a </b>"+"<br>");
    }else{
        incorrectAnswer++;
        //document.write("La respuesta correcta de la <b> P7 es la opcion a </b>"+"<br>");
    }
    if (p8Answers === "a") {
        correctAnswers++;
    }else if(p1Answers === "b"){
        incorrectAnswer++;
        //document.write("La respuesta correcta de la <b> P8 es la opcion a </b>"+"<br>");
    }else{
        incorrectAnswer++;
       // document.write("La respuesta correcta de la <b> P8 es la opcion a </b>"+"<br>");
    }
    if (p9Answers === "b") {
        correctAnswers++; 
    }else if(p1Answers === "a"){
        incorrectAnswer++;
        //document.write("La respuesta correcta de la <b> P9 es la opcion b </b>"+"<br>");
    }else{
        incorrectAnswer++;
        //document.write("La respuesta correcta de la <b> P9 es la opcion b </b>"+"<br>");  
    }
    if (p10Answers === "c") {
        correctAnswers++; 
    }else if(p1Answers === "a"){
        incorrectAnswer++;
        //document.write("La respuesta correcta de la <b> P10 es la opcion c </b>"+"<br>");
    }else{
        incorrectAnswer++;
        //document.write("La respuesta correcta de la <b> P10 es la opcion c </b>"+"<br>");
    }         
    document.getElementById("result").innerHTML = "Respuestas Correctas: " + correctAnswers+"<br>"+"Respuestas Incorrectas: " + incorrectAnswer+"<br>";
    document.getElementById("p1").innerHTML = "<br>"+"La respuesta es la A"+"<br>";
    document.getElementById("p2").innerHTML = "<br>"+"La respuesta es la B"+"<br>";
    document.getElementById("p3").innerHTML = "<br>"+"La respuesta es la A"+"<br>";
    document.getElementById("p4").innerHTML = "<br>"+"La respuesta es la A"+"<br>";
    document.getElementById("p5").innerHTML = "<br>"+"La respuesta es la C"+"<br>";
    document.getElementById("p6").innerHTML = "<br>"+"La respuesta es la B"+"<br>";
    document.getElementById("p7").innerHTML = "<br>"+"La respuesta es la B"+"<br>";
    document.getElementById("p8").innerHTML = "<br>"+"La respuesta es la A"+"<br>";
    document.getElementById("p9").innerHTML = "<br>"+"La respuesta es la B"+"<br>";
    document.getElementById("p10").innerHTML = "<br>"+"La respuesta es la C"+"<br>";

}