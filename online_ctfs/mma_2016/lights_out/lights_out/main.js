document.addEventListener('DOMContentLoaded', function() {
  var level = document.getElementById('level');
  var game = {};
  var canvas = document.getElementById('main');
  var levelChanged = function() {
    var map = data[level.value];
    canvas.width = map.width * map.size;
    canvas.height = map.height * map.size;
    game.width = map.width;
    game.height = map.height;
    game.size = map.size;
    var ctx = canvas.getContext('2d');
    // grid
    for(var y = 0; y < map.height; y++) {
      ctx.beginPath();
      ctx.moveTo(0, (y + 1) * map.size);
      ctx.lineTo(canvas.width, (y + 1) * map.size);
      ctx.closePath();
      ctx.strokeStyle = '#ddd';
      ctx.stroke();
    }
    for(var x = 0; x < map.width; x++) {
      ctx.beginPath();
      ctx.moveTo((x + 1) * map.size, 0);
      ctx.lineTo((x + 1) * map.size, canvas.height);
      ctx.closePath();
      ctx.strokeStyle = '#ddd';
      ctx.stroke();
    }
    // get status
    game.remain = 0;
    game.clicked = Array(map.height);
    game.state = Array(map.height);
    for(var y = 0; y < map.height; y++) {
      game.clicked[y] = Array(map.width);
      game.state[y] = Array(map.width);
      for(var x = 0; x < map.width; x++) {
        game.clicked[y][x] = 0;
        game.state[y][x] = map.map[y * map.width + x] == '1' ? 1 : 0;
        if(game.state[y][x] === 1) {
          game.remain++;
          ctx.fillStyle = 'black';
          ctx.fillRect(x * map.size + 1, y * map.size + 1, map.size - 1, map.size - 1);
        }
      }
    }
  };

  canvas.addEventListener('click', function(e) {
    if(game.remain === 0) return;
    var rect = e.target.getBoundingClientRect();
    var x = e.clientX - rect.left;
    var y = e.clientY - rect.top;
    var tx = Math.floor(x / game.size);
    var ty = Math.floor(y / game.size);
    if(0 <= tx && tx < game.width && 0 <= ty && ty < game.height) {
      var ctx = canvas.getContext('2d');
      var dx = [0,1,2,1,0,-1,-2,-1], dy = [-2,-1,0,1,2,1,0,-1];
      game.clicked[ty][tx] ^= 1;
      for(var i = 0; i < 8; i++) {
        var nx = tx + dx[i], ny = ty + dy[i];
        if(0 <= nx && nx < game.width &&
            0 <= ny && ny < game.height) {
          game.state[ny][nx] ^= 1;
          if(game.state[ny][nx] == 0) {
            game.remain--;
            ctx.fillStyle = '#ffffff';
          } else {
            game.remain++;
            ctx.fillStyle = '#000000';
          }
          ctx.fillRect(nx * game.size + 1, ny * game.size + 1, game.size - 1, game.size - 1);
        }
      }
    }
    if(game.remain == 0) {
      alert("Congratulations! I'll check your solution. Wait a moment.");
      var message = '';
      for(var y = 0; y < game.height; y++) {
        for(var x = 0; x < game.width; x++) {
          message += game.clicked[y][x] === 1 ? '1' : '0';
        }
      }
      var req = new XMLHttpRequest();
      req.open('POST', 'http://ppc1.chal.ctf.westerns.tokyo:19283/check', true);
      req.setRequestHeader('Content-Type', 'application/json')
      req.send(JSON.stringify({
        level: level.value,
        clicked: message
      }));

      req.onreadystatechange = function() {
        if(req.readyState == 4) {
          if(req.status === 200) {
            var result = JSON.parse(req.responseText);
            if(result.result == 'Wrong') {
              alert('Wrong');
            }else if(result.result == 'Correct') {
              alert(result.message);
            }
          } else {
            alert('Something wrong');
          }
        }
      }
    }
  });
  levelChanged(level.value);
  level.addEventListener('change', levelChanged);
});
