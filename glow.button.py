<!DOCTYPE html>
<html>
<head>
  <title>Glow Button</title>

  <style>

    body{
      display:flex;
      justify-content:center;
      align-items:center;
      height:100vh;
      background:black;
    }

    button{
      padding:15px 35px;
      font-size:20px;
      border:none;
      border-radius:30px;
      background:#ff00ff;
      color:white;
      cursor:pointer;
      box-shadow:0 0 20px #ff00ff;
      transition:0.3s;
    }

    button:hover{
      box-shadow:0 0 40px #ff00ff;
      transform:scale(1.1);
    }

  </style>
</head>

<body>

  <button>Click Me ✨</button>

</body>
</html>