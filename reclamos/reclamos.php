<?php
if(empty($_POST['nombre']) || empty($_POST['asunto']) || empty($_POST['incidente']) || !filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) {
  http_response_code(500);
  exit();
}

$nombre = strip_tags(htmlspecialchars($_POST['nombre']));
$email = strip_tags(htmlspecialchars($_POST['email']));
$m_asunto = strip_tags(htmlspecialchars($_POST['asunto']));
$incidente = strip_tags(htmlspecialchars($_POST['incidente']));
$placa = strip_tags(htmlspecialchars($_POST['placa']));
$information = strip_tags(htmlspecialchars($_POST['information']));
$description = strip_tags(htmlspecialchars($_POST['description']));





$to = "info@example.com"; // Change this email to your //
$subject = "$m_asunto:  $nombre";
$body = "Mensaje recivido desde el formulario de reclamos.\n\n"."Detalles:\n\nNombre: $nombre\n\n\Correo: $correo\n\Asunto: $m_asunto\n\nPlaca: $placa\n\nincidente: $incidente \n\ninformation: $information\n\ndescription: $description";
$header = "From: $email";
$header .= "Reply-To: $email";	

if(!mail($to, $asunto, $body, $header))
  http_response_code(500);
?>
