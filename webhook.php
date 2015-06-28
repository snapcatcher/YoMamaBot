<?php
$json = json_decode(file_get_contents('php://input'), true);

$chat_id = $json['message']['chat']['id'];
$message = $json['message']['text'];
$author_id = $json['message']['from']['id'];
$author_name = $json['message']['from']['first_name'];
$current_datetime = date('Ymd-H:i');

$log_file = "yomama.log";
$file = fopen($log_file, "a") or die("can't open file");

trigger_error($author_name);

$append_string = $current_datetime . ': ' . $author_name . '(' . $author_id . ") " . "in chat id = " . $chat_id . "message: " . $message .  "\n";
fwrite($file, $append_string);
fclose($file);


$command = escapeshellcmd('/usr/bin/python /var/www/yomama/YoMamaBot.py ' . $chat_id . ' ' . $message);

shell_exec($command);

?>
