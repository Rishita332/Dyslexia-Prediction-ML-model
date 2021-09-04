<?php
// database connection code
// $con = mysqli_connect('localhost', 'database_user', 'database_password','database');

$con = mysqli_connect('localhost', 'root', 'your_password','dyslexia');

// get the post records
$m1 = $_POST['q1'];
    $m2 = $_POST['q2'];
    $m3 = $_POST['q3'];
    $m4 = $_POST['q4'];
    $m5 = $_POST['q5'];
    $m6 = $_POST['q6'];
    $m7 = $_POST['q7'];
    $m8 = $_POST['q8'];
    $m9 = $_POST['q9'];
    $m10 = $_POST['q10'];
    $m11 = $_POST['q11'];
    $m12 = $_POST['q12'];
    $m13 = $_POST['q13'];
    $m14 = $_POST['q14'];
    $m15 = $_POST['q15'];
    $m16 = $_POST['q16'];
    $m17 = $_POST['q17'];
    $m18 = $_POST['q18'];
    $m19 = $_POST['q19'];
    $m20 = $_POST['q20'];


// database insert SQL code

$sql = "INSERT INTO 'survey' ('m1', 'm2', 'm3', 'm4', 'm5', 'm6' ,'m7' ,'m8' ,'m9', 'm10', 'm11', 'm12', 'm13', 'm14', 'm15', 'm16' ,'m17' ,'m18' ,'m19', 'm20') VALUES ('$m1', '$m2', '$m3', '$m4', '$m5', '$m6' ,'$m7' ,'$m8' ,'$m9', '$m10', '$m11', '$m12', '$m13', '$m14', '$m15', '$m16' ,'$m17' ,'$m18' ,'$m19', '$m20');"
    ;
// insert in database 
$rs = mysqli_query($con, $sql);

if($rs)
{
	echo "Answers submitted successfully";
}

?>