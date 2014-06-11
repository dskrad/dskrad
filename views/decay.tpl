<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
		<meta name="apple-mobile-web-app-capable" content="yes" />
		<meta name="apple-mobile-web-app-status-bar-style" content="black" />
		<title>
			Decayed Activity
		</title>
    <link rel="apple-touch-startup-image" href="/startup.png"/>
		<link rel="stylesheet" href="/jquery.mobile-1.3.0.min.css" />
		<link rel="stylesheet" href="/my.css" />
		<script src="http://code.jquery.com/jquery-1.7.2.min.js">
		</script>
		<script src="/jquery.mobile-1.3.0.min.js">
		</script>
		<script src="/my.js">
		</script>
		<!-- User-generated css -->
		<style>
		</style>
		<!-- User-generated js -->
		<script>
		try {
		} 
    catch (error) {
		console.error("Your javascript has an error: " + error);
		}
		</script>
	</head>
	<body>
	
		<!-- Home -->
		<div data-role="page" id="page1" data-theme="a">
      <div data-role="header">
        <h3>{{header}}</h3>
      </div>
      <div data-role"content">
      <ul data-role="listview">
      % for item in content:
        <li>{{item}}</li>
      % end
      </ul>
      </div>
		</div>
		
	</body>
</html>
