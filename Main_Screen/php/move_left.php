<?php exec('sudo python ../python/mv_lt.py'); ?>

<html>
<head>
	<title>Let's Start RPC</title>
	<link rel="stylesheet" type="text/css" href="../css/style.css">
</head>
<body>
	<div class="switch">
		<div class="body">
			<div class="volume"></div>
			<div class="screen">
				<div class="stream">
					<!-- Display a stream on here. -->
					<img src="http://192.168.10.135:8081">
				</div>
			<!--
				<div class="logo">
					<div class="icon">
						<div class="icon-part left">
						</div>
						<div class="icon-part right"></div>
					</div>
					<h1><span>Nintendo</span>Switch</h1>
				</div>
			-->
			</div>
	    </div>
														  
	    <div class="joy-con left">
		    <div class="button-group">
				<div class="button arrow up">
					<form method="post" action="move_forward.php">
						<input type="submit" name="btn_forward" value="forward">
					</form>
				</div>
				<div class="button arrow right">
					<form method="post" action="move_right.php">
						<input type="submit" name="btn_right" value="right">
					</form>
				</div>
				<div class="button arrow down">
					<form method="post" action="move_backward.php">
						<input type="submit" name="btn_down" value="backward">
					</form>
				</div>
				<div class="button arrow left">
					<form method="post" action="move_left.php">
						<input type="submit" name="btn_left" value="left">
					</form>
				</div>
			</div>
															    
			<div class="stick"></div>
			<div class="select"></div>
		    <div class="capture">
				<form method="post" action="move_stop.php">
					<input type="submit" name="btn_stop" value="stop">
				</form>	
			</div>
		    <div class="shoulder l"></div>
		</div>
		<div class="joy-con right">
			<div class="button-group">
	     		<div class="button letter" data-letter="X"></div>
	     		<div class="button letter" data-letter="Y"></div>
				<div class="button letter" data-letter="A"></div>
		        <div class="button letter" data-letter="B">
					<!-- <form method="post" action="move_stop.php">
						<input type="submit" name="btn_stop" value="stop">
					</form>	 -->
				</div>
	        </div>
   		    <div class="stick"></div>
       		<div class="start"></div>
       		<div class="home"></div>
       		<div class="shoulder r"></div>
	    </div>
	</div>
</body>
</html>
