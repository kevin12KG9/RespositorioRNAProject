<?php
 require_once "calculos.php";

$objeto = new calculadora();

$n1 = $_POST['numero1'];
$n2 = $_POST['numero2'];
$op = $_POST['operacion'];


//echo $n1."<br>".$n2."<br>".$op;

//echo "El resultado es: ".$objeto -> calcular($n1, $n2, $op);

try {
    // Código que podría generar una excepción
    echo "El resultado es: ".$objeto -> calcular($n1, $n2, $op); // Esto generará una excepción de división entre cero
} catch (Exception $e) {
    // Manejar la excepción
    echo "Se ha producido una excepción: " . $e->getMessage();
}


?>
